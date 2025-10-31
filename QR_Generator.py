import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

content = input("Insert your name or email: ")
Number = int(input("Insert any number: "))
Generated = content + str(Number)

# Generate QR code and save as PNG
url = pyqrcode.create(Generated)
url.png("myqr.png", scale=5)
print("QR code is generated successfully")

# Display the generated QR code
qr_img = Image.open("myqr.png")
qr_img.show()

# QR code reader
answer = input("Do you want to read the QR code? (yes/no): ")

if answer.lower() == 'yes' or answer.upper() == 'YES':
    img = Image.open("myqr.png")
    cont = decode(img)
    print("QR code contains:")
    print(cont[0].data.decode())
else:
    print("Ending program.")
    exit()
