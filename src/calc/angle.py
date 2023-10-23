import math


def AdjustBallAngle(ballAngle):
    if (ballAngle < 0):
        while ballAngle < 0:
            ballAngle += 0x1000
    if (0xfff < ballAngle):
        while 0xfff < ballAngle:
            ballAngle += -0x1000
    return ballAngle

def mssbConvertToRadians(param_1):
    if (param_1 < 0):
        param_1 += 0x1000

    if (0xfff < param_1):
        param_1 += -0x1000

    dVar1 = (math.pi * (param_1 << 1)) / 4096
    if (math.pi < dVar1):
        dVar1 = -(2 * math.pi - dVar1)

    return dVar1

def degreesToRadians(d):
    return d * math.pi / 180