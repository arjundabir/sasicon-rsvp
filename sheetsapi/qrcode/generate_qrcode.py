import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def generate_qrcode():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    # change this to the url of the flask server
    qr.add_data('http://192.168.1.236:5000')

    img_3 = qr.make_image(image_factory=StyledPilImage,
                          color_mask=RadialGradiantColorMask(back_color=(
                              255, 255, 255), center_color=(158, 164, 229), edge_color=(23, 34, 166)),
                          embeded_image_path="logo.png")

    img_3.save("qr_with_logo.png")
