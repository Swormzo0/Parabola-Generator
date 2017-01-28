from png import from_array
from cmath import isnan
from math import ceil
from math import sqrt
from time import time
from subprocess import call


def parabolaGen(h, l, open_paint=False, file_name="parabola_antialiased"):
    """parabolaGen help:

    parabolaGen(h, l)

    Let h be the height of the parabola. It must be a number greater than 0.
    Let l be the length of the parabola. It must also be a greater than 0.
    You can also use pGen(h, l) as a shortcut.
    """
    if _inputParser_(h, l):
        t = time()
        h = abs(ceil(h))
        l = abs(ceil(l))
        a = -4 * h / (l*l)
        sff = round(h + (l**2-16*h**2)/(16*h))

#Records the heights of the parabola at a certain position on the x-axis
        if sff <= h:
            p = parabola_vBiased(h, sff, l, a) + parabola_hBiased(h, sff, l, a)
        else:
            p = parabola_vBiased(h, h, l, a)

        for row in range(h):
            p[row] += [p[row][pix] for pix in range(int(l/2)-1, -1, -1)]

        from_array(p, 'L').save(file_name+".png")
        print("Parabola generation took", time() - t, "seconds.")
        if open_paint:
            call(["mspaint", file_name+".png"], shell=True)
        return


def parabola_vBiased(h, sff, l, a):
    y = [a * (i+0.5) * (i+0.5-l) for i in range(l)]
    l = ceil(l/2)
    p = [[] for i in range(sff)]

    for row in range(sff):
        dThreshold = h - 1 - row
        for pix in range(l):
            pixVal = 0
            if y[pix] > dThreshold:
                pixVal = y[pix] - dThreshold
                if pixVal > 1:
                    pixVal = 1
            p[row].append(ceil(pixVal * 255))

    return p


def parabola_hBiased(h, sff, l, a):
    x = [(sqrt(a*(a*l**2+4*i+2))+a*l) / (2*a) for i in range(h-1, -1, -1)]
    l = ceil(l/2) + 1
    dsff = h-sff
    p = [[] for i in range(dsff)]

    for dThreshold in range(1, l):
        for pix in range(sff, h):
            pixVal = 0
            if dThreshold > x[pix]:
                pixVal = dThreshold - x[pix]
                if pixVal > 1:
                    pixVal = 1
            p[pix-sff].append(ceil(pixVal * 255))

    return p


def pGen(h, l, open_paint=False):
    parabolaGen(h, l, open_paint)


def pHelp():
    print()
    print(parabolaGen.__doc__)


def _inputParser_(h, l):
    try:
        if not (isnan(h) or isnan(l) or not h or not l):
            return True
        else:
            pHelp()
    except TypeError:
        pHelp()
        return False


#Please remove if this program is not run outside the Python console.

try:
    h = ceil(float(input("Please input the height of the desired parabola: ")))
    l = ceil(float(input("Please input the length of the desired parabola: ")))
    pGen(h, l, True)
except TypeError:
    pHelp()
except ValueError:
    pHelp()
