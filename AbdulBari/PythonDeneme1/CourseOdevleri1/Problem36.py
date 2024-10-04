ogrenciler = ['Ali', 'Ayse', 'Mehmet']
notlar = {'Ali': 90, 'Ayse': 85, 'Mehmet': 95}

# Öðrencileri notlarýna göre sýrala
sirali_ogrenciler = sorted(ogrenciler, key=lambda ogrenci: notlar[ogrenci])

print(sirali_ogrenciler)