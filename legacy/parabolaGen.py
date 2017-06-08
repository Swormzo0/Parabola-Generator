import png
import cmath
import math
import time
from subprocess import call


def parabolaGen(h, l, open_paint=False, file_name="parabola"):
    if _inputParser_(h, l) is not None:
        t = time.time()
        h = abs(int(h))
        l = abs(int(l))
        a = -4 * h / (l*l)
        y = [_mround_(a * (i+0.5) * (i+0.5-l)) for i in range(l)]

        p = []
        for i in range(h):
            p.append([])
            drawThreshold = h - 1 - i
            for j in range(math.ceil(l/2)):
                pixVal = 0
                if y[j] > (drawThreshold):
                    pixVal = y[j] - drawThreshold
                    if pixVal > 1:
                        pixVal = 1
                p[i].append(math.ceil(pixVal * 255))

        for row in range(h):
            for pix in range(int(l/2)-1, -1, -1):
                p[row].append(p[row][pix])

        png.from_array(p, 'L').save(file_name+".png")
        print("Parabola generation took ", time.time() - t, " seconds.")
        if open_paint:
            call(["mspaint", file_name+".png"], shell=True)


def pGen(h, l, open_paint=False):
    parabolaGen(h, l, open_paint)


def pHelp():
    print("parabolaGen help: ")
    print()
    print("parabolaGen(h, l)")
    print("Let h be the height of the parabola. It must be a number.")
    print("Let l be the length of the parabola. It must also be a number.")
    print("You can also use pGen(h, l) as a shortcut.")


def _inputParser_(h, l, isnan=cmath.isnan):
    try:
        if not isnan(h) + isnan(l) + (not h) + (not l):
            return True
    except TypeError:
        pHelp()
        return False


def _mround_(x):
    x *= 2
    if x >= (math.floor(x)+0.5):
        return math.ceil(x) / 2
    else:
        return math.floor(x) / 2


#Please remove if this program is not run outside the Python console.

try:
    h = math.ceil(float(input(
        "Please input the height of the desired parabola: ")))
    l = math.ceil(float(input(
        "Please input the length of the desired parabola: ")))
    pGen(h, l, True)
except TypeError:
    pHelp()
except ValueError:
    pHelp()
