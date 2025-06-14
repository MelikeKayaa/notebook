### NOT DEFTERİ UYGULAMASI ###

from datetime import datetime

def not_ekle(notlar):
    ek = input('Eklemek istediğiniz notu giriniz: ')
    tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Notun yazıldığı yıl-ay-gün ve saat-dakika-saniye alıyor.
    not_metni = f'{ek} (Tarih: {tarih})'   # not ve tarih bilgisi birleştiriliyor.
    notlar.append(not_metni)     # birleşmiş olan not ve tarih bilgisi notlara ekleniyor.
    print('Not eklendi.')

def notlari_goster(notlar):
    if not notlar:     # notların içinde not yoksa kullanıcıya haber veriliyor.
        print('Notlar listeniz boş.')
    else:
        print('Notlarınız: ')
        for i, not_ in enumerate(notlar,1):  # girilen notlar 1 den itibaren numaralandırarak yazılıyor.
           print(f'{i}. {not_}')

def not_sil(notlar):
    if not notlar:
        print('Silinecek notunuz yok.')
    else:
            sil = int(input('Silmek istediğiniz notun numarasını giriniz: '))
            if 1<= sil <= len(notlar):
                silinen = notlar.pop(sil-1)
                print(f'{sil}. not silindi.')
            else:
                print('Geçersiz numara.')

def not_duzenle(notlar):
    if not notlar:  # notlar listesinde düzenlenecek not var mı kontrol ediliyor.
        print('Düzenlenecek not bulunamadı.')
        return

    print('Notlarınız: ')
    for i,not_ in enumerate(notlar,1):
        print(f'{i}. {not_}')

    try:
        secim = int(input('Düzenlemek istediğiniz notun numarasını giriniz. '))
        if 1 <= secim <= len(notlar):
            yeni_not = input('Düzenlenmiş notu giriniz: ')
            tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            notlar[secim - 1] = f'{yeni_not} ( Güncellendi: {tarih})'
            print('Not güncellendi.')
        else:
            print('Geçersiz numara girdiniz.')
    except ValueError:
        print('Lütfen geçerli bir sayı giriniz ! ')

def not_arama(notlar):
    kelime = input('Notlarda aramak istediğiniz kelimeyi giriniz: ').lower()
    for not_ in notlar:
        if kelime in not_.lower():
            print(not_)

def dosyaya_kaydet(notlar,dosya_adi = 'notlar.txt'):
    with open(dosya_adi,'w', encoding='utf-8') as file: # pythonda dosya açma yolu.w ile dosya yazma modunda açılır
        # .utf-8 türkçe karakterler için.with ile dosya işi bittiğinde otomatik kapanır.
        for not_ in notlar: # listedeki notları tek tek alır.
            file.write(not_ + '\n') # notları dosyaya yazar ve her notu ayrı satıra koyar.
    print(f'Notlar {dosya_adi} dosyasına kaydedildi.')

def dosyadan_oku(dosya_adi='notlar.txt'):
    notlar = []
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as file: # dosya okuma modunda açılır.
            for satir in file:
                satir = satir.strip() # satırdaki gereksiz boşluklar temizlenir.
                if satir: #boş satırı atlar.
                    notlar.append(satir)
    except FileNotFoundError:
        print(f'{dosya_adi} dosyası bulunamadı, yeni liste oluşturuluyor.')
    return notlar


def menu():
    notlar = dosyadan_oku()
    print('\n        *** KAYITLI NOTLAR *** ')
    notlari_goster(notlar)
    while True:
        print('\n--- NOT DEFTERİ ---')
        secim = input('1: Not Ekle | 2: Notları Göster | 3: Not Sil | 4: Not Düzenle | 5: Not Arama | 6: Notları kaydet | 7: Çıkış \n Seçiminiz: ')

        if secim == '1':
            not_ekle(notlar)
        elif secim == '2':
            notlari_goster(notlar)
        elif secim == '3':
            not_sil(notlar)
        elif secim == '4':
            not_duzenle(notlar)
        elif secim == '5':
            not_arama(notlar)
        elif secim == '6':
            dosyaya_kaydet(notlar,dosya_adi='notlar.txt')
        elif secim == '7':
            kayit =  input('Notlarınızı kaydetmek ister misiniz ? (E/H): ').upper()
            if kayit == 'E':
                 dosyaya_kaydet(notlar,dosya_adi='notlar.txt')
            print('Çıkılıyor...')
            break
        else:
            print('Geçerli bir seçim yapmadınız !')
menu()
