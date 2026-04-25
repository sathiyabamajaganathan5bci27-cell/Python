import qrcode

img = qrcode.make("https://google.com")
img.save("my_qr.png")
print("QR Code Saved!")
