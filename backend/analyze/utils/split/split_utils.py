import cv2

def split_image(image, rows, cols):

    # 画像の高さと幅を取得する
    height, width = image.shape[:2]

    # 分割後の各サブイメージの高さと幅を計算する
    sub_img_height = height // rows
    sub_img_width = width // cols

    # 分割されたイメージを保存するためのリストを作成する
    sub_images = []

    # 画像を行と列に分割する
    for y in range(0, height, sub_img_height):
        for x in range(0, width, sub_img_width):
            # サブイメージを取得する
            sub_image = image[y:y+sub_img_height, x:x+sub_img_width]
            sub_images.append(sub_image)

    #下のはテスト
    # for i, sub_image in enumerate(sub_images):
    #     cv2.imshow(f'Sub Image {i+1}', sub_image)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return sub_images
    

