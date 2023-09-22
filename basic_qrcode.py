import segno

qr_code = segno.make_qr('https://www.google.co.za')

qr_code.save("basic_qrcode.png")
