import math
menu = (
    """
=============================
      HESAP MAKİNESİ V1
=============================
  1) Toplama
  2) Çıkarma
  3) Bölme
  4) Çarpma
  5) Kare Alma
  6) Karekök
  0) Çıkış
=============================

    """
)

def sayi_al(aciklama):
    while True:
        try:
            return float(input(aciklama))
        except:
            print("\n *** Lütfen Bir Sayı Giriniz... ***\n")
def temiz_float(n):
    if n == int(n):
        return int(n)
    else:
        return n

while True:
    # Menü Seçimi
    while True:
        print(menu)
        try:
            sec = int(input("Lütfen Bir İşlem Seçin : "))
            if sec < 0 or sec > 6:
                print("\n\t\t *** Hata, lütfen 0-6 arasında bir değer giriniz ! ***\n")
                continue
            break

        except ValueError:
            print("\n\t\t *** lütfen geçerli bir değer/sayı giriniz ***\n")
            continue
    if sec == 0:
        print("\nProgramdan Çıkılıyor...\n"*3)
        print("* Program Kapatıldı *")
        break
    if sec in [1, 2, 3, 4]:
        print("\n\t---İşlem Yapılacak Sayıları Giriniz---\n")
        x = sayi_al("1. Sayıyı Gir : ")
        y = sayi_al("2. Sayıyı Gir : ")

        if sec == 1:
            sonuc = x + y
            print(f"{temiz_float(x)} + {temiz_float(y)} = {temiz_float(sonuc)}\n")
        elif sec == 2:
            sonuc = x - y
            print(f"{temiz_float(x)} - {temiz_float(y)} = {temiz_float(sonuc)}\n")
        elif sec == 3:
            if x == 0 or y == 0:
                print("\n\t\t *** Hata, bir sayı sıfıra bölünemez ! ***\n")
                continue
            sonuc = x / y
            print(f"{temiz_float(x)} / {temiz_float(y)} = {temiz_float(sonuc)}\n")
        elif sec == 4:
            sonuc = x * y
            print(f"{temiz_float(x)} * {temiz_float(y)} = {temiz_float(sonuc)}\n")
    if sec == 5:
        x = sayi_al("Karesi Alınacak Sayı : ")
        sonuc = x **2
        print(f"{temiz_float(x)}² = {temiz_float(sonuc)}\n")
    if sec == 6:
        x = sayi_al("Kökü Alınacak Sayı : ")
        if x < 0:
            print("\n\t\t *** Hata, Negatif Sayınının Karekökü Tanımsızdır.***\n")
            continue
        sonuc = math.sqrt(x)
        print(f"Sonuç: √{temiz_float(x)} = {temiz_float(sonuc)}\n")
    input("Ana Menüye Dönmek İçin [Enter]'a Basınız")