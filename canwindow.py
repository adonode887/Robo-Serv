import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

# Initialize PiCamera
camera = PiCamera()
camera.resolution = (1920, 1080)  # Adjust resolution to match your camera
camera.framerate = 30  # Set the frame rate to 60fps
raw_capture = PiRGBArray(camera, size=(1920, 1080))

# Allow the camera to warm up
time.sleep(0.1)

# Open a window to display the camera feed
cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    # Grab the raw NumPy array representing the image
    image = frame.array

    # Display the image in the window
    cv2.imshow("Camera Feed", image)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Clear the stream for the next frame
    raw_capture.truncate(0)

# Release resources
cv2.destroyAllWindows()
