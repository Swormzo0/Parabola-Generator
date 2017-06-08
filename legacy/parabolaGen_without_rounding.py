import png
import cmath
import math
from time import time
from subprocess import call


def parabolaGen(h, l, open_paint=False, file_name="parabola_fine_vertical",
                ceil=math.ceil):
    if _inputParser_(h, l):
        t = time()
        h = abs(int(h))
        l = abs(int(l))
        a = -4 * h / (l*l)
#Records the heights of the parabola at a certain position on the x-axis
        y = [a * (i+0.5) * (i+0.5-l) for i in range(l)]

        p = [[] for i in range(h)]
        for row in range(h):
            dThreshold = h - 1 - row
            for pix in range(ceil(l/2)):
                pixVal = 0
                if y[pix] > dThreshold:
                    pixVal = y[pix] - dThreshold
                    if pixVal > 1:
                        pixVal = 1
                p[row].append(ceil(pixVal * 255))

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
        else:
            pHelp()
    except TypeError:
        pHelp()
        return False


#Please remove if this program is not run outside the Python console.

try:
    height = int(input("Please input the height of the desired parabola: "))
    length = int(input("Please input the length of the desired parabola: "))
    pGen(height, length, True)
except TypeError:
    pHelp()
except ValueError:
    pHelp()
