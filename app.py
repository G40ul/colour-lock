import cv2
from src.person_tracker import person_tracker_with_color_lock

def main():
    print("Starting Person Tracking with Color Lock System")
    
    # Define the color to detect (example: blue color in HSV)
    blue_lower = (100, 150, 0)   # HSV lower bound for blue
    blue_upper = (140, 255, 255) # HSV upper bound for blue

    # Start the tracking process from webcam (you can change to a video file by passing a file path instead of 0)
    person_tracker_with_color_lock(0, blue_lower, blue_upper)

if __name__ == "__main__":
    main()
