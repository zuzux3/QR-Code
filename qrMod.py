import segno
from PIL import Image
import io

def qr(string: str):
    qrCode = segno.make_qr(string)
    out = io.BytesIO()
    qrCode.save(out, scale=5, kind='png')
    out.seek(0)
    img = Image.open(out)
    
    return img

test = qr('test')
test.show()