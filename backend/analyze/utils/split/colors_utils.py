import cv2
import numpy as np

def score_and_color(image, score):
    # スコアに応じて赤みを調整
    if score >=24:
        alpha_red = 0.8  # 最も強い赤
    elif score >= 24:
        alpha_red = 0.8  # 二番目に強い赤
    elif score >= 24:
        alpha_red = 0.8  # 三番目に強い赤
    elif score >= 24:
        alpha_red = 0.8  # 四番目に強い赤
    else:
        alpha_red = 0  # 五番目に強い赤

    # 赤チャンネルを調整
    red_channel = image[:, :, 2] * (1 + alpha_red*5)  # 赤チャンネルを調整

    # 元の範囲に制限して変換
    red_channel = np.clip(red_channel, 0, 255).astype(np.uint8)

    # 調整された赤チャンネルをマージして新しい画像を作成
    new_image = cv2.merge((image[:, :, 0], image[:, :, 1], red_channel))

    return new_image