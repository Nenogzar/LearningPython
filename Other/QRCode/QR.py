# pip install PyQRCode
# pip install pypng

import pyqrcode
import png
link = input("input link: ")
qr_code = pyqrcode.create(link)
qr_code.png(f"{link}.png", scale15)