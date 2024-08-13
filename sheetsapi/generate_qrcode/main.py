import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def generate_qrcode(name):
    """
    Generates a QR code for the given name
    """
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    name = name.replace(" ", "-").lower()
    qr.add_data(f'http://192.168.1.236:5000/{name}')

    img = qr.make_image(image_factory=StyledPilImage,
                        color_mask=RadialGradiantColorMask(back_color=(
                            255, 255, 255), center_color=(158, 164, 229), edge_color=(23, 34, 166)),
                        embeded_image_path="./generate_qrcode/logo.png")
    img_file = f"./generate_qrcode/qrcode_{name}.png"
    img.save(img_file)
    return img_file
