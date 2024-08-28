import pyautogui
import pygetwindow as gw
from PIL import Image
import keyboard
from datetime import datetime
import os
import time

# スクリーンショットを保存するディレクトリ
save_directory = "H:\python\ss\screenshots"

# ディレクトリが存在しない場合は作成
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

def take_screenshot_of_active_window():
    # アクティブウィンドウを取得
    window = gw.getActiveWindow()
    if window is not None:
        left, top, width, height = window.left, window.top, window.width, window.height
        # スクリーンショットを撮影
        screenshot = pyautogui.screenshot()
        # スクリーンショットをウィンドウの領域にクロップ
        cropped_screenshot = screenshot.crop((left, top, left + width, top + height))
        
        # 現在の日時をファイル名に使用
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(save_directory, f"screenshot_{timestamp}.png")
        
        # クロップした画像を保存
        cropped_screenshot.save(file_path)
        print(f"Screenshot saved to {file_path}")
    else:
        print("No active window found.")

# F11キーの押下を監視
# Alt + Control + Sキーの押下を監視
keyboard.add_hotkey('alt+ctrl+s', take_screenshot_of_active_window)

print("Press Alt + Control + S to take a screenshot of the active window.")


# プログラムを終了しないようにループ
# プログラムを終了しないようにループ
try:
    while True:
        # イベントループを効率的に管理するために短いスリープを追加
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated.")