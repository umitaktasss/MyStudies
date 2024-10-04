ogrenciler = ['Ali', 'Ayse', 'Mehmet']
notlar = {'Ali': 90, 'Ayse': 85, 'Mehmet': 95}

# ��rencileri notlar�na g�re s�rala
sirali_ogrenciler = sorted(ogrenciler, key=lambda ogrenci: notlar[ogrenci])

print(sirali_ogrenciler)