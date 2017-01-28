import png
import cmath
import math
from time import time
from subprocess import call

helpdoc = """parabolaGen help:

    parabolaGen(h, l)

    Let h be the height of the parabola. It must be a number greater than 0.
    Let l be the length of the parabola. It must also be a greater than 0.
    You can also use pGen(h, l) as a shortcut.
"""


def parabolaGen(h, l, open_paint=False, file_name="parabola_fine_horizontal",
                sqrt=math.sqrt, ceil=math.ceil):
    if _inputParser_(h, l):
        t = time()
        h = abs(int(h))
        l = abs(int(l))
        a = -4 * h / (l*l)
#Records the heights of the parabola at a certain position on the x-axis
        x = [(sqrt(a*(a*l**2+4*i+2))+a*l) / (2*a) for i in range(h-1, -1, -1)]

        p = [[] for i in range(h)]
        for dThreshold in range(1, ceil(l/2)+1):
            for pix in range(h):
                pixVal = 0
                if dThreshold > x[pix]:
                    pixVal = dThreshold - x[pix]
                    if pixVal > 1:
                        pixVal = 1
                p[pix].append(ceil(pixVal * 255))

        for row in range(h):
            for pix in range(int(l/2)-1, -1, -1):
                p[row].append(p[row][pix])

        png.from_array(p, 'L').save(file_name+".png")
        print("Parabola generation took ", time() - t, " seconds.")
        if open_paint:
            call(["mspaint", file_name+".png"], shell=True)


def pGen(h, l, open_paint=False):
    parabolaGen(h, l, open_paint)


def pHelp():
    print()
    print(helpdoc)


def _inputParser_(h, l, isnan=cmath.isnan):
    try:
        if not isnan(h) + isnan(l) + (not h) + (not l):
            return True
    except TypeError:
        pHelp()
        return False


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
