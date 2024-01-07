import qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=4,)

qr.add_data("https://github.com/aimei60")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="orange")
img.save("githubQRcode.png")