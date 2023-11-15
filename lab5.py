from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.savefig('histogram1.png')
    plt.show()

def zlicz_roznice_srednia_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if np.mean(t_obraz[i, j, :]) > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

def zlicz_roznice_suma_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if sum(t_obraz[i, j, :]) > wsp: # poniżej równoważne sformułowania tego warunku
                # if (t_obraz[i, j, 0] + t_obraz[i, j, 1] + t_obraz[i, j, 2]) > wsp:
                # if t_obraz[i, j, 0] > wsp or  t_obraz[i, j, 1] > wsp or t_obraz[i, j, 2] > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

def ukryj_kod(obraz, im_kod):
    t_obraz = np.asarray(obraz)
    t_kodowany = t_obraz.copy()
    h, w, d = t_obraz.shape
    t_kod = np.asarray(im_kod)
    for i in range(h):
        for j in range(w):
            if t_kod[i, j] > 0:
                k = randint(0,2)
                t_kodowany[i, j, k] = t_obraz[i, j, k] + 1
    return Image.fromarray(t_kodowany)

def are_arrays_the_same(tab1, tab2):
    x = 0
    # print(tab1)
    while tab1[x] == tab2[x]:
        if x == 2:
            return True
        x += 1
    return False


def odkoduj(obraz1, obraz2):
    t_obraz1 = np.asarray(obraz1)
    t_obraz2 = np.asarray(obraz2)
    h, w, d = t_obraz1.shape
    t_odkod = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            # print(t_obraz1[i, j], " ", t_obraz2[i, j])
            if are_arrays_the_same(t_obraz1[i, j], t_obraz2[i, j]):
                t_odkod[i, j] = 255
    return Image.fromarray(t_odkod)


# im1 = Image.open('im3.png')
#
# im1.save('diff.png')
#
# statystyki(im1)
# rysuj_histogram_RGB(im1)
# print("------------------")
# print(zlicz_roznice_srednia_RGB(im1, 0))
# print(zlicz_roznice_srednia_RGB(im1, 254.7))
# print(zlicz_roznice_srednia_RGB(im1, 100))

# im1 = Image.open('obraz.jpg')
# im1.save('obraz1.jpg')
# im2 = Image.open('obraz1.jpg')
# im2.save('obraz2.jpg')
# im3 = Image.open('obraz2.jpg')
# im3.save('obraz3.jpg')
# im4 = Image.open('obraz3.jpg')
# im4.save('obraz4.jpg')
# im5 = Image.open('obraz4.jpg')
# im5.save('obraz5.jpg')

# statystyki(im1)
# print("------------")
# statystyki(im2)
# print("------------")
# statystyki(im4)
# print("------------")
# statystyki(im5)

jesien = Image.open('jesien.jpg')
zakodowany = Image.open('zakodowany1.bmp')

statystyki(jesien)
print("-----------")
statystyki(zakodowany)

obraz = odkoduj(jesien, zakodowany)
obraz.show()
