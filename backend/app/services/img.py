import cv2
import numpy as np
import io
import uuid
import base64
import os



def read_image(bin_data, size=(256, 256)):
    """画像を読み込む

    Arguments:
        bin_data {bytes} -- 画像のバイナリデータ

    Keyword Arguments:
        size {tuple} -- リサイズしたい画像サイズ (default: {(224, 224)})

    Returns:
        numpy.array -- 画像
    """
    file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, size)
    return img

def save_icon_imag(
    imag: str,
    old_path: str
):
    bin_data = io.BytesIO(base64.b64decode(imag))
    re_imag = read_image(bin_data)
    path = './food/' + str(uuid.uuid4()) + '.jpg' 
    cv2.imwrite(path, re_imag)
    return path

def change_imag_to_base64(
    path: str
):
    b64_img = ""
    with open(path, 'br') as f:
        b64_img = base64.b64encode(f.read())
    return b64_img