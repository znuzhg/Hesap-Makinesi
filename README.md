📌 Python ile Konsol + GUI Hesap Makinesi Projesi

Bu proje, Python kullanarak geliştirdiğim konsol tabanlı ve Tkinter GUI tabanlı bir hesap makinesinin tam gelişim sürecini içermektedir.
Temelden başlayarak, adım adım GUI’ye geçiş, hata kontrolü, fonksiyon yapıları ve en sonunda .EXE uygulamasına dönüştürme aşamalarını kapsamaktadır.

📁 Proje Klasör Yapısı
Klasör	Açıklama
İlk Kod/	Projeye ilk başladığım konsol versiyonunun temel hali.
Geliştirme aşaması/	Fonksiyonların ayrılması (utils, menu, islemler), temiz kodlama, hata kontrolleri yapılan orta seviye sürüm.
Geliştirme 2 GUI/	Tkinter kullanarak oluşturduğum grafik arayüzlü hesap makinesi. Rakam tuşları, operatörler ve “=” dâhil tüm butonlar çalışır.
Son Hali EXE/	PyInstaller ile oluşturulmuş çalışabilir Hesap Makinesi V1.exe dosyası.
🎯 Projenin Amacı

Bu projede amaç:

Python’da fonksiyonları etkin kullanmak

Hata yönetimi (try/except)

Modüler programlama (menu.py, utils.py, islemler.py)

Tkinter ile GUI geliştirme

Konsol uygulamasını GUI uygulamasına yükseltme

PyInstaller ile EXE üretmek

🧮 Konsol Versiyonu Özellikleri

✔ Toplama
✔ Çıkarma
✔ Çarpma
✔ Bölme (Sıfıra bölme kontrolü ile)
✔ Kare Alma
✔ Karekök (Negatif sayı hata kontrolü ile)
✔ Temiz float gösterimi (1.0 yerine 1 yazdırma)

🖥️ GUI (Tkinter) Versiyonu Özellikleri

✔ Modern pencere tasarımı
✔ Siyah ekran – beyaz tuşlar
✔ Buton basıldığında ekrana otomatik yazma
✔ +, -, x, / operatör tuşları
✔ C (temizle) tuşu
✔ = ile işlem sonucunu hesaplama
✔ Hataları ekrana "HATA" olarak yansıtma

⚙️ Kullanılan Teknolojiler

Python 3.11

Tkinter (GUI)

Math kütüphanesi

PyInstaller (EXE çevrim)

📌 EXE Nasıl Oluşturuldu?

Aşağıdaki komut kullanıldı:

pyinstaller --onefile --noconsole gui.py


Oluşan .exe dosyası Son Hali EXE/ klasörünün içine taşındı.

📤 Projeyi Çalıştırma
Konsol versiyonu:
python main.py

GUI versiyonu:
python gui.py

📷 Ekran Görüntüsü

(İstersen buraya GUI ekran resmini ekleyebilirsin.)

📎 Proje Linki

👉 https://github.com/znuzhg/Hesap-Makinesi

(Hocaya vereceğin link budur.)

💬 Geliştirici Notu

Bu proje, temelden gelişime doğru ilerleyen bir öğrenme sürecinin tamamını içerir.
Önce konsol, sonra modüller, ardından GUI ve en son EXE dönüşümü ile proje bir yazılım geliştirme sürecini tam olarak anlatmaktadır.

📌 Lisans

Bu proje eğitim ve kişisel gelişim amaçlıdır.
