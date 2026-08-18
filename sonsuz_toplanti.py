#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ TOPLANTI SİMULATÖRÜ
===========================
Kurumsal dünyanın en kutsal ritüeli.
Hiçbir karar alınmaz. Sadece jargon üretilir.
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64 ile saklandı, çünkü toplantıda konuşulmaz)
# Decode edersen: "Özgür irade vardır ama toplantıda kullanılamaz."
_gizli = "T3pndXIgZXJhZGUgdmFyZGlyIGFtYSB0b3BsYW50xLFkYSBrdWxsYW7EsWxtYXou"

KATILIMCILAR = [
    "Proje Yöneticisi",
    "Senior Developer",
    "Ürün Sahibi",
    "İnsan Kaynakları",
    "Finans Temsilcisi",
    "Dışarıdan Gelen Danışman",
    "Hiçbir Şey Bilmeyen Ama Çok Konuşan Kişi",
    "Sessizce Not Tutan Stajyer",
]

JARGONLAR = [
    "aslında ben de aynı fikirdeyim ama...",
    "bu konuyu biraz daha derinlemesine ele almamız lazım",
    "stakeholder'ların beklentilerini de göz önünde bulundurarak",
    "synergy yaratmak açısından...",
    "low-hanging fruit'lara odaklanırsak",
    "bu aslında bir win-win durumu",
    "let's take this offline",
    "benim açımdan action item olarak...",
    "circle back yapabiliriz",
    "bu konuyu bir sonraki sprint'e bırakalım",
    "alignment sağlamamız gerekiyor",
    "ben de katılıyorum, ek olarak...",
    "paradigm shift gerektirebilir",
    "bu aslında cultural change konusu",
    "KPI'larımızı da unutmayalım",
    "benim side'ımdan bakınca...",
    "bu bir blocker olabilir",
    "dependency'leri de düşünmemiz lazım",
    "aslında çözüm basit ama...",
    "bu konuda more data'ya ihtiyacımız var",
]

KARAR_ENGELLEYICILER = [
    "ama önce risk analizi yapmamız lazım",
    "hukuk ekibinin de onayını almamız gerekiyor",
    "bütçe konusu netleşmeden ilerleyemeyiz",
    "üst yönetimden yeşil ışık beklemek durumundayız",
    "bu konuda bir çalışma grubu kuralım",
    "önce bir doküman hazırlayalım",
    "bir de anket yapalım mı?",
    "pilot çalışma ile başlayalım",
    "best practice'leri inceleyelim",
    "benchmark yapmadan karar veremeyiz",
]

def yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def toplanti_baslat():
    yaz("\n" + "="*60)
    yaz("  SONSUZ TOPLANTI SİMULATÖRÜ v1.0")
    yaz("  (Karar Alma Engelleme Sistemi Aktif)")
    yaz("="*60 + "\n")
    time.sleep(1)
    
    yaz("Toplantı odası hazırlanıyor...")
    time.sleep(0.8)
    yaz("Kahveler dağıtılıyor...")
    time.sleep(0.8)
    yaz("Projeksiyon açılıyor...")
    time.sleep(0.8)
    yaz("Herkes 'kamera açayım mı?' diye soruyor...\n")
    time.sleep(1.2)
    
    yaz("=== TOPLANTI BAŞLADI ===\n")
    time.sleep(1)

def konus(katilimci, cumle):
    yaz(f"[{katilimci}]: {cumle}")
    time.sleep(random.uniform(0.6, 1.4))

def ana_dongu():
    tur = 1
    while True:
        yaz(f"\n--- Tur {tur} (Hâlâ karar yok) ---\n")
        
        # Rastgele 3-5 kişi konuşsun
        konusmacilar = random.sample(KATILIMCILAR, k=random.randint(3, 5))
        
        for kisi in konusmacilar:
            cumle = random.choice(JARGONLAR)
            if random.random() < 0.4:
                cumle += " " + random.choice(KARAR_ENGELLEYICILER)
            konus(kisi, cumle)
        
        # Ara sıra sessizlik
        if random.random() < 0.25:
            yaz("\n[Uzun bir sessizlik... herkes ekrana bakıyor]\n")
            time.sleep(1.5)
        
        # Ara sıra "özet"
        if tur % 5 == 0:
            yaz("\n[Toplantı Yöneticisi]: Şimdiye kadar konuştuklarımızın özeti...")
            time.sleep(1)
            yaz("[Toplantı Yöneticisi]: ...aslında özet yok. Devam edelim.\n")
        
        tur += 1
        
        # Kullanıcıya çıkış şansı verme (ama zorlaştır)
        if tur % 7 == 0:
            yaz("\n[Sistem]: Toplantıyı bitirmek ister misiniz? (e/h)")
            # Cevabı bekleme, çünkü toplantı bitmez
            yaz("[Sistem]: Cevap alınamadı. Toplantı devam ediyor...\n")
            time.sleep(1)

if __name__ == "__main__":
    try:
        toplanti_baslat()
        ana_dongu()
    except KeyboardInterrupt:
        yaz("\n\n[Sistem]: Ctrl+C algılandı.")
        yaz("[Sistem]: Ama toplantılar Ctrl+C ile bitmez.")
        yaz("[Sistem]: Lütfen 'action item' oluşturun ve tekrar deneyin.")
        yaz("[Sistem]: Toplantı arka planda devam ediyor...\n")
        # Gizli mesajı hafifçe göster
        # print(_gizli)  # Yorum satırı, çünkü gizli
        sys.exit(0)
