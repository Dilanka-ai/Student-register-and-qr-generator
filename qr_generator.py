import qrcode

class QR_generator:
    def __init__(self, qr_text, qr_file):
        self.qr_text = qr_text
        self.qr_file = qr_file
        
    def generate_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.qr_text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.qr_file)