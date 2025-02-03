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
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=5
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="red")

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if file_path:
            img.save(file_path)
            messagebox.showinfo("QR Code generated successfully", f"QR Code saved at {file_path}")


# Creating the main window
root = tk.Tk()
root.title("QR Code Generator - Developed by @Nemitha Wijerathna")

# Creating the label
tk.Label(root, text="Enter the data to be encoded:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Creating the button
tk.Button(root, text="Generate QR Code", command=generate_qr_code).pack(pady=20)

# Running the main loop
root.mainloop()