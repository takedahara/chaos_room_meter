import base64

def b64_image(image):
    # Base64エンコードして文字列として返す
    return base64.b64encode(image).decode('utf-8')
