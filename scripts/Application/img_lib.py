# coding: UTF-8

import base64
from io import BytesIO

from PIL import Image

class ImgLib:
    @classmethod
    def getBase64fromPath(cls, path : str ):
        # file open
        img = Image.open(path)
        # convert image -> base64
        data = pil_to_base64(img, format="png")
        # file close
        img.close()
        return data

    @classmethod
    def saveImageFromBase64(cls, data : str, path : str ) :
        img = base64_to_pil(data)
        img.save(path)
        pass

def pil_to_base64( img : Image, format = "png" ) -> str :
    buffer = BytesIO()
    img.save(buffer, format)
    img_str = base64.b64encode( buffer.getvalue() ).decode("ascii")
    
    return img_str

def base64_to_pil( data : str ) -> Image :
    if "base64," in data :
        # DATA URI の場合、data:[<mediatype>][;base64], を除く
        data = data.split(",")[1]
    imgRaw = base64.b64decode(data)
    img = Image.open( BytesIO(imgRaw) )
    return img
