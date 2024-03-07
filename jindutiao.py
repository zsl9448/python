import tkinter as tk
from tkinter import ttk
import time

def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        progress_bar["value"] = i
        window.update_idletasks()
        time.sleep(0.1)  # 模拟耗时操作
    progress_bar["value"] = 0

# 创建主窗口
window = tk.Tk()
window.title("进度条示例")

# 创建进度条
progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

# 创建按钮来触发进度条
start_button = tk.Button(window, text="开始进度条", command=run_progressbar)
start_button.pack(pady=10)

# 运行主循环
window.mainloop()