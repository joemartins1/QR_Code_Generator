# QR CODE Generator
# Python Projet by Joe

# Main file

import qrcode
import cv2
from PIL import Image
import os


def introduction_print():
    print()
    os.system("type ascii_intro.txt")
    print()

# QRCode Encode function
def qrcode_generator(content, image):
    img = qrcode.make(content)
    type(img)  # qrcode.image.pil.PilImage
    img.save(image + ".png")
    print(f"Your QRCode '{image}'tt has been saved")

# QRCode Decoder function
def qrcode_decoder(content):
    qrcode_image_for_decode = cv2.imread(content)
    qrcode_image_detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = qrcode_image_detector.detectAndDecode(qrcode_image_for_decode)
    # decoder_image_pil = Image.open(content)
    # decode_qr_result = decode(decoder_image_pil)
    print(f"QRCode content is: {data}")


# Choice Menu
menu_choice = ""
while menu_choice == "":
    os.system("Title QRCode Generator")
    introduction_print()
    print("'encode': Generate your QRCode.")
    print("'decode': Decrypte your QRCode image.")
    menu_choice = input("Enter your choice (encode, decode): ")
    if menu_choice == "encode":
        # Encode QRCode
        qrcode_content = input("Enter your Website link: ")
        qrcode_image_name = input("Enter a name for a QR Code image (whitout .png): ")
        qrcode_generator(qrcode_content, qrcode_image_name)
    elif menu_choice == "decode":
        # Decode QR Code
        decode_image_dir = input("Enter QRCode Image to Decode: ")
        qrcode_decoder(decode_image_dir)
    else:
        print("Error")
