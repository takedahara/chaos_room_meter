import cv2

FONT = cv2.FONT_HERSHEY_SIMPLEX
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
ORANGE = (0, 130, 255)
SCORE_AP = (0, 80)
SCORE_FONT_SIZE = 2
SCORE_FONT_WEIGHT = 8

def display_obeya_score(resized_img, obeya_contours, score, rank):
    score_frame = resized_img.copy()

    for contour in obeya_contours:
        cv2.drawContours(score_frame, [contour], -1, GREEN, 3)

    # cv2.putText(score_frame, ' '.join([str(score), rank]), SCORE_AP, FONT, SCORE_FONT_SIZE, BLUE, SCORE_FONT_WEIGHT, cv2.LINE_AA)

    # 画像を表示
    # cv2.imshow('OBEYA Score', score_frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return score_frame
