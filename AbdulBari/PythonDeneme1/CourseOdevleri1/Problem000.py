import pyautogui
import time

# WhatsApp Web'in a��k oldu�undan ve gerekli sohbet penceresinin aktif oldu�undan emin ol.
time.sleep(25)  # Kullan�c�ya gerekli pencereyi a�mas� i�in 5 saniye bekler

message = "I LOVE U"
repeat_count = 100

for _ in range(repeat_count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(0.1)  # Her mesaj aras�nda k�sa bir bekleme s�resi

print("Mesajlar gonderildi.")