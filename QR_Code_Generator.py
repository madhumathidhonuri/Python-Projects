#pip install qrcode[pil]

import qrcode
#qrcode module,allows you to generate QR codes in Python.

import qrcode.constants
#This imports constants used in the QR code generation process, like error correction levels.

data="HAPPY BIRTHDAY!"

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
# version=1: Controls the size of the QR code (1 is the smallest, fitting up to 25 characters).
#error_correction=qrcode.constants.ERROR_CORRECT_L: Sets the error correction level to Low (L), meaning it can recover about 7% of data if the QR code gets damaged.

qr.add_data(data)
#Adds the actual data ("HAPPY BIRTHDAY!") into the QR code object.

qr.make(fit=True)
# Generates the QR code. fit=True tells it to automatically choose the best version/size to fit the data (unless overridden by version).

img=qr.make_image(fill_color='black',back_color='white')

img.save("qrcode.png")