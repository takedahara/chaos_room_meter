# image_encoder.py

import base64

# 画像ファイルをBase64にエンコードする
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string
