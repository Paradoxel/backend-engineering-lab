import qrcode

data = input("Enter text or URL: ")

img = qrcode.make(data)

img.show()

print("QR Code generated successfully!")