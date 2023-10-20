from __future__ import annotations
from pygame import Vector3, Vector2
import numpy
import math
from numpy.linalg import inv as matrix_inverse


class Vector4:
    def __init__(self, x=0, y=0, z=0, w=1) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __getitem__(self, i):
        return [self.x, self.y, self.z, self.w][i]

    def normalize(self):
        if self.w == 0:
            self.x = float('inf')
            self.y = float('inf')
            self.z = float('inf')
            self.w = float('inf')
            return
        self.x = self.x / self.w
        self.y = self.y / self.w
        self.z = self.z / self.w
        self.w = self.w / self.w

    def __sub__(self, __o) -> Vector4:
        assert (isinstance(__o, Vector4))
        return Vector4(self.x - __o.x, self.y - __o.y, self.z - __o.z, self.w - __o.w)

    @property
    def xyz(self) -> Vector3:
        return Vector3(self.x, self.y, self.z)


def convert_list_to_vector(v):
    if len(v) == 2:
        return Vector2(*v)
    if len(v) == 3:
        return Vector3(*v)
    if len(v) == 4:
        return Vector4(*v)


class mat:
    def __init__(self, values: list) -> None:
        self.v = values

    def rows(self):
        return len(self.v)

    def columns(self):
        return len(self.v[0])

    def __str__(self) -> str:
        rows = self.rows()
        columns = self.columns()
        return "\n".join([" ".join([f"{self.v[a][b]:.2f}" for b in range(columns)]) for a in range(rows)])

    def transpose(self):
        a = numpy.transpose(self.v)
        return mat([[y for y in x] for x in a])

    def __mul__(self, other):
        if isinstance(other, mat):
            assert self.columns() == other.rows()

            v = [[0 for _ in range(self.rows())] for _ in range(other.columns())]

            for r in range(self.rows()):
                for c in range(other.columns()):
                    for k in range(other.rows()):
                        v[r][c] += self.v[r][k] * other.v[k][c]

            return mat(v)

        if isinstance(other, Vector3):
            assert (self.columns() == 3)
            output = [0 for _ in range(self.rows())]
            for r in range(self.rows()):
                for c in range(self.columns()):
                    output[r] += self.v[r][c] * other[c]
            return convert_list_to_vector(output)

        if isinstance(other, Vector4):
            assert (self.columns() == 4)
            output = [0 for _ in range(self.rows())]
            for r in range(self.rows()):
                for c in range(self.columns()):
                    output[r] += self.v[r][c] * other[c]
            return convert_list_to_vector(output)

        assert False

    def inv(self):
        a = matrix_inverse(self.v)
        return mat([[y for y in x] for x in a])

    def set_size(self, rows, columns):
        while self.rows() > rows:
            self.v.pop(-1)
        while self.rows() < rows:
            new_row = self.rows()
            self.v.append([1.0 if i == new_row else 0.0 for i in range(self.columns())])

        while self.columns() > columns:
            for i in range(self.rows()):
                self.v[i].pop(-1)
        while self.columns() < columns:
            new_columns = self.columns()
            for i in range(self.rows()):
                self.v[i].append(1.0 if i == new_columns else 0.0)

    def all_values(self):
        return [j for i in self.v for j in i]


def translation_mat(v: Vector3) -> mat:
    return mat([
        [1.0, 0.0, 0.0, v.x],
        [0.0, 1.0, 0.0, v.y],
        [0.0, 0.0, 1.0, v.z],
        [0.0, 0.0, 0.0, 1.0],
    ])


def vec3_to_vec4(v: Vector3):
    return Vector4(v.x, v.y, v.z, 1.0)


def scale_mat(v: Vector3) -> mat:
    return mat([
        [v.x, 0.0, 0.0, 0.0],
        [0.0, v.y, 0.0, 0.0],
        [0.0, 0.0, v.z, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])


def rotation_mat(v: Vector3) -> mat:
    c_x = math.cos(v.x)
    c_y = math.cos(v.y)
    c_z = math.cos(v.z)

    s_x = math.sin(v.x)
    s_y = math.sin(v.y)
    s_z = math.sin(v.z)

    rotate_x = mat([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, c_x, -s_x, 0.0],
        [0.0, s_x, c_x, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])

    rotate_y = mat([
        [c_y, 0.0, -s_y, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [s_y, 0.0, c_y, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])

    rotate_z = mat([
        [c_z, -s_z, 0.0, 0.0],
        [s_z, c_z, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])

    return rotate_x * rotate_y * rotate_z
