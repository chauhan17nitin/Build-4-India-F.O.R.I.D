#import RPi.GPIO as GPIO
from time import sleep
from motion import motion
#from capture import capture
#from predict import predict

	
motion_obj = motion()
motion_obj.forward()
motion_obj.stop()
#capture()
motion_obj.forward()
motion_obj.stop()
motion_obj.forward()
motion_obj.stop()
motion_obj.forward()
motion_obj.stop()
#capture()
#motion_obj.forward()
#motion_obj.stop()

#motion_obj.right()
#motion_obj.stop()

#motion_obj.left()
#motion_obj.stop()

#motion_obj.reverse()
#motion_obj.stop()



#print(predict())



