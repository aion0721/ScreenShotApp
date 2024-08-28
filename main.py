import pyautogui
import keyboard
import time
from datetime import datetime
import os

# スクリーンショットを保存するディレクトリ
save_directory = "H:\python\ss\screenshots"

# ディレクトリが存在しない場合は作成
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

def take_screenshot():
    # 現在の日時をファイル名に使用
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(save_directory, f"screenshot_{timestamp}.png")
    
    # スクリーンショットを撮影して保存
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)
    print(f"Screenshot saved to {file_path}")

# F11キーの押下を監視
keyboard.add_hotkey('f11', take_screenshot)

print("Press F11 to take a screenshot of the active window.")

# プログラムを終了しないようにループ
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated.")
