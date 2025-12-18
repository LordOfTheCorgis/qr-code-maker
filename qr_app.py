import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import os
import sys

current_qr = None

def generate_qr():
    global current_qr
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return
    qr = qrcode.make(url).resize((250, 250))
    current_qr = qr
    qr_img = ImageTk.PhotoImage(qr)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img

def save_qr():
    if current_qr is None:
        messagebox.showwarning("No QR", "Please generate a QR code first.")
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if file_path:
        current_qr.save(file_path)
        messagebox.showinfo("Saved", f"QR code saved to:\n{file_path}")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x420")
root.resizable(False, False)

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(base_path, "icon.png")
icon_img = ImageTk.PhotoImage(file=icon_path)
root.iconphoto(True, icon_img)

ttk.Label(root, text="Enter URL:").pack(pady=(15, 5))
url_entry = ttk.Entry(root, width=35)
url_entry.pack(pady=5)

ttk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)
ttk.Button(root, text="Save QR Code", command=save_qr).pack(pady=5)

qr_label = ttk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
