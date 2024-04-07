import cv2

def load_and_resize_image(image_path, target_width, target_height):
    # 画像を読み込み、リサイズする
    img = cv2.imread(image_path)
    resized_img = cv2.resize(img, (target_width, target_height))
    return resized_img