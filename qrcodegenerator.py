# Importing the necessary libraries
import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog

# Function to generate the QR code
def generate_qr_code():
    data = entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )