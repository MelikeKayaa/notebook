# 📝 Kendi Dijital Not Defteriniz (TR)

**Gizli tarifleri, unutulmaması gereken görevleri ve aniden gelen fikirleri saklamak için ideal bir yer !**  
Artık dağınık kâğıtlarla veya kaybolan notlarla uğraşmak yok. " Bir yere yazmıştım ama nerede?" sorusuna veda zamanı.
Bu metin tabanlı Python projesi ile kendi kişisel not defterinizi yönetin !

---

## Proje Hakkında :
Bu proje, metin tabanlı interaktif bir not defteri uygulamasıdır. Kullanıcı, not ekleyebilir, silebilir, düzenleyebilir, arama yapabilir ve notlarını .txt dosyasına kaydedebilir. Program başlatıldığında daha önce kaydedilmiş notlar otomatik olarak yüklenir.
 
---

##  Özellikler :

- Not ekleme ( tarih ve saat bilgisi ile birlikte )
- Notları listeleme
- Not silme
- Not düzenleme ( değiştirme tarihi ve saat bilgisi ile birlikte)
- Anahtar kelime ile not arama
- Notları ' .txt ' dosyasına kaydetme
- Uygulama açıldığında daha önce kaydedilen notları otomatik görüntüleme
- Kullanıcı dostu metin tabanlı menü

--- 

## Kullanılan Teknolojiler Ve Yapılar :

- Python 3
- Fonksiyonlar : Her işlem(not ekleme,silme,düzenleme,arama,kaydetme) ayrı fonksiyonlar halinde yapılandırılmıştır. Bu sayede kod daha okunabilir ve sürdürülebilir hale gelmiştir.
- Döngüler : while ve for döngüleri ile kullanıcıdan sürekli giriş alınmakta ve notlar listelenmektedir.
- Listeler : Notlar bir liste yapısında tutulmaktadır. Not ekleme, silme ve düzenleme işlemleri doğrudan bu liste üzerinden gerçekleştirilir.
- datetime Modülü : Notlara ve düzenlemelere tarih- saat bilgisi eklemek için kullanılmıştır.
- Dosya İşlemleri : open(), write(), read() gibi dosya fonksiyonlarıyla notlar.txt dosyasına kaydedilir ve program başlarken bu dosyadan notlar otomatik olarak gösterilir.
- String İşlemleri : lower(), strip(), split() gibi string metotları ile metin işleme yapılır.
- Koşullar : Kullanıcıdan gelen seçimlere göre if-elif-else bloklarıyla akış kontrol edilmiştir.
- Hata Yakalama : Dosya bulunamazsa FileNotFoundError yakalanarak kullanıcıya bilgilendirme yapılır. Yanlış bir sayı girilirse ValueError uyarısı yapılır.
        
---

## Nasıl Kullanılır ?

1. Python yüklü bir ortamda terminali açın.
2. ' not_defteri.py ' dosyasının bulunduğu klasöre gidin.
3. Aşağıdaki komutu çalıştırarak programı başlatın.

python not_defteri.py

