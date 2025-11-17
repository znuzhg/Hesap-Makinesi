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

# === BUTONLAR ===

buton_1 = tk.Button(
    pencere,
    text="1",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("1")
)
buton_1.grid(row=3, column=0, padx=5, pady=5)


buton_2 = tk.Button(
    pencere,
    text="2",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("2")
)
buton_2.grid(row=3, column=1, padx=5, pady=5)

buton_3 = tk.Button(
    pencere,
    text="3",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("3")
)
buton_3.grid(row=3, column=2, padx=5, pady=5)

buton_4 = tk.Button(
    pencere,
    text="4",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("4")
)
buton_4.grid(row=2, column=0, padx=5, pady=5)


buton_5 = tk.Button(
    pencere,
    text="5",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("5")
)
buton_5.grid(row=2, column=1, padx=5, pady=5)

buton_6 = tk.Button(
    pencere,
    text="6",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("6")
)
buton_6.grid(row=2, column=2, padx=5, pady=5)

buton_7 = tk.Button(
    pencere,
    text="7",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("7")
)
buton_7.grid(row=1, column=0, padx=5, pady=5)


buton_8 = tk.Button(
    pencere,
    text="8",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("8")
)
buton_8.grid(row=1, column=1, padx=5, pady=5)

buton_9 = tk.Button(
    pencere,
    text="9",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("9")
)
buton_9.grid(row=1, column=2, padx=5, pady=5)

buton_0 = tk.Button(
    pencere,
    text="0",
    font=("Arial", 15),
    width=4,
    height=2,
    bg="white",
    fg="black",
    bd=3,
    command=lambda: tus_bas("0")
)
buton_0.grid(row=4, column=1, padx=5, pady=5)

# işlem oparetör tuşları

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
# c tuşu ekran temizleme fonksiyonu
def temizle():
    ekran.delete(0,tk.END)
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

# hesaplama fonksiyonu
def hesapla():
    try:
        ifade = ekran.get()
        sonuc = eval(ifade)
        ekran.delete(0,tk.END)
        ekran.insert(tk.END, str(sonuc))
    except:
        ekran.delete(0, tk.END)
        ekran.insert(tk.END, "HATA")
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

pencere.mainloop()
