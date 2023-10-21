import time, json, copy

from visualizer import *
from stadium_variables import *
import calc_batting
import PySimpleGUI as sg
from random import randint
from os.path import exists

render_dimensions = (1280, 720)

DEFAULT_STADIUM = "Stadiums/Mario Stadium.json"

CHARACTERNAME_TO_ID = {
    "Mario": 0,
    "Luigi": 1
}

ID_TO_CHARACTERNAME = {v: k for k, v in CHARACTERNAME_TO_ID.items()}


KEYBOARD_CAMERA_CONTROLS = {
    pygame.K_w      : lambda movement, delta_time, sensitivity : movement + (Vector3(0, 0, 1) * delta_time * sensitivity),
    pygame.K_s      : lambda movement, delta_time, sensitivity : movement - (Vector3(0, 0, 1) * delta_time * sensitivity),
    pygame.K_q      : lambda movement, delta_time, sensitivity : movement + (Vector3(0, 1, 0) * delta_time * sensitivity),
    pygame.K_e      : lambda movement, delta_time, sensitivity : movement - (Vector3(0, 1, 0) * delta_time * sensitivity),
    pygame.K_a      : lambda movement, delta_time, sensitivity : movement + (Vector3(1, 0, 0) * delta_time * sensitivity),
    pygame.K_d      : lambda movement, delta_time, sensitivity : movement - (Vector3(1, 0, 0) * delta_time * sensitivity),
    pygame.K_LSHIFT : lambda movement, delta_time, sensitivity : movement * 2.0,
}

PARSE_GUI_INPUTS = {
    "-BATTER-ID-"       : lambda GUI_Value : CHARACTERNAME_TO_ID[GUI_Value],
    "-PITCHER-ID-"      : lambda GUI_Value : CHARACTERNAME_TO_ID[GUI_Value],
    "-BATTER-ISLEFTY-"  : lambda GUI_Value : 1 if GUI_Value else 0,
    #The next 3 check if value is a float before using the float function, then truncates to -2 to 2.
    #The truncating should be made smarter in the future to use real values from the game.
    "-BATTER-X-"        : lambda GUI_Value : 0 if not GUI_Value.replace(".","").replace("-","").isnumeric() else min(max(float(GUI_Value),-2),2),
    "-BALL-X-"          : lambda GUI_Value : 0 if not GUI_Value.replace(".","").replace("-","").isnumeric() else min(max(float(GUI_Value),-2),2),
    "-BALL-Z-"          : lambda GUI_Value : 0 if not GUI_Value.replace(".","").replace("-","").isnumeric() else min(max(float(GUI_Value),-2),2),
    "-CHEM-LINKS-"      : lambda GUI_Value: GUI_Value,
    "-HITTYPE-SLAP-"    : lambda GUI_Value: 0,
    "-HITTYPE-CHARGE-"  : lambda GUI_Value: 1,
    "-PITCHTYPE-CURVE-" : lambda GUI_Value: 0,
    "-PITCHTYPE-CHARGE-": lambda GUI_Value: 1,
    "-PITCHTYPE-PERFECT-" 
                        : lambda GUI_Value: 2,
    "-PITCHTYPE-CHANGEUP-"  
                        : lambda GUI_Value: 3,
    "-CHARGE-UP-"       : lambda GUI_Value: min(max(GUI_Value, 0), 1),
    "-CHARGE-DOWN-"     : lambda GUI_Value: min(max(GUI_Value, 0), 1),
    "-CONTACT-FRAME-"   : lambda GUI_Value: int(GUI_Value),
    "-STICK-UP-"        : lambda GUI_Value: GUI_Value,
    "-STICK-LEFT-"      : lambda GUI_Value: GUI_Value,
    "-STICK-RIGHT-"     : lambda GUI_Value: GUI_Value,
    "-STICK-DOWN-"      : lambda GUI_Value: GUI_Value,
    "-RNG-1-"           : lambda GUI_Value: 0 if not GUI_Value.isnumeric() else min(max(int(GUI_Value),0),32767),
    "-RNG-2-"           : lambda GUI_Value: 0 if not GUI_Value.isnumeric() else min(max(int(GUI_Value),0),32767),
    "-RNG-3-"           : lambda GUI_Value: 0 if not GUI_Value.isnumeric() else min(max(int(GUI_Value),0),32767)
}

GUIName_TO_JSONName = {
    "-BATTER-ID-"           : "batter_id",
    "-PITCHER-ID-"          : "pitcher_id",
    "-BATTER-ISLEFTY-"      : "handedness",
    "-BATTER-X-"            : "batter_x",
    "-BALL-X-"              : "ball_x",
    "-BALL-Z-"              : "ball_z",
    "-CHEM-LINKS-"          : "chem",
    "-HITTYPE-SLAP-"        : "hit_type",
    "-HITTYPE-CHARGE-"      : "hit_type",
    "-PITCHTYPE-CURVE-"     : "pitch_type",
    "-PITCHTYPE-CHARGE-"    : "pitch_type",
    "-PITCHTYPE-PERFECT-"   : "pitch_type",
    "-PITCHTYPE-CHANGEUP-"  : "pitch_type",
    "-CHARGE-UP-"           : "charge_up",
    "-CHARGE-DOWN-"         : "charge_down",
    "-CONTACT-FRAME-"       : "frame",
    "-STICK-UP-"            : "stick_up",
    "-STICK-LEFT-"          : "stick_left",
    "-STICK-RIGHT-"         : "stick_right",
    "-STICK-DOWN-"          : "stick_down",
    "-RNG-1-"               : "rand_1",
    "-RNG-2-"               : "rand_2",
    "-RNG-3-"               : "rand_3"
}

class RenderedBattingScene:
    def __init__(self) -> None:
        self.screen = canvas(render_dimensions)
        self.stadium:MssbStadium = None
        self.stadium_graphics_list = None
        self.camera_sensitivity = 10.0

        self.proj_mat = self.screen.make_projection_horizontal(80.0, render_dimensions[0]/render_dimensions[1], 0.1, 200.0)

        self.view_pos = Vector3(0, 2, -5)
        self.view_rot = Vector3()

        self.frame_counter = 0
        self.start_time = self.old_time = self.get_time()
        self.batting_json = {}

        self.saved_final_spots = None
        self.dt = 0.0
        self.stadium_path = None
        with open(DEFAULT_STADIUM, "r") as f:
            self.set_stadium(read_stadium(json.load(f)))
    
    def set_batting_json(self, d:dict):
        if d != self.batting_json:
            self.batting_json = d

            if self.saved_final_spots != None:
                self.screen.delete_list(self.saved_final_spots)
                self.saved_final_spots = None
    

    def get_time(self):
        return time.perf_counter_ns() * 1e-9

    def get_new_view(self)->mat:
        # m = mat([[]])
        # m.set_size(4, 4)
        # # m.v[3][2] = 5.0
        # return m 
        scale_flip = scale_mat(Vector3(-1.0, 1.0, -1.0))
        scale_render = scale_mat(Vector3(1.0, -1.0, 1.0))

        r_mat = rotation_mat(self.view_rot)
        t_mat = translation_mat(self.view_pos)
        new_view = r_mat * scale_render * t_mat * scale_flip
        return new_view

    def update_variables(self):

        new_time = self.get_time()
        dt = new_time - self.old_time
        self.dt = dt
        self.old_time = new_time
        self.frame_counter = int((new_time - self.start_time) * 60)
        self.screen.update_events()

        # camera movement
        movement = Vector3()

        for key, func in KEYBOARD_CAMERA_CONTROLS.items():
            if self.screen.is_pressed(key):
                movement = func(movement, dt, self.camera_sensitivity)

        # update render position if we moved
        if movement.length() > 0:
            i = self.get_new_view()
            # movement *= -1
            t = translation_mat(movement)
            
            new_mat = t * i
            new_mat:mat

            output_loc = new_mat.inv() * vec3_to_vec4(Vector3(0.0, 0.0, 0.0))

            self.view_pos = output_loc.xyz
            self.view_pos.y *= -1

        # update the rotation matrix if right click is held
        if self.screen.is_right_button_down():
            new_move = self.screen.mouse_move
            self.view_rot = Vector3(self.view_rot.x + new_move.y, self.view_rot.y - new_move.x, self.view_rot.z)

        self.check_update_stadium()
    
    def render(self):
        self.screen.clear((0, 0, 0))

        self.screen.set_matrices(self.get_new_view(), self.proj_mat)

        self.draw_stadium()

        self.draw_ball_path()

        self.draw_bat()

        self.draw_batter()

        self.draw_fps()

        self.screen.present()

    def draw_fps(self):
        try:
            if self.batting_json.get("show_fps", False) == True:
                self.screen.draw_text(text=f"Fps: {int(1/(self.dt))}", p=Vector3(-1,-1,0), direction_vector=Vector3(1,0,0), rendered_height=0.05, text_size=24, on_ui=True)
        except:
            pass

    def draw_batter(self):
        try:
            batter_x = self.batting_json.get("batter_x", 0)
            handedness = self.batting_json.get("handedness", 0)
            batter_id = self.batting_json.get("batter_id", 0)

            hbox_batter = calc_batting.get_hitbox(batter_id)
                
            batter_width = hbox_batter[0] / 100
            batter_hitbox_near =  hbox_batter[1] / 100
            batter_hitbox_far =  hbox_batter[2] / -100

            batter_offset_x = calc_batting.BATTER_HITBOXES[batter_id]["EasyBattingSpotHorizontal"]
            batter_offset_z = calc_batting.BATTER_HITBOXES[batter_id]["EasyBattingSpotVertical"]

            if handedness == 1:
                batter_x *= -1
                batter_offset_x *= -1
                batter_hitbox_near *= -1
                batter_hitbox_far *= -1
            
            height = 2
            slight_offset = 0.001

            for p in [batter_hitbox_near, batter_hitbox_far]:
                self.screen.draw_cube(position=Vector3(batter_x + batter_offset_x, slight_offset, batter_offset_z), scale=Vector3(p, height, batter_width), offset=Vector3(p/2, height/2, batter_width/2), filled=False, color=(0, 255, 255))
            
            self.screen.draw_text(text=calc_batting.get_name(batter_id), p=Vector3(batter_x + batter_offset_x, slight_offset, batter_offset_z - slight_offset), direction_vector=Vector3(1, 0, 0),text_size=24, rendered_height=0.25)

        except:
            pass

    def draw_bat(self):
        try:
            batter_x = self.batting_json.get("batter_x", 0)
            handedness = self.batting_json.get("handedness", 0)
            batter_id = self.batting_json.get("batter_id", 0)

            if handedness == 1:
                batter_x *= -1

            near_far = calc_batting.get_bat_hitbox(batter_id, 0, handedness)
            
            for p in near_far:
                self.screen.draw_cube(position=Vector3(batter_x, 1, 0), scale=Vector3(p, 0.1, 0.1), offset=Vector3((p/2), 0, 0))

        except:
            pass

    def draw_ball_path(self):
        try:
            count = 1 if "override_vertical_range" in self.batting_json else 5

            for i in range(count):
                kwargs = copy.deepcopy(self.batting_json)
                if self.batting_json.get("show_one_hit", False) != True:
                    kwargs.setdefault("override_vertical_range", i) 
                kwargs.setdefault("rand_1", 1565)
                kwargs.setdefault("rand_2", 20008)
                kwargs.setdefault("rand_3", 1628)

                res = calc_batting.hit_ball(**kwargs)["FlightDetails"]["Path"]
                if len(res) > 0:
                    new_points = [
                        dict_to_vec3(x)
                        for x 
                        in res
                    ]
                    self.screen.draw_lines(new_points, line_width=5)
                    final_point = new_points[-1]
                    final_point_display = final_point.copy()
                    render_height = 0.5

                    if kwargs.get("units_feet", False) == True:
                        final_point_display *= 3.28084
                    
                    self.screen.draw_text(text=f"({final_point_display.x:.2f}, {final_point_display.z:.2f})", p=final_point, direction_vector=Vector3(1, 0, 0), text_size=24, rendered_height=render_height)

                    hit_distance = final_point_display.length()
                    text = f"{hit_distance:.2f} m"
                    if kwargs.get("units_feet", False) == True:
                        text = f"{hit_distance:.2f} ft"
                        
                    self.screen.draw_text(text=text, p=final_point + Vector3(0, render_height, 0), direction_vector=Vector3(1, 0, 0), text_size=24, rendered_height=render_height)

                    self.screen.draw_sphere(new_points[self.frame_counter % len(new_points)], radius=0.1, resolution=5)

            if isinstance(self.batting_json["generate_random_hits"], int) and self.batting_json["generate_random_hits"] > 0 and self.saved_final_spots == None:
                self.saved_final_spots = self.screen.start_new_list()
                s = set()
                for i in range(self.batting_json["generate_random_hits"]):
                    kwargs = copy.deepcopy(self.batting_json)
                    kwargs.setdefault("rand_1", randint(0, (2**15)-1))
                    kwargs.setdefault("rand_2", randint(0, (2**15)-1))
                    kwargs.setdefault("rand_3", randint(0, (2**15)-1))

                    all_hit_points = calc_batting.hit_ball(**kwargs)["FlightDetails"]["Path"]
                    all_hit_points = [dict_to_vec3(x) for x in all_hit_points]
                    final_point = all_hit_points[-1]
                    if (*final_point,) not in s:
                        s.add((*final_point,))
                        # self.screen.draw_lines(all_hit_points, line_width=1, color=(255, 255, 255))

                        self.screen.draw_sphere(final_point, radius=0.1, resolution=2)

                self.screen.end_list(self.saved_final_spots)

            if self.saved_final_spots != None:
                self.screen.call_list(self.saved_final_spots)

        except:
            if self.saved_final_spots != None:
                self.screen.delete_list(self.saved_final_spots)
                self.saved_final_spots = None
            pass

    def check_update_stadium(self):
        if self.batting_json != None:
            new_path = self.batting_json.get("stadium_path", None)

            if new_path != None and new_path != self.stadium_path and exists(new_path):
                try:
                    self.stadium_path = new_path
                    with open(new_path, "r") as f:
                        self.set_stadium(read_stadium(json.load(f)))
                except:
                    pass

    def set_stadium(self, stadium:MssbStadium):
        self.stadium = stadium
        self.record_stadium()

    def draw_stadium(self):
        if self.stadium_graphics_list != None:
            self.screen.call_list(self.stadium_graphics_list)

    def record_stadium(self):
        if self.stadium == None:
            return

        if self.stadium_graphics_list != None: 
            self.screen.delete_list(self.stadium_graphics_list)

        self.stadium_graphics_list = self.screen.start_new_list()

        stadium_flip = Vector3(1, -1, 1)

        for vertCollection in self.stadium.vertex_collection:
            for tris in vertCollection.triangle_collection:
                points = [
                    p.point.elementwise() * stadium_flip.elementwise()
                    for p
                    in tris.points
                ]
                
                if tris.collection_type == STADIUM_TRIANGLE_COLLECTION_SINGLES:
                    r = range(0, len(points), 3)
                    triangle_method = self.screen.draw_triangles

                elif tris.collection_type == STADIUM_TRIANGLE_COLLECTION_STRIP:
                    r = range(0, len(points)-2)
                    triangle_method = self.screen.draw_triangle_strip


                for i in r:
                    # get just the vec3s
                    new_points = points[i:i+3]
                    # third point in the triangle defines the collision type
                    color = tri_type_to_color(tris.points[i+2].stadium_type)

                    triangle_method(new_points, filled=True, color=color, draw_normals=False)
                    triangle_method(new_points, filled=False, color=contrast_color(color), draw_normals=False)

        self.screen.end_list(self.stadium_graphics_list)


class ParameterWindow:
    def __init__(self) -> None:
        #originalGUI_column = [
        #    [sg.Multiline("{}", key="-BATTING-JSON-", enable_events=True, expand_y=True, auto_size_text=True)],
        #    [sg.Button("Instructions", key="-INSTRUCTIONS-", enable_events=True), sg.Button("Show Resulting Hit Details", key="-SHOW-HIT-DETAILS-", enable_events=True)]
        #]
        
                #set default inputs
        self.input_params = {
            "batter_id": 0,
            "is_batter_captain": False,
            "pitcher_id": 0,
            "handedness": 0,
            "batter_x": 0,
            "ball_x": 0,
            "ball_z": 0,
            "chem": 0,
            "hit_type": 0,
            "pitch_type": 0,
            "charge_up": 0,
            "charge_down": 0,
            "frame": 6,
            "stick_up": False,
            "stick_down": False,
            "stick_left": False,
            "stick_right": False,
            "rand_1":1565,
            "rand_2":20008,
            "rand_3":1628
        }

        #create GUI and fill default values according to the input_params defaults
        visualizer_param_column = [
            [
                sg.Text("Batter ID"), 
                sg.Combo(values=('Mario', 'Luigi'), default_value=ID_TO_CHARACTERNAME[self.input_params["batter_id"]], key="-BATTER-ID-", enable_events=True),  
                sg.Checkbox('Superstar', default=False), 
                sg.Checkbox('Lefty', default=self.input_params["handedness"], key="-BATTER-ISLEFTY-",enable_events=True)
            ],

            [
                sg.Text("Pitcher ID"), 
                sg.Combo(values=('Mario', 'Luigi'), default_value=ID_TO_CHARACTERNAME[self.input_params["pitcher_id"]], key="-PITCHER-ID-", enable_events=True),  
                sg.Checkbox('Superstar', default=False), 
                sg.Checkbox('Lefty', default=False)
            ],

            [sg.Text("Batter x"), sg.InputText(self.input_params["batter_x"], key="-BATTER-X-", enable_events=True)], 
            [sg.Text("Ball x"), sg.InputText(self.input_params["ball_x"], key="-BALL-X-", enable_events=True)], 
            [sg.Text("Ball z"), sg.InputText(self.input_params["ball_z"], key="-BALL-Z-", enable_events=True)],

            [sg.Text("Chemistry Links on Base"), sg.Combo(values=(0, 1, 2, 3), default_value=self.input_params["chem"], key="-CHEM-LINKS-", enable_events=True)],

            [sg.Text("Swing Type"), 
                sg.Radio('Slap', group_id="swingTypes", default= False if self.input_params["hit_type"] else True, key="-HITTYPE-SLAP-", enable_events=True),  
                sg.Radio('Charge', group_id="swingTypes", default= True if self.input_params["hit_type"] else False, key="-HITTYPE-CHARGE-", enable_events=True), ],

            [sg.Text("Pitch Type"), 
                sg.Radio('Curve', group_id="pitchTypes", key="-PITCHTYPE-CURVE-", default= True if self.input_params["pitch_type"] == 0 else False, enable_events=True), 
                sg.Radio('Charge', group_id="pitchTypes", key="-PITCHTYPE-CHARGE-", default= True if self.input_params["pitch_type"] == 1 else False, enable_events=True), 
                sg.Radio('Perfect', group_id="pitchTypes", key="-PITCHTYPE-PERFECT-", default= True if self.input_params["pitch_type"] == 2 else False, enable_events=True), 
                sg.Radio('ChangeUp', group_id="pitchTypes", key="-PITCHTYPE-CHANGEUP-", default= True if self.input_params["pitch_type"] == 3 else False, enable_events=True), ],

            [sg.Text("Charge Up"), sg.Slider(range=(0,1), default_value=self.input_params["charge_up"], orientation='horizontal', 
                                             resolution=0.01, tick_interval=0.25, key="-CHARGE-UP-", enable_events=True)],
            [sg.Text("Charge Down"), sg.Slider(range=(0,1), default_value=self.input_params["charge_down"], orientation='horizontal', 
                                               resolution=0.01, tick_interval=0.25, key="-CHARGE-DOWN-", enable_events=True)],

            [sg.Text("Contact Frame"), sg.Slider(range=(2,10), default_value=self.input_params["frame"], orientation='horizontal', 
                                                 resolution=1, tick_interval=1, key="-CONTACT-FRAME-", enable_events=True)],

            [
                sg.Text("Stick Input"), 
                sg.Checkbox("↑", default=False, key="-STICK-UP-", enable_events=True), 
                sg.Checkbox("←", default=False, key="-STICK-LEFT-", enable_events=True), 
                sg.Checkbox("→", default=False, key="-STICK-RIGHT-", enable_events=True), 
                sg.Checkbox("↓", default=False, key="-STICK-DOWN-", enable_events=True)
            ],

            [sg.Text("RNG 1"),sg.InputText(self.input_params["rand_1"], key="-RNG-1-", enable_events=True)], 
            [sg.Text("RNG 2"),sg.InputText(self.input_params["rand_2"], key="-RNG-2-", enable_events=True)], 
            [sg.Text("RNG 3"),sg.InputText(self.input_params["rand_3"], key="-RNG-3-", enable_events=True)],

            [sg.Text("Vertical Range Override"),sg.InputText()], #TODO: connect rest of default values with input-params
            [sg.Text("Vertical Angle Override"),sg.InputText()], 
            [sg.Text("Horizontal Angle Override"),sg.InputText()],  
            [sg.Text("Power Override"),sg.InputText()],  

            [sg.Checkbox("Show One Hit", default=False)],  
            [sg.Checkbox("Generate Random Hits", default=False)],   

            [sg.Checkbox("Show FPS", default=False)],  
            [sg.Checkbox("Convert Units to Feet", default=False)], 
             
            [sg.Text("Stadium Path"),sg.InputText()] 
        ]
        
        layout = [
            [sg.Column(visualizer_param_column)]
        ]

        self.window = sg.Window("Render Parameters", layout, resizable=True, enable_close_attempted_event=True)
        self.parsed_input = {}
        self.instructions_text = ""



    def update_values(self):
        new_input = None
        json_updated = False
        
        event, values = self.window.read(timeout=1/1000)
        #for event in self.window.read(timeout=1/1000):
        if event == None or event == "__TIMEOUT__":
            pass
        else:
            event = event
            if event == "-WINDOW CLOSE ATTEMPTED-":
                exit()
            elif event == "-BATTING-JSON-":
                json_updated = True
                try:
                    new_input = json.loads(self.window["-BATTING-JSON-"].get())
                except:
                    new_input = None
            elif event == "-INSTRUCTIONS-":
                layout = [[sg.Text(self.instructions_text, key='TEXT')]]
                sg.Window(f'Instructions', layout, finalize=True)
            elif event == "-SHOW-HIT-DETAILS-":
                try:
                    res_json = calc_batting.hit_ball(**self.parsed_input)
                    if "FlightDetails" in res_json and "Path" in res_json["FlightDetails"]:
                        res_json["FlightDetails"].pop("Path")
                    layout = [[sg.Multiline(json.dumps(res_json, indent=2), key="-BATTING-JSON-", expand_y=True, auto_size_text=True)]]
                    sg.Window(f'Hit Details', layout, finalize=True, resizable=True)
                except Exception as e:
                    pass


            #parse changes to the GUI
            if event == "-WINDOW CLOSE ATTEMPTED-":
                exit()
            else:
                for key, func in PARSE_GUI_INPUTS.items():
                    if event == key:
                        test = GUIName_TO_JSONName[key]
                        self.input_params[GUIName_TO_JSONName[key]] = func(values[event])
                        test = self.input_params[GUIName_TO_JSONName[key]]


            #elif event == "-BATTER-ID-":
             #   self.input_params["batter_id"] = CHARACTERNAME_TO_ID[self.window["-BATTER-ID-"].get()]
            #elif event == "-PITCHER-ID-":
             #   self.input_params["pitcher_id"] = CHARACTERNAME_TO_ID[self.window["-PITCHER-ID-"].get()]
            #elif event == "-BATTER-ISLEFTY-":
                #sets handedness to lefty (1) if checkbox is checked.
             #   self.input_params["handedness"] = 1 if self.window["-BATTER-ISLEFTY-"].get() else 0
            #elif event == "-BATTER-X-":
            #    try:
            #        if abs(float(self.window["-BATTER-X-"].get())) < 2:
            #            self.input_params["batter_x"] = float(self.window["-BATTER-X-"].get())
            #        else:
            #            self.input_params["batter_x"] = 0
            #    except Exception as e:
            #        pass
            # elif event == "-BALL-X-":
            #     try:
            #         if abs(float(self.window["-BALL-X-"].get())) < 2:
            #             self.input_params["ball_x"] = float(self.window["-BALL-X-"].get())
            #         else:
            #             self.input_params["ball_x"] = 0
            #     except Exception as e:
            #         pass
            # elif event == "-BALL-Z-":
            #     try:
            #         if abs(float(self.window["-BALL-Z-"].get())) < 2:
            #             self.input_params["ball_z"] = float(self.window["-BALL-Z-"].get())
            #         else:
            #             self.input_params["ball_z"] = 0
            #     except Exception as e:
            #         pass

        #overriding this to true for while i'm porting over the logic.
        json_updated = True
        if json_updated:
            #self.parsed_input = new_input
            self.parsed_input = self.input_params

        return json_updated

def main():
    renderer = RenderedBattingScene()
    param_window = ParameterWindow()

    with open("instructions.txt", "r") as f:
        param_window.instructions_text = f.read()

    while True:
        json_update = param_window.update_values()
        if json_update:
            renderer.set_batting_json(param_window.parsed_input)
        renderer.update_variables()
        renderer.render()

if __name__ == "__main__":
    main()