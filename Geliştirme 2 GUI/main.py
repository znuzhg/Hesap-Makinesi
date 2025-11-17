import tkinter as tk

pencere = tk.Tk()
pencere.title("Hesap Makinesi v1")
pencere.geometry("300x400")
pencere.resizable(False, False)

# === EKRAN ===
ekran = tk.Entry(
    pencere,
    font=("Arial", 20),
    width=15,
    justify="right",
    bg="black",
    fg="white",
    bd=5,
)
ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# basılan rakamı ekranın sonuna ekleyen fonksiyon
def tus_bas(rakam):
    ekran.insert(tk.END, rakam)

# hesaplama fonksiyonu
def hesapla():
    try:
        ifade = ekran.get().replace("x","*")
        sonuc = eval(ifade)
        ekran.delete(0,tk.END)
        ekran.insert(tk.END, str(sonuc))
    except:
        ekran.delete(0, tk.END)
        ekran.insert(tk.END, "HATA")

# c tuşu için temizleme
def temizle():
    ekran.delete(0,tk.END)

# === BUTONLAR ===
#---------------------------------------------------------------------------------------------
# Rakamlar için satır ve kolon düzenini kod gelişmeden önde öğrendik ve not aldık
# Şimdi ise kod çok uzun ve karmaşık gözüküyor kodu for döngüsü ile kodu kısaltabiliriz
rakamlar = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 1)
]

for (rakam, row, col) in rakamlar:
    Sayi_Butonlari = tk.Button(
        pencere,
        text=rakam,
        font=("Arial", 15),
        width=4,
        height=2,
        bg="white",
        fg="black",
        bd=3,
        command=lambda r=rakam: tus_bas(r)

    )
    Sayi_Butonlari.grid(row=row,column=col, padx=5, pady=5)
#---------------------------------------------------------------------------------------------

#  ----------------------------------
# | *** işlem oparetör tuşları ***   |
#  ----------------------------------

# --- Toplama ---
#------------------------------------------------------------------------
buton_toplama = tk.Button(
    pencere,
    text="+",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("+")
)
buton_toplama.grid(row=4, column=3, padx=5, pady=5)
#------------------------------------------------------------------------
# --- Çıkarma ---
#------------------------------------------------------------------------
buton_cikarma = tk.Button(
    pencere,
    text="-",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("-")
)
buton_cikarma.grid(row=3, column=3, padx=5, pady=5)
#------------------------------------------------------------------------
# --- Çarpma ---
#------------------------------------------------------------------------
buton_carpma = tk.Button(
    pencere,
    text="x",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("x")
)
buton_carpma.grid(row=2, column=3, padx=5, pady=5)
#------------------------------------------------------------------------
# --- Bölme ---
#------------------------------------------------------------------------
buton_bolme = tk.Button(
    pencere,
    text="/",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("/")
)
buton_bolme.grid(row=1, column=3, padx=5, pady=5)
#------------------------------------------------------------------------
# --- Temizleme Butonu ---
#------------------------------------------------------------------------
buton_c = tk.Button(
    pencere,
    text="c",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: temizle()
)
buton_c.grid(row=4, column=0, padx=5, pady=5)
#------------------------------------------------------------------------
# --- Eşittir ---
#------------------------------------------------------------------------
buton_hesaplama = tk.Button(
    pencere,
    text="=",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: hesapla()
)
buton_hesaplama.grid(row=4, column=2, padx=5, pady=5)
#------------------------------------------------------------------------
pencere.mainloop()
