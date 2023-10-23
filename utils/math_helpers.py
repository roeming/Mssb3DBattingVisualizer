import math

def floor(f):
    return math.trunc(f)


def LinearInterpolateToNewRange(value, prevMin, prevMax, nextMin, nextMax):
    min = 0.0
    max = 0.0
    if (min == (prevMax - prevMin)):
        max = 1.0
    else:
        max = 1.0
        calcedValue = (value - prevMin) / (prevMax - prevMin)

        if ((calcedValue <= max)):
            max = calcedValue
            if (calcedValue < min):
                max = min
    return (nextMax - nextMin) * max + nextMin

def valueToDegrees(v):
    return (v / 4096) * 360