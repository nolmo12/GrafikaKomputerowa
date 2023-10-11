from PIL import Image
import numpy as np

def rysuj_paski_w_obrazie(obraz, grub): # rysuje pionowy pas grubości grub po lewej stronie oraz po prawej stronie
    tab_obraz = np.asarray(obraz)*1 # wczytanie tablicy obrazu i zamiana na int
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j]=0
        for j in range(w-grub,w):
            tab_obraz[i][j]=0
    tab = tab_obraz.astype(bool) # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)

def rysuj_ramke_w_obrazie(obraz, grub):
    image_array = np.asarray(obraz) * 1
    h, w = image_array.shape

    i = 0

    for x in range(w):
        for y in range(grub):
            if i < grub:
                image_array[i][x] = 0
                i += 1
        i = 0

    j = h - 1

    for x in reversed(range(w)):
        for y in range(grub):
            if j > h - grub - 1:
                image_array[j][x] = 0
                j -= 1
        j = h - 1

    obraz = Image.fromarray(image_array)

    return rysuj_paski_w_obrazie(obraz, grub)

def rysuj_ramke(w, h, grub): # grub grubość ramki w pikselach
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    tab[grub:h - grub, grub:w - grub] = 1  # skrócona wersja ustawienia wartości dla prostokatnego fragmentu tablicy [zakresy wysokości, zakresy szerokości] tablicy
    tab1 = tab.astype(bool)
    return tab1

def draw_spiral_border(w, h, grub):
    tab = (h, w)
    array = np.zeros(tab, dtype=np.uint8)
    ile = int(min(w, h)/grub)
    print(ile)

    print(array)

img = Image.open("inicjaly.bmp")
img.load()

# new_img = rysuj_ramke_w_obrazie(img, 10)
# new_img.show()
# new_img.save("ramka10.bmp")
# #zad 2
# new_img1 = rysuj_ramke_w_obrazie(img, 5)
# new_img1.show()
# new_img1.save("ramka5.bmp")

# tab = rysuj_ramke(120, 60, 8)
# print("typ danych tablicy", tab.dtype)
# print("rozmiar wyrazu tablicy:",   tab.itemsize)
# im_ramka = Image.fromarray(tab)
# im_ramka.show()

draw_spiral_border(20, 10, 2)
