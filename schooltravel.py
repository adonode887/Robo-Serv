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


in1 = 24
in2 = 23
in3 = 17
in4 = 27
ena = 25
enb = 22

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

p.start(20)
q.start(20)

text = "Hello. My name is Robo-Server."
engine.say(text)
# play the speech
engine.runAndWait()

GPIO.output (in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)
GPIO.output (in3, GPIO.HIGH)
GPIO.output(in4, GPIO.LOW)
text = "I am a robot programmed to deliver items."
engine.say(text)
# play the speech
engine.runAndWait()
p.ChangeDutyCycle(50)
q.ChangeDutyCycle(0)
sleep(1)
GPIO.output (in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)
GPIO.output (in3, GPIO.LOW)
GPIO.output(in4, GPIO.HIGH)
p.ChangeDutyCycle(20)
q.ChangeDutyCycle(20)
text = "I can also do other tasks of carrying objects."
engine.say(text)
# play the speech
engine.runAndWait()
GPIO.output (in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)
GPIO.output (in3, GPIO.HIGH)
GPIO.output(in4, GPIO.LOW)
p.ChangeDutyCycle(0)
q.ChangeDutyCycle(50)
sleep(1)
p.ChangeDutyCycle(20)
q.ChangeDutyCycle(20)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.cleanup
text = "Thank you for watching and listening."
engine.say(text)
# play the speech
engine.runAndWait()