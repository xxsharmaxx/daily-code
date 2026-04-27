# Day 25: QR Code Generator

import qrcode

def generate_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR Code saved as {filename}")


# Input
data = input("Enter text or URL: ")
filename = input("Enter filename (e.g., qr.png): ")

generate_qr(data, filename)
