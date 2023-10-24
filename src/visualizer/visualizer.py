from __future__ import annotations
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import sys
from utils.vec_mtx import *

cached_fonts = {}
cached_strings = {}

CACHED_STRING_LIMIT = 10000

class canvas:
    def __init__(self, size) -> None:
        pygame.init()
        self.width, self.height = self.size = size
        self.screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)

        glEnable(GL_DEPTH_TEST)

    def update_light(self, sun_position: Vector3):
        glLight(GL_LIGHT0, GL_POSITION, (sun_position.x, -sun_position.y, sun_position.z, 0.0))

        # Ambient lighting
        # glLightfv(GL_LIGHT0, GL_AMBIENT, (255, 255, 255, 1))
        # Diffuse lighting
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0, 0.5, 0.1, 0))

        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1, 1, 1, 0))
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128)
        glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        # glEnable(GL_LIGHTING)
        # glEnable(GL_LIGHT0)
        # glEnable(GL_COLOR_MATERIAL)
        # glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
        pass

    def start_new_list(self):
        l = glGenLists(1)
        glNewList(l, GL_COMPILE)
        return l

    def end_list(self, l):
        glEndList()

    def call_list(self, l):
        glCallList(l)

    def delete_list(self, l):
        glDeleteLists(l, 1)

    def make_projection(self, l, r, b, t, n, f) -> mat:
        m = mat([[]])
        m.set_size(4, 4)

        m.v[0][0] = 2.0 * n / (r - l)
        m.v[0][2] = (r + l) / (r - l)
        m.v[1][1] = 2.0 * n / (t - b)
        m.v[1][2] = (t + b) / (t - b)
        m.v[2][2] = -(f + n) / (f - n)
        m.v[2][3] = -(2.0 * f * n) / (f - n)
        m.v[3][2] = -1.0
        m.v[3][3] = 0.0

        return m

    def make_projection_vertical(self, fov, aspect, front, back):
        fov = math.radians(fov)  # transform fov from degrees to radians

        tangent = math.tan(fov / 2.0)  # tangent of half vertical fov
        height = front * tangent  # half height of near plane
        width = height * aspect  # half width of near plane

        return self.make_projection(-width, width, -height, height, front, back)

    def make_projection_horizontal(self, fov, aspect, front, back):
        fov = math.radians(fov)  # transform fov from degrees to radians
        fov = 2.0 * math.atan(math.tan(fov * 0.5) / aspect)  # transform from horizontal fov to vertical fov

        tangent = math.tan(fov / 2.0)  # tangent of half vertical fov
        height = front * tangent  # half height of near plane
        width = height * aspect  # half width of near plane

        return self.make_projection(-width, width, -height, height, front, back)

    def set_matrices(self, view: mat, proj: mat):
        self.view_matrix = view
        self.projection_matrix = proj

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glMultMatrixf(self.view_matrix.transpose().all_values())
        glScalef(-1.0, -1.0, 1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMultMatrixf(self.projection_matrix.transpose().all_values())

        glMatrixMode(GL_MODELVIEW)

    def update_events(self):
        self.mouse_move = Vector2()
        self.pressed_keys = []

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.pressed_keys.append(event.key)
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_move = Vector2(event.rel).elementwise() / Vector2(self.width, self.width).elementwise()

    def get_new_pressed_keys(self):
        # print(self.pressed_keys)
        return self.pressed_keys

    def is_pressed(self, k) -> bool:
        keys = pygame.key.get_pressed()
        return keys[k]

    def is_left_button_down(self):
        return pygame.mouse.get_pressed(3)[0]

    def is_right_button_down(self):
        return pygame.mouse.get_pressed(3)[2]

    def get_mouse_move(self) -> Vector2:
        return self.mouse_move

    def clear(self, color):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(color[0] / 255, color[1] / 255, color[2] / 255, 1.0)
        # self.screen.fill(color)

    def present(self):
        # glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(1)

    def project_point(self, v: Vector3) -> Vector3:
        p = Vector4(v.x, -v.y, v.z, 1.0)
        p = self.projection_matrix * self.view_matrix * p

        if (p.w == 0.0): return Vector3(0.0, 0.0, -1)
        p = p.xyz / p.w
        p = Vector3((p.x * 0.5 + 0.5) * self.width, (1.0 - (p.y * 0.5 + 0.5)) * self.height, p.z)
        return p

    def draw_sphere(self, p: Vector3, resolution=20, radius=1.0, line_width=2, color=(255, 0, 0), fill=True):
        quad = gluNewQuadric()

        glPushMatrix()
        glPushAttrib(GL_POLYGON_BIT | GL_LINE_BIT)

        glLineWidth(line_width)

        glTranslatef(p.x, p.y, p.z)

        glColor3ub(*color)
        if not fill:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        gluSphere(quad, radius, resolution, resolution // 2)

        glLineWidth(line_width / 2)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor3ub(255 - color[0], 255 - color[1], 255 - color[2])
        gluSphere(quad, radius + 0.001, 8, 8)

        glPopAttrib()
        glPopMatrix()

        gluDeleteQuadric(quad)

        # #draw ring
        # diameter = radius * 2
        # points = []
        # for ii in range(resolution):
        #     a = (ii / resolution) * 2 * math.pi
        #     points.append(p + diameter * Vector3(math.cos(a), 0.0, math.sin(a)))

        # self.draw_lines(points, color, line_width, closed=False)

        # # pygame.draw.lines(self.screen, color, points, width=line_width, closed=False)

        # #draw X
        # points = []
        # for ii in range(resolution):
        #     a = (ii / resolution) * 2 * math.pi
        #     points.append(p + diameter * Vector3(0.0, math.cos(a), math.sin(a)))
        # self.draw_lines(points, color, line_width, closed=False)

        # # pygame.draw.lines(self.screen, color, points=points, width=line_width, closed=False)

        # #draw Z
        # points = []
        # for ii in range(resolution):
        #     a = (ii / resolution) * 2 * math.pi
        #     points.append(p + diameter * Vector3(math.cos(a), -math.sin(a), 0.0))
        # self.draw_lines(points, color, line_width, closed=False)
        # # pygame.draw.lines(self.screen, color, points=points, width=line_width, closed=False)

    def draw_hemisphere(self, p: Vector3, resolution=20, radius=1.0, line_width=2, color=(255, 0, 0)):

        # draw ring
        diameter = radius * 2
        points = []
        for ii in range(resolution):
            a = (ii / resolution) * 2 * math.pi
            points.append(self.project_point(p + diameter * Vector3(math.cos(a), 0.0, math.sin(a))).xy)
        self.draw_lines(points, color, line_width)
        # pygame.draw.lines(self.screen, color, points, width=line_width, closed=False)

        # draw X
        points = []
        for ii in range(resolution):
            a = (ii / (resolution - 1)) * math.pi - math.pi * 1 / 2
            points.append(self.project_point(p + diameter * Vector3(0.0, math.cos(a), math.sin(a))).xy)
        self.draw_lines(points, color, line_width)
        # pygame.draw.lines(self.screen, color, points=points, width=line_width, closed=False)

        # draw Z
        points = []
        for ii in range(resolution):
            a = (ii / (resolution - 1)) * math.pi + math.pi
            points.append(self.project_point(p + diameter * Vector3(math.cos(a), -math.sin(a), 0.0)).xy)
        self.draw_lines(points, color, line_width)
        # pygame.draw.lines(self.screen, color, points=points, width=line_width, closed=False)

    def draw_text(self, text: str, p: Vector3, direction_vector: Vector3, color=(0, 0, 0), text_size=10,
                  rendered_height=2, on_ui=False):
        global cached_fonts, cached_strings
        
        if text_size not in cached_fonts:
            font = pygame.font.SysFont("Arial", text_size)
            cached_fonts[text_size] = font
        else:
            font = cached_fonts[text_size]

        # if we've got too many textures, free them all
        if len(cached_strings) > CACHED_STRING_LIMIT:
            glDeleteTextures([generated_texture for (_, __), generated_texture in cached_strings.values()])
            cached_strings.clear()

        if on_ui:
            glMatrixMode(GL_MODELVIEW)
            glPushMatrix()
            glLoadIdentity()
            # glMultMatrixf(self.view_matrix.transpose().all_values())
            # glScalef(-1.0,-1.0,1.0)

            glMatrixMode(GL_PROJECTION)
            glPushMatrix()
            glLoadIdentity()
            # glMultMatrixf(self.projection_matrix.transpose().all_values())

            glMatrixMode(GL_MODELVIEW)
        cached_string_tuple = (text, text_size)
        if cached_string_tuple not in cached_strings:
            rendered_string = font.render(text, False, color)
            rendered_string: pygame.surface.Surface

            this_generated_texture = glGenTextures(1)
            rgb_surface = pygame.image.tostring(rendered_string, 'RGBA')
            glBindTexture(GL_TEXTURE_2D, this_generated_texture)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
            surface_rect = rendered_string.get_rect()
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, surface_rect.width, surface_rect.height, 0, GL_RGBA,
                         GL_UNSIGNED_BYTE, rgb_surface)
            glGenerateMipmap(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, 0)
            texture_width, texture_height = (surface_rect.width, surface_rect.height)
            cached_strings[cached_string_tuple] = ((texture_width, texture_height), this_generated_texture)
        else:
            (texture_width, texture_height), this_generated_texture = cached_strings[cached_string_tuple]

        my_height = rendered_height
        my_width = (texture_width / texture_height) * rendered_height

        my_direction = direction_vector.normalize()
        up_vector = Vector3(0, 1, 0)
        right = up_vector.cross(my_direction).normalize()
        tilted_top = my_direction.cross(right).normalize()

        tilted_offset = tilted_top * my_height

        bl_corner = p
        tl_corner = bl_corner + tilted_offset

        br_corner = bl_corner + (my_direction * my_width)
        tr_corner = br_corner + tilted_offset

        glPushMatrix()

        glBindTexture(GL_TEXTURE_2D, this_generated_texture)
        glEnable(GL_TEXTURE_2D)
        glBegin(GL_QUADS)

        glColor4f(1.0, 1.0, 1.0, 0.0)
        glTexCoord2f(0, 1);
        glVertex3f(*bl_corner)
        glTexCoord2f(0, 0);
        glVertex3f(*tl_corner)
        glTexCoord2f(1, 0);
        glVertex3f(*tr_corner)
        glTexCoord2f(1, 1);
        glVertex3f(*br_corner)

        glEnd()
        glDisable(GL_TEXTURE_2D)

        glPopMatrix()

        if on_ui:
            glMatrixMode(GL_PROJECTION)
            glPopMatrix()

            glMatrixMode(GL_MODELVIEW)
            glPopMatrix()

    def draw_cylinder(self, p: Vector3, color=(255, 0, 0), resolution=20, radius=0.5, height=1.0, line_width=2,
                      fill=False):

        diameter = radius * 2

        # draw ring
        # if self.is_outside(self.project_point(p)):
        #     return
        bottom_ring = []
        for ii in range(resolution):
            a = (ii / resolution) * 2 * math.pi
            new_p = p + diameter * Vector3(math.cos(a), 0.0, math.sin(a))
            bottom_ring.append(new_p)

        top_ring = [Vector3(a.x, a.y + height, a.z) for a in bottom_ring]

        if not fill:
            self.draw_lines(bottom_ring, color, line_width, closed=True, filled=False)
            # pygame.draw.polygon(self.screen, color, bottom_ring, width=line_width)
            self.draw_lines(top_ring, color, line_width, closed=True, filled=False)
            # pygame.draw.polygon(self.screen, color, top_ring, width=line_width)

            # draw lines connecting top ring to bottom ring
            self.draw_lines(points=[bottom_ring[int(resolution * 0 / 4)], top_ring[int(resolution * 0 / 4)]],
                            color=color, line_width=line_width)
            self.draw_lines(points=[bottom_ring[int(resolution * 1 / 4)], top_ring[int(resolution * 1 / 4)]],
                            color=color, line_width=line_width)
            self.draw_lines(points=[bottom_ring[int(resolution * 2 / 4)], top_ring[int(resolution * 2 / 4)]],
                            color=color, line_width=line_width)
            self.draw_lines(points=[bottom_ring[int(resolution * 3 / 4)], top_ring[int(resolution * 3 / 4)]],
                            color=color, line_width=line_width)

            # pygame.draw.line(self.screen, color, bottom_ring[int(resolution * 0/4)], top_ring[int(resolution * 0/4)], width=line_width)
            # pygame.draw.line(self.screen, color, bottom_ring[int(resolution * 1/4)], top_ring[int(resolution * 1/4)], width=line_width)
            # pygame.draw.line(self.screen, color, bottom_ring[int(resolution * 2/4)], top_ring[int(resolution * 2/4)], width=line_width)
            # pygame.draw.line(self.screen, color, bottom_ring[int(resolution * 3/4)], top_ring[int(resolution * 3/4)], width=line_width)
        else:
            self.draw_lines(top_ring, color, line_width, closed=True, filled=True)
            self.draw_lines(bottom_ring, color, line_width, closed=True, filled=True)

            outside_skin = []
            for i in range(len(top_ring)):
                outside_skin.append(top_ring[i])
                outside_skin.append(bottom_ring[i])
            outside_skin.append(outside_skin[0])
            outside_skin.append(outside_skin[1])

            self.draw_triangle_strip(outside_skin, color, line_width, filled=True)

    def draw_wedge(self, p: Vector3, inner_radius, outer_radius, upper_angle, lower_angle, mAboveGround=0, line_width=0,
                   resolution=20, color=(255, 0, 0), filled=False):
        points = []
        # inner arc
        for ii in range(resolution):
            a = (ii / resolution) * (upper_angle - lower_angle) + lower_angle
            points.append(p + inner_radius * Vector3(math.cos(a), mAboveGround, math.sin(a)))
        # outer arc
        for ii in range(resolution):
            a = ((resolution - ii - 1) / resolution) * (upper_angle - lower_angle) + lower_angle
            points.append(p + outer_radius * Vector3(math.cos(a), mAboveGround, math.sin(a)))
        # connect back to start
        points.append(p + inner_radius * Vector3(math.cos(lower_angle), mAboveGround, math.sin(lower_angle)))

        self.draw_lines(points=points, color=color, line_width=line_width, closed=True, filled=filled)

        # pygame.draw.polygon(self.screen, color, points=points,width=line_width)

    def is_outside(self, p: Vector3):
        return p.z >= 0 or p.x < 0 or p.x > self.width or p.y < 0 or p.y > self.height

    Vector3s = list[Vector3]

    def draw_lines(self, points: Vector3s, color=(255, 0, 0), line_width=2, closed=False, filled=False):
        if len(points) == 0:
            return
        glColor3ub(*color)
        # center = Vector3(0.0,0.0,0.0)
        # for p in points:
        #     center += p
        # center = center / len(points)

        # projected_center = self.project_point(center)
        # if self.is_outside(projected_center):
        #     return

        # new_p = [self.project_point(p).xy for p in points]
        # pygame.draw.lines(self.screen, color=color, points=new_p, width=line_width, closed=closed)
        glLineWidth(float(line_width))

        # if closed:
        #     glBegin(GL_POLYGON)
        # else:
        #     glBegin(GL_LINES)
        if filled:
            glBegin(GL_POLYGON)
        else:
            glBegin(GL_LINE_STRIP)

        for p in points:
            glVertex3f(*p)

        if closed and not filled and len(points) >= 1:
            p = points[0]
            glVertex3f(*p)

        glEnd()

    def draw_triangles(self, points: Vector3s, color=(255, 0, 0), line_width=2, filled=False, draw_normals=True):
        if len(points) == 0:
            return

        glColor3ub(*color)
        glPushAttrib(GL_POLYGON_BIT | GL_COLOR_BUFFER_BIT | GL_LIGHTING_BIT)
        glLineWidth(float(line_width))

        if not filled:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        # glEnable(GL_LIGHTING)
        # glEnable(GL_LIGHT0)
        # glEnable(GL_COLOR_MATERIAL)
        # glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

        glBegin(GL_TRIANGLES)
        normals = []
        for i in range(0, len(points), 3):
            n = self.calculate_normal(points[i:i + 3])
            center = (points[i + 0] + points[i + 1] + points[i + 2]) / 3
            normals.append((center - n, center + n))
            glNormal3f(*n)

            glVertex3f(*points[i + 0])
            glVertex3f(*points[i + 1])
            glVertex3f(*points[i + 2])

        glEnd()

        glPopAttrib()
        if draw_normals:
            for p1, p2 in normals:
                self.draw_lines([p1, p2], (255, 255, 255))

    def calculate_normal(self, points: list[Vector3]):
        a = points[0]
        b = points[1]
        c = points[2]

        norm = (b - a).cross(c - a)
        if norm.length() > 0:
            norm = norm.normalize()

        return norm

    def draw_triangle_strip(self, points: Vector3s, color=(255, 0, 0), line_width=2, filled=False, draw_normals=True):
        if len(points) == 0:
            return

        glPushAttrib(GL_POLYGON_BIT | GL_COLOR_BUFFER_BIT | GL_LIGHTING_BIT)
        glColor3ub(*color)
        glLineWidth(float(line_width))

        if not filled:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        # glEnable(GL_LIGHTING)
        # glEnable(GL_LIGHT0)
        # glEnable(GL_COLOR_MATERIAL)
        # glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

        glBegin(GL_TRIANGLE_STRIP)

        spare_points = points[-2:]
        normals = []
        for i in range(len(points) - 2):
            p = points[i]

            normal = self.calculate_normal(points[i:i + 3])
            center = (points[i + 0] + points[i + 1] + points[i + 2]) / 3
            normals.append((center - normal, center + normal))

            glNormal3f(*normal)
            glVertex3f(*p)
        for p in spare_points:
            glVertex3f(*p)

        glEnd()

        glPopAttrib()

        if draw_normals:
            for p1, p2 in normals:
                self.draw_lines([p1, p2], (255, 255, 255))

    def draw_point(self, point: Vector3, color=(255, 0, 0), radius=2, line_width=2):

        glPointSize(float(radius))
        glBegin(GL_POINTS)
        glColor3ub(*color)
        glVertex3f(*point)
        glEnd()

    def draw_cube(self, position: Vector3, scale: Vector3 = Vector3(1.0, 1.0, 1.0),
                  rotation: Vector3 = Vector3(0.0, 0.0, 0.0), offset: Vector3 = Vector3(0.0, 0.0, 0.0),
                  color=(255, 0, 0), line_width=2, filled=True):
        points = [
            Vector3(-0.5, -0.5, -0.5),
            Vector3(-0.5, -0.5, 0.5),
            Vector3(0.5, -0.5, 0.5),
            Vector3(0.5, -0.5, -0.5),

            Vector3(0.5, 0.5, -0.5),
            Vector3(-0.5, 0.5, -0.5),
            Vector3(-0.5, 0.5, 0.5),
            Vector3(0.5, 0.5, 0.5),
        ]

        r = rotation_mat(rotation)

        for i, p in enumerate(points):
            p = p.elementwise() * scale.elementwise()
            p = (r * vec3_to_vec4(p)).xyz
            p = p + position + offset
            points[i] = p

            # draw_points = points + [points[4], points[7], points[2], points[1], points[6], points[5], points[0]]
        bottom = points[0:4]
        top = points[4:8]
        left = [points[0], points[1], points[6], points[5]]
        right = [points[2], points[3], points[4], points[7]]
        front = [points[1], points[2], points[7], points[6]]
        back = [points[0], points[3], points[4], points[5]]

        light_mult = 255
        light_color = [min(255, int(x + light_mult)) for x in color]
        for this_color, outline in [(light_color, False), (color, True)]:
            if outline or filled:
                self.draw_lines(bottom, color=this_color, line_width=line_width, closed=True, filled=outline and filled)
                self.draw_lines(top, color=this_color, line_width=line_width, closed=True, filled=outline and filled)
                self.draw_lines(left, color=this_color, line_width=line_width, closed=True, filled=outline and filled)
                self.draw_lines(right, color=this_color, line_width=line_width, closed=True, filled=outline and filled)
                self.draw_lines(front, color=this_color, line_width=line_width, closed=True, filled=outline and filled)
                self.draw_lines(back, color=this_color, line_width=line_width, closed=True, filled=outline and filled)
