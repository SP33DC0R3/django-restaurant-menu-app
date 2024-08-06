import qrcode

image = qrcode.make("https://127.0.0.1:8000")  # Change the url to the url of your app
image.save("qr.png")