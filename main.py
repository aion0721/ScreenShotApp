import tkinter as tk
import pyautogui
import pygetwindow as gw
from PIL import Image, ImageDraw, ImageFont
import keyboard
from datetime import datetime
import os
import socket
from win10toast import ToastNotifier

# スクリーンショットを保存するディレクトリ
save_directory = os.path.join(os.path.expanduser('~'), 'Desktop', 'screenshots')

# ディレクトリが存在しない場合は作成
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# トースト通知のインスタンスを作成
toaster = ToastNotifier()

def take_screenshot_of_active_window():
    # アクティブウィンドウを取得
    window = gw.getActiveWindow()
    if window is not None:
        left, top, width, height = window.left, window.top, window.width, window.height
        # スクリーンショットを撮影
        screenshot = pyautogui.screenshot()
        # スクリーンショットをウィンドウの領域にクロップ
        cropped_screenshot = screenshot.crop((left, top, left + width, top + height))
        
        # 現在の日時とホスト名を取得
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hostname = socket.gethostname()
        
        # テキストを追加
        draw = ImageDraw.Draw(cropped_screenshot)
        text = f"{timestamp}\n{hostname}"
        font = ImageFont.load_default()
        # テキストのバウンディングボックスを取得
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_size = (text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1])
        text_position = (cropped_screenshot.width - text_size[0] - 10, cropped_screenshot.height - text_size[1] - 10)
        draw.text(text_position, text, font=font, fill="white")
        
        # ファイルパスを生成
        file_path = os.path.join(save_directory, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        
        # 画像を保存
        cropped_screenshot.save(file_path)
        print(f"Screenshot saved to {file_path}")
        
        # トースト通知を表示
        toaster.show_toast("スクリーンショット", "スクリーンショットが保存されました。", duration=3, threaded=True)
    else:
        print("No active window found.")

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("300x100")

# 説明ラベルを追加
label = tk.Label(root, text="Press Alt + Control + S to take a screenshot of the active window.")
label.pack(pady=20)

# Alt + Control + Sキーの押下を監視
keyboard.add_hotkey('alt+ctrl+s', take_screenshot_of_active_window)

# Tkinterのイベントループを開始
root.mainloop()
