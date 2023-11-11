import pyqrcode
import png

from pyqrcode import QRCode
address='addres'
url = pyqrcode.create(address)
url.png('image.png', scale=7)
