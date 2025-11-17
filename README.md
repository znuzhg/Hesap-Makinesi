# 🧮 Python Hesap Makinesi Projesi

**Konsol → Modüler Kod → GUI (Tkinter) → EXE**  
Tam bir yazılım geliştirme süreci örneğidir.

Bu proje, Python kullanarak sıfırdan başlayıp adım adım ilerleyerek hazırladığım hesap makinesi uygulamasının tüm gelişim aşamalarını içerir.  
İlk konsol sürümünden başlayıp, modüllere ayrılmış temiz koda geçtim, ardından Tkinter GUI tasarladım ve son aşamada projeyi **.exe uygulamasına** dönüştürdüm.

---

## 📁 Proje Klasör Yapısı

Aşağıdaki tablo, projedeki klasörlerin ne işe yaradığını göstermektedir:


| 📂 **Klasör**            | 📝 **Açıklama**                                                                 |
|--------------------------|----------------------------------------------------------------------------------|
| **İlk Kod/**             | Konsolda çalışan en temel, başlangıç versiyonu.                                  |
| **Geliştirme aşaması/**  | Modüler yapı (menu.py, utils.py, islemler.py), hata kontrolleri, temiz kodlama.  |
| **Geliştirme 2 GUI/**    | Tkinter ile hazırlanmış çalışan grafik arayüz (butonlar, işlemler, C, =).        |
| **Son Hali EXE/**        | PyInstaller ile üretilmiş **Hesap Makinesi V1.exe** dosyası.                     |


---

## 🎯 Projenin Amacı

Bu projede hedeflenen yazılım geliştirme becerileri:

- Fonksiyonları etkili şekilde kullanmak  
- `try/except` ile hata yönetimi  
- Modüler Python yapısı  
- Tkinter ile GUI oluşturmak  
- Konsol uygulamasını GUI uygulamasına dönüştürmek  
- PyInstaller ile EXE üretmek  

---

## 🧮 Konsol Versiyonu Özellikleri

✔ Toplama  
✔ Çıkarma  
✔ Çarpma  
✔ Bölme (Sıfıra bölme kontrolüyle)  
✔ Kare alma  
✔ Karekök (negatif sayı kontrolüyle)  
✔ Temiz float gösterimi (`1.0` → `1`)

---

## 🖥️ GUI (Tkinter) Versiyonu Özellikleri

✔ Modern pencere tasarımı  
✔ Siyah ekran – beyaz tuşlar  
✔ Basılan tuşun ekrana otomatik yazılması  
✔ +, -, x, / operatör tuşları  
✔ C (Temizle) butonu  
✔ "=" ile işlem hesaplama  
✔ Hatalı işlemde ekrana **"HATA"** yazdırma  

---

## ⚙️ Kullanılan Teknolojiler

- Python 3.11  
- Tkinter (GUI)  
- Math kütüphanesi  
- PyInstaller (EXE oluşturma)

---

## 📌 EXE Nasıl Oluşturuldu?

Kullanılan PyInstaller komutu:

pyinstaller --onefile --noconsole gui.py

yaml
Kodu kopyala

Oluşan `.exe` dosyası **Son Hali EXE/** klasörüne taşınmıştır.

---

## 📤 Projeyi Çalıştırma

### Konsol Sürümü
python main.py

shell
Kodu kopyala

### GUI Sürümü
python gui.py

yaml
Kodu kopyala

---

## 💬 Geliştirici Notu

Bu proje, bir yazılımın **temelden profesyonele** ilerleyiş sürecinin tam örneğidir:

**Konsol → Modüler Python → GUI (Tkinter) → EXE**

Eğitim ve kişisel gelişim amacıyla hazırlanmış olup geliştirilmeye açıktır.

---

## 📎 Proje Linki

👉 https://github.com/znuzhg/Hesap-Makinesi

---
