def notHesapla(satir):
    satir=satir[:-1]
    liste=satir.split(",")
    print(liste)
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    son_not=not1*(0.3)+not2*(0.3)+not3*(0.4)
    if son_not>=90:
        harf="AA"
    elif son_not>=85:
        harf="BA"
    elif son_not>=80:
        harf="BB"
    elif son_not>=75:
        harf="BC"
    elif son_not>=70:
        harf="CC"
    elif son_not>=65:
        harf="CD"
    elif son_not>=60:
        harf="DD"
    elif son_not>=55:
        harf="FD"
    else:
        harf="FF"
    return isim+ "----------------->" + harf + "\n"






with open("Notlar.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []
    gecenler_listesi = []  # Geçenlerin listesi
    for i in file:
        not_bilgisi = notHesapla(i)
        eklenecekler_listesi.append(not_bilgisi)
        if "FF" not in not_bilgisi:  # FF harf notu yoksa geçenler listesine ekle
            gecenler_listesi.append(not_bilgisi)
    with open("notlar2.txt", "w") as file2:
        for not_bilgisi in eklenecekler_listesi:
            file2.write(not_bilgisi)
    with open("Gecenler.txt", "w") as file3:
        for not_bilgisi in gecenler_listesi:
            file3.write(not_bilgisi)

     