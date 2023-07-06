import qrcode
qr=qrcode.QRCode(version=1)
link=input("Enter your link here")
qr.add_data(link)
qr.make(fit=True)
f_color=input("Choose primary color")
s_color=input("Choose secondary color")
img=qr.make_image(fill_color=f_color,back_color=s_color)
file_name=input("Enter the name of the file you want to save as")
img.save(f"{file_name}.png")