import pyautogui
import time
import sys
import os
from PIL import Image

pyautogui.FAILSAFE = True

BUTTON_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "atla_button.png")

CHECK_INTERVAL   = 0.5
CONFIDENCE       = 0.7
CLICK_DELAY      = 0.2
AFTER_CLICK_WAIT = 1.0


def find_and_click(button_img):
    try:
        location = pyautogui.locateOnScreen(button_img, confidence=CONFIDENCE)
        if location:
            center = pyautogui.center(location)
            print(f"\n[OK] Buton bulundu! Konum: {center} -- Tiklaniyor...")
            time.sleep(CLICK_DELAY)
            pyautogui.click(center)
            print(f"[OK] Tiklandi. {AFTER_CLICK_WAIT}s bekleniyor...")
            time.sleep(AFTER_CLICK_WAIT)
            return True
    except pyautogui.ImageNotFoundException:
        pass
    except Exception as e:
        print(f"\n[!] Hata: {e}")
    return False


def main():
    if not os.path.exists(BUTTON_IMAGE):
        print(f"[X] Hata: Gorsel bulunamadi: {BUTTON_IMAGE}")
        sys.exit(1)

    try:
        button_img = Image.open(BUTTON_IMAGE)
        button_img.load()
    except Exception as e:
        print(f"[X] Hata: Gorsel acilamadi: {e}")
        sys.exit(1)

    print("=" * 50)
    print("  Atla Butonu Auto-Clicker")
    print("=" * 50)
    print(f"  Gorsel    : {BUTTON_IMAGE}")
    print(f"  Hassasiyet: {CONFIDENCE}")
    print(f"  Kontrol   : her {CHECK_INTERVAL}s")
    print()
    print("  Durdurmak icin: Ctrl+C")
    print("  veya fareyi ekranin SOL UST kosesine gotur")
    print("=" * 50)
    print()

    click_count = 0
    try:
        while True:
            clicked = find_and_click(button_img)
            if not clicked:
                print(f"\r[~] Buton aranıyor... (toplam tiklama: {click_count})", end="", flush=True)
            else:
                click_count += 1
                print(f"[i] Toplam tiklama sayisi: {click_count}")
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print(f"\n\n[!] Durduruldu. Toplam tiklama: {click_count}")
    except pyautogui.FailSafeException:
        print(f"\n\n[!] Fail-safe tetiklendi. Toplam tiklama: {click_count}")


if __name__ == "__main__":
    main()
