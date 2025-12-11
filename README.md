# Basit Keylogger 

Bu proje, siber güvenlik eğitimim kapsamında sistem programlama ve "hooking" (kanca atma) mantığını kavramak amacıyla geliştirdiğim temel seviye bir tuş kaydedici (keylogger) uygulamasıdır.

Projenin Amacı ve Yasal Uyarı
Bu yazılım tamamen eğitim ve farkındalık amacıyla geliştirilmiştir. Klavye dinleme tekniklerinin nasıl çalıştığını ve sistemlerin bu tür arka plan servislerini nasıl algıladığını anlamayı hedefler. Başkalarının bilgisayarında izinsiz kullanımı yasal suç teşkil eder ve sorumluluk kullanıcıya aittir.

Neler Yapıldı?
Python'un "pynput" kütüphanesi kullanılarak klavye hareketlerini dinleyen bir yapı kuruldu.
- Basılan tuşların anlık olarak yakalanması.
- Özel tuşların (Enter, Space, Shift vb.) anlamlı formatta kaydedilmesi.
- Verilerin scriptin bulunduğu dizinde "keylogs.txt" dosyasına anlık olarak (tampon bellek kullanmadan) yazılması sağlandı.

Python Olmayan Bilgisayarda Çalıştırma Mantığı (Taşınabilirlik)
Bu proje şu an kaynak kod (.py) halindedir. Ancak geliştirme sürecinde, hedef sistemde Python yüklü olmasa bile kodun nasıl çalıştırılabileceğini araştırdım.
Normalde Python kurulu olmayan bir bilgisayarda bu kodu çalıştırmak için "PyInstaller" veya "Auto-Py-To-Exe" gibi araçlar kullanılarak proje tek bir çalıştırılabilir dosyaya (.exe) dönüştürülür. 
Bu sayede gerekli tüm kütüphaneler tek bir paketin içine gömülür ve program herhangi bir Windows bilgisayarda çift tıklanarak çalışabilir hale gelir. (Bu sürümde .exe dönüşümü yapılmamış, kaynak kod paylaşılmıştır).
(Bunu daha sonra yapmayı deneyeceğim)

- Python 3
- pynput (Klavye dinleme modülü)
- os & sys (Sistem dosya yolları yönetimi)

Kurulum ve Test
1. Gerekli kütüphaneyi yükleyin: pip install pynput
2. Scripti çalıştırın: python logger.py
3. Durdurmak için terminalde CTRL + C yapabilirsiniz.
4. Kaydetme işlemi txt dosyasındadır.

Emircan Bingöl
