import qrcode

# Generate the QR code
img = qrcode.make("https://google.com")

# Save it as an image file
img.save("my_qr_code.png")