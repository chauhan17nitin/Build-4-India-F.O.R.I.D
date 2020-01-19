import RPi.GPIO as GPIO
from time import sleep

class motion(): 
    def __init__(self): 
        
        #GPIO.setmode(GPIO.BOARD)
     
        self.IN1 = 16
        self.IN2 = 18
        self.IN3 = 22
        self.IN4 = 24   
        self.ENA = 13
        self.ENB = 15 

        GPIO.setwarnings(False)

        GPIO.setup(self.IN1,GPIO.OUT)
        GPIO.setup(self.IN2,GPIO.OUT)
        GPIO.setup(self.IN3,GPIO.OUT)
        GPIO.setup(self.IN4,GPIO.OUT)
        GPIO.setup(self.ENA,GPIO.OUT)
        GPIO.setup(self.ENB,GPIO.OUT) 
    
    def reverse(self):

        print ("REVERSE MOTION")
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
        #GPIO.output(ENA,GPIO.HIGH)
        #GPIO.output(ENB,GPIO.LOW)
        sleep(0.5)

    def forward(self):
        print ("FORWARD TURN")
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.HIGH)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
        #GPIO.output(ENA,GPIO.HIGH)
        #GPIO.output(ENB,GPIO.HIGH)
        sleep(0.65)
        #GPIO.cleanup()
        

    def right(self):
        print("RIGHT TURN")
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.HIGH)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
        #GPIO.output(ENA,GPIO.HIGH)
        #GPIO.output(ENB,GPIO.LOW)
        sleep(1)

    def left(self):
        print("LEFT TURN")
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
        #GPIO.output(ENA,GPIO.LOW)
        #GPIO.output(ENB,GPIO.HIGH)
        sleep(1)

    def stop(self):
            
        print ("STOP")
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.LOW)
        sleep(3)
    #GPIO.cleanup()



