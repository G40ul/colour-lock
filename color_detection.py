import cv2
import numpy as np

def detect_color(frame, lower_bound, upper_bound):
    # Convert the image to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a binary mask where the color within the range will be white, and the rest will be black
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    
    # Use the mask to extract the color part of the image
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Check if the color is detected by counting non-zero pixels in the mask
    color_detected = np.count_nonzero(mask) > 0
    
    return color_detected, result
