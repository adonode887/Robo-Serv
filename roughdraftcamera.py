import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import RPi.GPIO as GPIO          
from time import sleep
import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)  # Adjust 'new_rate' to desired speech rate
voices = engine.getProperty('voices')  # Get a list of available voices
# Set a different voice by changing the index
engine.setProperty('voice', voices[2].id)  # Adjust 'index' to select a different voice

# ... (GPIO setup for motors)
in1 = 24
in2 = 23
in3 = 17
in4 = 27
ena = 25
enb = 22
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(ena,500)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
q=GPIO.PWM(enb,500)

p.start(50)
q.start(50)
# convert this text to speech
text = "My name is Robo-Server, and I am ready to assist delivering items."
engine.say(text)
# play the speech
engine.runAndWait()

# Motor control setup functions (adjust as per your hardware setup)
def move_forward(speed):
    # Code to move the robot forward
    p.ChangeDutyCycle(50)
    q.ChangeDutyCycle(50)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    temp1=1

def move_backward(speed):
    # Code to move the robot backward
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    temp1=0

def turn_left(speed):
    # Adjust GPIO pins for left turn
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    p.ChangeDutyCycle(10)  # Adjust the speed as needed
    q.ChangeDutyCycle(50)  # Adjust the speed as needed
    sleep(0.05)  # Adjust the duration of the turn

def turn_right(speed):
    # Adjust GPIO pins for right turn
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    p.ChangeDutyCycle(50)  # Adjust the speed as needed
    q.ChangeDutyCycle(10)  # Adjust the speed as needed
    sleep(0.05)  # Adjust the duration of the turn

def stop_motors():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

# Initialize PiCamera
camera = PiCamera()
camera.resolution = (1920, 1080)
raw_capture = PiRGBArray(camera, size=(1920, 1080))
# Allow the camera to warm up
sleep(0.25)

text = "Starting delivery."
engine.say(text)
# play the speech
engine.runAndWait()

# Path following algorithm
frame_width = 1920  # Width of the camera frame
center_threshold = 30  # Adjust this threshold as needed

# Continuously capture frames and perform path detection
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame.array, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image (adjust threshold value as needed)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   # Assuming you've detected contours, implement path-following logic
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        # Get centroid and implement path-following logic based on centroid

        # Example: Calculate centroid
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            # Your path following logic goes here, adjusting motors based on the centroid
            if cx < (frame_width // 2 - center_threshold):
                turn_left(50)  # Adjust speed as needed
                print ("turning left")
            elif cx > (frame_width // 2 + center_threshold):
                turn_right(50)  # Adjust speed as needed
                print ("turning right")
            else:
                move_forward(50)
                print ("going forward")  # Adjust speed as needed
        else:
            # No centroid found, stop the motors or take appropriate action
            stop_motors()
    else:
        # No path detected, stop the motors or take appropriate action
        stop_motors()

    cv2.imshow("Path Detection", binary)
    # Show the binary image for visualization
    raw_capture.truncate(0)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
            # Stop the motors before exiting
            # stop_motors()
        break

# Clean up resources
cv2.destroyAllWindows()
# Release resources, GPIO cleanup, etc.
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
text = "Delivery over."
engine.say(text)
# play the speech
engine.runAndWait()
print("Done!")
GPIO.cleanup
