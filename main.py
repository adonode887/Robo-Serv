
import RPi.GPIO as GPIO          
from time import sleep

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

p.start(20)
q.start(20)
print("\n")
print("The default speed & direction of motor is fast & forward")
print("g-go n-no w-forward s-backward f-fast ff-faster fff-fastest b-Nitro! l-left r-right e-exit")
print("There is a secret command that turns this car to it's max potential!")
print("\n")    

while(1):

    x=raw_input()
    if x=='g':
        print("go")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='n':
        print("no")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='w':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='s':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'
        
    elif x=='a':
        print("left")
        p.ChangeDutyCycle(1)
        q.ChangeDutyCycle(1)
        sleep(0.25)
        p.ChangeDutyCycle(0)
        q.ChangeDutyCycle(25)
 	sleep(1)
	p.ChangeDutyCycle(25)
	q.ChangeDutyCycle(25)
        p.ChangeDutyCycle(10)
        q.ChangeDutyCycle(10)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        p.ChangeDutyCycle(20)
        q.ChangeDutyCycle(20)
        x='z'
    
    elif x=='d':
        print("right")
        p.ChangeDutyCycle(1)
        q.ChangeDutyCycle(1)
        sleep(0.25)
        p.ChangeDutyCycle(25)
        q.ChangeDutyCycle(0)
	sleep(1)
	p.ChangeDutyCycle(25)
        q.ChangeDutyCycle(25)
        p.ChangeDutyCycle(10)
        q.ChangeDutyCycle(10)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        p.ChangeDutyCycle(20)
        q.ChangeDutyCycle(20)
        x='z'

    elif x=='f':
        print("fast")
        p.ChangeDutyCycle(20)
        q.ChangeDutyCycle(20)
        x='z'

    elif x=='ff':
        print("Faster")
        p.ChangeDutyCycle(25)
        q.ChangeDutyCycle(25)
        x='z'

    elif x=='fff':
        print("FASTEST")
        p.ChangeDutyCycle(50)
        q.ChangeDutyCycle(50)
        x='z'
    elif x=='b':
        print ("Nitro Boost!")
        p.ChangeDutyCycle(75)
        q.ChangeDutyCycle(75)
        x='z'
    elif x=='AAA':
        print ("AAAAAAAAAAAAAAA! Secret command found!")
        p.ChangeDutyCycle(100)
        q.ChangeDutyCycle(100)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        print("End")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
