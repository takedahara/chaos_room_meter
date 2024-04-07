import sys
import os
import json
from utils.image_utils import load_and_resize_image
from utils.contour_utils import find_obeya_contours
from utils.scoring_utils import calculate_obeya_score
from utils.ranking_utils import rank_obeya_score
from utils.display_utils import display_obeya_score
from utils.split.split_utils import split_image
from utils.split.synthesis_utils import merge_images
from utils.split.colors_utils import score_and_color
from utils.base64_utils import b64_image

target_width = 1000
target_height = 600
split_rows = 5
split_cols = 5

def process_image(image_path):
    # 画像を読み込み、リサイズする
    resized_img = load_and_resize_image(image_path, target_width, target_height)

    # 画像を分割する
    split_images = split_image(resized_img, split_rows, split_cols)

    scores_list = []
    color_images = []
    for sub_image in split_images:
        # OBEYA 輪郭を検出する
        sub_contours = find_obeya_contours(sub_image)

        # OBEYA スコアを計算する
        sub_score = calculate_obeya_score(sub_contours)

        # 分割画像のリストにスコアを追加する
        scores_list.append(sub_score)

        # OBEYA部分の表示
        color_images.append(score_and_color(sub_image, sub_score))

    # 分割画像を再構築する
    image = merge_images(color_images, split_rows, split_cols)

    # OBEYA 輪郭を検出する
    obeya_contours = find_obeya_contours(resized_img)

    # OBEYA スコアを計算する
    score = calculate_obeya_score(obeya_contours)

    # OBEYA スコアに基づいてランク付けを行う
    rank = rank_obeya_score(score)

    # 画像を表示する
    result_image = display_obeya_score(image, obeya_contours, score, rank)

    # 画像をBase64エンコードする
    b64_result_image = b64_image(result_image)

    # 処理結果をJSON形式で返す
    return json.dumps({"image": b64_result_image, "score": score, "sub_scores": scores_list})

# サーバーから呼び出された場合の処理
if __name__ == "__main__":
    # コマンドライン引数から画像ファイルのパスを取得する
    if len(sys.argv) != 2:
        print("Usage: python obeya.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]

    # 画像を処理し、結果を取得する
    result = process_image(image_path)

    # 結果を出力する
    print(result)


