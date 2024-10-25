# import cv2
# import time
# video = cv2.VideoCapture(0)
# # Attempt to open the video capture
# while True:
#     time.sleep(1)
#     check, frame = video.read()
#     cv2.imshow("My viedo",frame)

#     key = cv2.waitKey(1)

#     if key == ord("q"):
#         break
# video.release()


import cv2
import time

# Open the video capture
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if the video capture opened successfully
if not video.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    time.sleep(1)  # Sleep for 1 second
    check, frame = video.read()

    # Check if the frame was captured correctly
    if not check or frame is None or frame.size == 0:
        print("Error: Could not read frame.")
        break

    cv2.imshow("My Video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

# Release the video capture and destroy all windows
video.release()
cv2.destroyAllWindows()
