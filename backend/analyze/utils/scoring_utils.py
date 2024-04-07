from collections import deque
from statistics import median
import math
import cv2

def calculate_obeya_score(contours):
    # OBEYA スコアを計算する関数
    score_queue = deque([])
    total_arc_length = sum(cv2.arcLength(contour, True) for contour in contours)
    score_queue.append(math.floor(total_arc_length / 100))
    if len(score_queue) > 30:
        score_queue.popleft()

    score = median(score_queue)
    return score
