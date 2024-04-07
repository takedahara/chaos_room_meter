import numpy as np

def merge_images(sub_images, rows, cols):
    # サブイメージの高さと幅を取得する
    sub_img_height, sub_img_width = sub_images[0].shape[:2]

    # 元の画像のサイズを計算する
    height = sub_img_height * rows
    width = sub_img_width * cols

    # 元の画像を初期化する
    merged_image = np.zeros((height, width, 3), dtype=np.uint8)

    # サブイメージを元の画像に配置する
    for i, sub_image in enumerate(sub_images):
        # サブイメージの行と列を計算する
        row_index = i // cols
        col_index = i % cols

        # サブイメージを元の画像に配置する
        merged_image[row_index * sub_img_height: (row_index + 1) * sub_img_height,
                     col_index * sub_img_width: (col_index + 1) * sub_img_width] = sub_image

    return merged_image