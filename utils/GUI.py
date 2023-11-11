from data.constants import *
import PySimpleGUI as sg
from src.calc import calc_batting
import time, json, copy

DEFAULT_STADIUM = "data/Stadiums/Mario Stadium.json"

fieldersShown = set()
fielder_charID = [0] * 9

posName = ['P','C','1B','2B','3B','SS','LF','CF','RF']

FIELDER_SHOWN_EVENT_TO_POSNUMBER = {
    "-FIELDER-SHOW-P-": 0,
    "-FIELDER-SHOW-C-": 1,
    "-FIELDER-SHOW-1B-": 2,
    "-FIELDER-SHOW-2B-": 3,
    "-FIELDER-SHOW-3B-": 4,
    "-FIELDER-SHOW-SS-": 5,
    "-FIELDER-SHOW-LF-": 6,
    "-FIELDER-SHOW-CF-": 7,
    "-FIELDER-SHOW-RF-": 8
}

FIELDER_ID_EVENT_TO_POSNUMBER = {
    "-FIELDER-CHARID-P-": 0,
    "-FIELDER-CHARID-C-": 1,
    "-FIELDER-CHARID-1B-": 2,
    "-FIELDER-CHARID-2B-": 3,
    "-FIELDER-CHARID-3B-": 4,
    "-FIELDER-CHARID-SS-": 5,
    "-FIELDER-CHARID-LF-": 6,
    "-FIELDER-CHARID-CF-": 7,
    "-FIELDER-CHARID-RF-": 8
}

def can_convert(val, type):
    try:
        type(val)
    except:
        return False
    return True

def clamp(_min, val, _max):
    return max(_min, min(val, _max))

PARSE_GUI_INPUTS = {
    "-BATTER-ID-"       : lambda GUI_Value : CHARACTERNAME_TO_ID[GUI_Value],
    "-PITCHER-ID-"      : lambda GUI_Value : CHARACTERNAME_TO_ID[GUI_Value],
    "-BATTER-ISLEFTY-"  : lambda GUI_Value : 1 if GUI_Value else 0,
    #The next 3 check if value is a float before using the float function, then truncates to -2 to 2.
    #The truncating should be made smarter in the future to use real values from the game.
    "-BATTER-X-"        : lambda GUI_Value : 0 if not can_convert(GUI_Value, float) else clamp(-2, float(GUI_Value), 2),
    "-BALL-X-"          : lambda GUI_Value : 0 if not can_convert(GUI_Value, float) else clamp(-2, float(GUI_Value), 2),
    "-BALL-Z-"          : lambda GUI_Value : 0 if not can_convert(GUI_Value, float) else clamp(-2, float(GUI_Value), 2),
    "-HITTYPE-SLAP-"    : lambda GUI_Value: 0,
    "-HITTYPE-CHARGE-"  : lambda GUI_Value: 1,
    "-PITCHTYPE-CURVE-" : lambda GUI_Value: 0,
    "-PITCHTYPE-CHARGE-": lambda GUI_Value: 1,
    "-PITCHTYPE-PERFECT-": lambda GUI_Value: 2,
    "-PITCHTYPE-CHANGEUP-": lambda GUI_Value: 3,
    "-CHARGE-UP-"       : lambda GUI_Value: clamp(0, GUI_Value, 1),
    "-CHARGE-DOWN-"     : lambda GUI_Value: clamp(0, GUI_Value, 1),
    "-CONTACT-FRAME-"   : lambda GUI_Value: int(GUI_Value),
    "-RNG-1-"           : lambda GUI_Value: 0 if not can_convert(GUI_Value, int) else clamp(0, int(GUI_Value), 32767),
    "-RNG-2-"           : lambda GUI_Value: 0 if not can_convert(GUI_Value, int) else clamp(0, int(GUI_Value), 32767),
    "-RNG-3-"           : lambda GUI_Value: 0 if not can_convert(GUI_Value, int) else clamp(0, int(GUI_Value), 32767),
    "-SHOWN-FIELDER-"   : lambda GUI_Value: CHARACTERNAME_TO_ID[GUI_Value],
    "-DIVE-POP-"        : lambda GUI_Value: "popfly",
    "-DIVE-LINE-"       : lambda GUI_Value: "linedrive",
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
    "-RNG-3-"               : "rand_3",
    "-OVERRIDE-VERTICAL-RANGE-": "override_vertical_range",
    "-OVERRIDE-VERTICAL-ANGLE-": "override_vertical_angle",
    "-OVERRIDE-HORIZONTAL-ANGLE-": "override_horizontal_angle",
    "-OVERRIDE-POWER-"      : "override_power",
    "-SHOW-ONE-HIT-"        : "show_one_hit",
    "-GEN-RAND-HITS-"       : "generate_random_hits",
    "-SHOW-FPS-"            : "show_fps",
    "-SHOW-MAX-HEIGHT-"     : "show_max_height",
    "-SHOW-CURVE-ON-GROUND-": "show_curve_on_ground",
    "-UNITS-FEET-"          : "units_feet",
    "-STADIUM-"             : "stadium_path",
    "-SHOWN-FIELDER-"       : "fielder_id",
    "-DIVE-POP-"            : "dive_type",
    "-DIVE-LINE-"           : "dive_type",
    "-BALL-HANGTIME-"       : "hangtime"
}

#set default inputs
input_params = {
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
    #commented out since we want these elements to be missing from the list as a default
    #"rand_1":1565,
    #"rand_2":20008,
    #"rand_3":1628,
    #"override_vertical_range": -1
    #"override_vertical_range": -1
    #"override_horizontal_range": -1
    #"override_power": -1
    "show_fps": False,
    "units_feet": False,
    "show_curve_on_ground" : False,
    "show_max_height" : False,
    "stadium_path": "Stadiums/Mario Stadium.json"
}


class ParameterWindow:
    def __init__(self) -> None:      


        #create GUI and fill default values according to the input_params defaults
        visualizer_param_column = [
            [
                sg.Button("Instructions", key="-INSTRUCTIONS-", enable_events=True), 
                sg.Button("Show Resulting Hit Details", key="-SHOW-HIT-DETAILS-", enable_events=True)
            ],
            [
                sg.Text("Batter ID"), 
                sg.Combo(values=list(CHARACTERNAME_TO_ID.keys()), default_value=ID_TO_CHARACTERNAME[input_params["batter_id"]], key="-BATTER-ID-", enable_events=True),  
                sg.Checkbox('Superstar', default=False), 
                sg.Checkbox('Lefty', default=input_params["handedness"], key="-BATTER-ISLEFTY-",enable_events=True)
            ],

            [
                sg.Text("Pitcher ID"), 
                sg.Combo(values=list(CHARACTERNAME_TO_ID.keys()), default_value=ID_TO_CHARACTERNAME[input_params["pitcher_id"]], key="-PITCHER-ID-", enable_events=True),  
                sg.Checkbox('Superstar', default=False), 
                sg.Checkbox('Lefty', default=False)
            ],

            [sg.Text("Batter x"), sg.InputText(input_params["batter_x"], key="-BATTER-X-", enable_events=True)], 
            [sg.Text("Ball x"), sg.InputText(input_params["ball_x"], key="-BALL-X-", enable_events=True)], 
            [sg.Text("Ball z"), sg.InputText(input_params["ball_z"], key="-BALL-Z-", enable_events=True)],

            [sg.Text("Chemistry Links on Base"), sg.Combo(values=(0, 1, 2, 3), default_value=input_params["chem"], key="-CHEM-LINKS-", enable_events=True)],

            [sg.Text("Swing Type"), 
                sg.Radio('Slap', group_id="swingTypes", default= False if input_params["hit_type"] else True, key="-HITTYPE-SLAP-", enable_events=True),  
                sg.Radio('Charge', group_id="swingTypes", default= True if input_params["hit_type"] else False, key="-HITTYPE-CHARGE-", enable_events=True), ],

            [sg.Text("Pitch Type"), 
                sg.Radio('Curve', group_id="pitchTypes", key="-PITCHTYPE-CURVE-", default= True if input_params["pitch_type"] == 0 else False, enable_events=True), 
                sg.Radio('Charge', group_id="pitchTypes", key="-PITCHTYPE-CHARGE-", default= True if input_params["pitch_type"] == 1 else False, enable_events=True), 
                sg.Radio('Perfect', group_id="pitchTypes", key="-PITCHTYPE-PERFECT-", default= True if input_params["pitch_type"] == 2 else False, enable_events=True), 
                sg.Radio('ChangeUp', group_id="pitchTypes", key="-PITCHTYPE-CHANGEUP-", default= True if input_params["pitch_type"] == 3 else False, enable_events=True), ],

            [sg.Text("Charge Up"), sg.Slider(range=(0,1), default_value=input_params["charge_up"], orientation='horizontal', 
                                             resolution=0.01, tick_interval=0.25, key="-CHARGE-UP-", enable_events=True)],
            [sg.Text("Charge Down"), sg.Slider(range=(0,1), default_value=input_params["charge_down"], orientation='horizontal', 
                                               resolution=0.01, tick_interval=0.25, key="-CHARGE-DOWN-", enable_events=True)],

            [sg.Text("Contact Frame"), sg.Slider(range=(2,10), default_value=input_params["frame"], orientation='horizontal', 
                                                 resolution=1, tick_interval=1, key="-CONTACT-FRAME-", enable_events=True)],
            [
                sg.Text("Stick Input"), 
                sg.Checkbox("↑", default=input_params["stick_up"], key="-STICK-UP-", enable_events=True), 
                sg.Checkbox("←", default=input_params["stick_left"], key="-STICK-LEFT-", enable_events=True), 
                sg.Checkbox("→", default=input_params["stick_right"], key="-STICK-RIGHT-", enable_events=True), 
                sg.Checkbox("↓", default=input_params["stick_down"], key="-STICK-DOWN-", enable_events=True)
            ],

            [sg.Text("RNG 1"),sg.InputText(key="-RNG-1-", enable_events=True)], 
            [sg.Text("RNG 2"),sg.InputText(key="-RNG-2-", enable_events=True)], 
            [sg.Text("RNG 3"),sg.InputText(key="-RNG-3-", enable_events=True)],

            [sg.Text("Vertical Range Override"),sg.InputText(key="-OVERRIDE-VERTICAL-RANGE-", enable_events=True)], #TODO: connect rest of default values with input-params
            [sg.Text("Vertical Angle Override"),sg.InputText(key="-OVERRIDE-VERTICAL-ANGLE-", enable_events=True)], 
            [sg.Text("Horizontal Angle Override"),sg.InputText(key="-OVERRIDE-HORIZONTAL-ANGLE-", enable_events=True)],  
            [sg.Text("Power Override"),sg.InputText(key="-OVERRIDE-POWER-", enable_events=True)],  

        ]

        instructions_fielder_column = [
            [sg.Text("Hit Visualizer", font=('Arial Bold', 20), justification='center')],
            [sg.Text("Enter hit inputs on the right.\nBelow are some options for the simulation")],

            [sg.Checkbox("Show One Hit", default=False, key="-SHOW-ONE-HIT-", enable_events=True),
             sg.Checkbox("Show FPS", default=input_params["show_fps"], key="-SHOW-FPS-", enable_events=True),
             sg.Checkbox("Convert Units to Feet", default=input_params["units_feet"], key="-UNITS-FEET-", enable_events=True)],

            [sg.Checkbox("Show Max Height", default=input_params["show_max_height"], key="-SHOW-MAX-HEIGHT-", enable_events=True),
             sg.Checkbox("Show Curve Along Ground", default=input_params["show_curve_on_ground"], key="-SHOW-CURVE-ON-GROUND-", enable_events=True)],

            [sg.Text("Generate n Random Hits"),sg.InputText(key="-GEN-RAND-HITS-", enable_events=True)], 
            [sg.Text("Stadium Path"),sg.Combo(values=("data/Stadiums/Mario Stadium.json", 
                                                      "data/Stadiums/Peach's Castle.json", 
                                                      "data/Stadiums/Wario Palace.json", 
                                                      "data/Stadiums/Yoshi Park.json", 
                                                      "data/Stadiums/Donkey Kong Jungle.json", 
                                                      "data/Stadiums/Bowser Castle.json", 
                                                      "data/Stadiums/Toy Field.json"), 
                                               default_value=DEFAULT_STADIUM,
                                               key="-STADIUM-",
                                               enable_events=True)],

            [sg.HorizontalSeparator()],

            [sg.Text("Fielder Catch Range", font=('Arial Bold', 15), justification='center')],
            [sg.Text("Control's the display of each fielder's maximum range.\nThe range is based on the entered hangtime of the hit \n(not connected to the actual simulated hit yet).")],
            [sg.Text("Hit hangtime for dive ranges (in frames)")], 
            [sg.Slider(range=(0,360), default_value=100, orientation='horizontal', 
                       resolution=1, tick_interval=60, key="-BALL-HANGTIME-", enable_events=True)],
            #[sg.InputText(key="-BALL-HANGTIME-", enable_events=True)],
            [
                sg.Text("Dive Type"),
                sg.Radio("Pop Fly", group_id="group_dive_type", key="-DIVE-POP-", default=True, enable_events=True),
                sg.Radio("Line Drive (IF Only)", group_id="group_dive_type", key="-DIVE-LINE-", default=False, enable_events=True),
            ],
        ]
        for pos in posName:
            instructions_fielder_column.append([sg.Checkbox(pos, default=False, enable_events=True, key=f'-FIELDER-SHOW-{pos}-'),
                                   sg.Combo(values=list(CHARACTERNAME_TO_ID.keys()), default_value="Mario", key= f"-FIELDER-CHARID-{pos}-", enable_events=True)])

        layout = [
            [sg.Column(instructions_fielder_column),
             sg.VSeperator(),
             sg.Column(visualizer_param_column)]
        ]

        self.window = sg.Window("Render Parameters", layout, resizable=True, enable_close_attempted_event=True)
        self.parsed_input = {}
        self.instructions_text = ""



    def update_values(self):
        new_input = None
        json_updated = False
        
        event, values = self.window.read(timeout=1/1000)
        if event == None or event == "__TIMEOUT__":
            pass
        elif event == "-WINDOW CLOSE ATTEMPTED-":
            exit()

        #When the buttons are pressed
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

        #for events that need to be removed from the json when they are blank or invalid
        elif event in ("-OVERRIDE-VERTICAL-RANGE-", "-OVERRIDE-VERTICAL-ANGLE-", "-OVERRIDE-HORIZONTAL-ANGLE-", "-OVERRIDE-POWER-", 
                        "-GEN-RAND-HITS-", "-RNG-1-", "-RNG-2-", "-RNG-3-"):
            if values[event].isdigit():
                input_params[GUIName_TO_JSONName[event]] = int(values[event])
                #self.saved_final_spots = None if event == "-GEN-RAND-HITS-" else self.saved_final_spots
            else:
                try: 
                    del input_params[GUIName_TO_JSONName[event]]
                except:
                    pass
            json_updated = True
        #show fielder ranges
        elif event.startswith("-FIELDER-SHOW-"):
            if values[event]:
                fieldersShown.add(FIELDER_SHOWN_EVENT_TO_POSNUMBER[event])
            else:
                fieldersShown.discard(FIELDER_SHOWN_EVENT_TO_POSNUMBER[event])
        elif event.startswith("-FIELDER-CHARID-"):
            fielder_charID[FIELDER_ID_EVENT_TO_POSNUMBER[event]] = CHARACTERNAME_TO_ID[values[event]]
        #for any other event, there is a lambda function dictionary 
        else:
            json_param_value = values[event]

            param_conversion_method = PARSE_GUI_INPUTS.get(event, None)
            if param_conversion_method != None:
                json_param_value = param_conversion_method(json_param_value)

            input_params[GUIName_TO_JSONName[event]] = json_param_value

            json_updated = True

        if json_updated:
            self.parsed_input = copy.deepcopy(input_params)

        return json_updated
