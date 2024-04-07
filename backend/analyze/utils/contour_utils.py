import cv2

max_length = 900

def find_obeya_contours(frame):
    # 輪郭を検出する関数
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny_frame = cv2.Canny(gray_frame, 120,200)
    contours, _ = cv2.findContours(canny_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    obeya_contours = []
    for contour in contours:
        arc_length = cv2.arcLength(contour, True)
        if 100 < arc_length < max_length:
            obeya_contours.append(contour)
    return obeya_contours
