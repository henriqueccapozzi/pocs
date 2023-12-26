#!/bin/python3

# Pre configuration steps
# sudo apt install python3-zbar
# pip install zbar

# Get text from QRCODE
from PIL import Image
from pyzbar.pyzbar import decode

result = decode(Image.open('qrcode_image.jpeg'))
print(result[0].data)

# ==========================================================================================
# Create a QRCODE from text
# https://medium.com/@rahulmallah785671/create-qr-code-by-using-python-2370d7bd9b8d
# pip install qrcode
import qrcode

# Create a QR code object with a larger size and higher error correction
qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

# Define the data to be encoded in the QR code
data = "henrique c. capozzi"

# Add the data to the QR code object
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code with a black fill color and white background
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qr_code_output.png")
