from qrcode import QRCode, constants
import  qrcode.image.svg
qr=QRCode(version=1,error_correction=constants.ERROR_CORRECT_L,box_size=20,border=2)

qr.add_data("https://www.instagram.com/p/C4H0NvnqTeF/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
qr.make(fit=True)

image=qr.make_image(fill_color='black',back_color='white')
image.save("qr.png")
factory=qrcode.image.svg.SvgPathImage
svg_img=qrcode.make("Hello World!",image_factory=factory)
svg_img.save("newqr.svg ")