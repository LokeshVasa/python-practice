import qrcode

qr = qrcode.make("heloo")
qr.save("myqr.png")
print("QR code saved as myqr.png")
