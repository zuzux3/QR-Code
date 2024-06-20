import segno

def qr(string: str):
    qrCode = segno.make_qr(string)
    qrCode.save(f'{string}_QR_Code.png')