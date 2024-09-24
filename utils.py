import cv2

def draw_bounding_box(frame, box, color=(0, 255, 0)):
    x, y, w, h = [int(v) for v in box]
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    return frame
