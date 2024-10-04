import pyautogui
import time

# WhatsApp Web'in açýk olduðundan ve gerekli sohbet penceresinin aktif olduðundan emin ol.
time.sleep(25)  # Kullanýcýya gerekli pencereyi açmasý için 5 saniye bekler

message = "I LOVE U"
repeat_count = 100

for _ in range(repeat_count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(0.1)  # Her mesaj arasýnda kýsa bir bekleme süresi

print("Mesajlar gonderildi.")