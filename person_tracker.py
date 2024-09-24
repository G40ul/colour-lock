import cv2
from src.color_detection import detect_color

def person_tracker_with_color_lock(video_source=0, color_lower_bound=None, color_upper_bound=None):
    # Load the webcam or video source
    cap = cv2.VideoCapture(video_source)
    
    # Initialize the tracker (e.g., KCF tracker for object tracking)
    tracker = cv2.TrackerKCF_create()
    initialized = False
    locked = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # If the tracker is initialized, update it
        if initialized:
            success, box = tracker.update(frame)
            if success:
                x, y, w, h = [int(v) for v in box]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Detect color in the tracking region
                tracking_frame = frame[y:y+h, x:x+w]
                color_detected, color_frame = detect_color(tracking_frame, color_lower_bound, color_upper_bound)

                if color_detected and not locked:
                    print("Color detected! Locking onto the target.")
                    locked = True

        # If tracker is not initialized, select the bounding box manually
        if not initialized:
            bbox = cv2.selectROI("Frame", frame, False)
            tracker.init(frame, bbox)
            initialized = True

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
