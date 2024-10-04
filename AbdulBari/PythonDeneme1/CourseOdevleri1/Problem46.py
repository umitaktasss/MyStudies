isim= ["Kerim","Tarik","Ezgi","Kemal","Ilkay","Sukran","Merve"]
soy_isim=["Yilmaz", "Ozturk", "Dagdeviren", "Ataturk", "Dikmen","Kaya", "Polat"]

tam_isimler=[f"{i} {s}" for i, s in zip(isim, soy_isim)]

tam_isimler_sorted= sorted(tam_isimler)

for isim in tam_isimler_sorted:
    print(isim)