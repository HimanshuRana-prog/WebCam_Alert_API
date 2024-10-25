import cv2

# Attempt to open the video capture
viedo = cv2.VideoCapture(0, cv2.CAP_DSHOW)
check, frame = viedo.read()

print(check)
print(frame)
# import cv2

# # Attempt to open the video capture
# # video = cv2.VideoCapture(0)

# # if not video.isOpened():
# #     print("Error: Could not open video.")
# # else:
# #     check, frame = video.read()
# #     print(check)  # Should be True if frame was read successfully
# #     print(frame)  # Should not be None if frame was read

# # video.release()
# # cv2.destroyAllWindows()
