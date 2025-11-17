from menu import menu_goster
from utils import sayi_al, menu_sec
from islemler import *

while True:
    print(menu_goster())
    sec = menu_sec()
    if sec == 0:
        print("* Program Kapatılıyor\n" *3)
        print("* Program Kapatıldı *")
        break
    if sec == 1:
        print("\n--- Toplama İşlemi ---\n")
        x = sayi_al()
        y = sayi_al()
        sonuc = topla(x,y)
        print(f"\n{x} + {y} = {sonuc}\n")
    if sec == 2:
        print("\n--- Çıkarma İşlemi ---\n")
        x = sayi_al()
        y = sayi_al()
        sonuc = cikar(x,y)
        print(f"\n{x} - {y} = {sonuc}\n")
    if sec == 3:
        print("\n--- Bölme İşlemi ---\n")
        x = sayi_al()
        while True:
            y = sayi_al()
            if y == 0:
                print("\n*** Bir Sayı Sıfıra Bölünemez! Bölen değerini yeniden girin. ***\n")
                continue
            break
        sonuc = bol(x, y)
        print(f"\n{x} / {y} = {sonuc}\n")
    if sec == 4:
        print("\n--- Çarpma İşlemi ---\n")
        x = sayi_al()
        y = sayi_al()
        sonuc = carp(x,y)
        print(f"\n{x} * {y} = {sonuc}\n")
    if sec  == 5:
        x = sayi_al()
        sonuc = kare(x)
        print(f"\n{x}² = {sonuc}\n")
    if sec == 6:
        while True:
            x = sayi_al()
            if x < 0:
                print("Hata: Negatif sayının karekökü alınamaz !\n")
                continue
            sonuc = karekok(x)
            print(f"\n√{x} = {sonuc}\n")
            break
    input("Ana Menüye Dönmek İçin [Enter]'a Basınız")
