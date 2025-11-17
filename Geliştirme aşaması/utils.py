def menu_sec():
    while True:
        try:
            sec = int(input("\nİşlem Seçin : "))
            if sec < 0 or sec > 6 :
                print("\nLütfen 0-6 arasında bir değer girin...\n")
                continue
            return sec
        except ValueError:
            print("\nLütfen bir sayı/değer giriniz !\n")
            continue


def sayi_al():
    while True:
        try:
            sayi_gir = float(input("\nSayı Giriniz : "))
            if sayi_gir == int(sayi_gir):
                return int(sayi_gir)
            return sayi_gir
        except ValueError:
            print("Lütfen Sayıyı Doğru Giriniz !\n")
