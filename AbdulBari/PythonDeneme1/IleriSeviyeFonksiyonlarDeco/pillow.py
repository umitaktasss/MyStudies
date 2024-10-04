from PIL import Image,ImageFilter

image = Image.open(r"C:\Users\Tulpar\Downloads\kus.jpg")
#Farkl� bir �ekilde kaydetme.
image.save("kus2.jpg")
#Rotate D�nd�rme
image.rotate(180).save("kus3.jpg")

image.rotate(90).save("kus4.jpg")
#Siyah-Beyaz 
image.convert(mode="L").save("kus5.jpg")

#Coz�n�rl�k degistirme

degistir=(960,600)

image.thumbnail(degistir)
image.save("kus6.jpg")
image.filter(ImageFilter.GaussianBlur(5)).save("kus7.jpg")
