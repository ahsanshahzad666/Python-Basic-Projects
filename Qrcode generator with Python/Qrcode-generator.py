import qrcode

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)


data = "https://github.com/ahsanshahzad666"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='blue', back_color='white')
img.save('txt.png') 
