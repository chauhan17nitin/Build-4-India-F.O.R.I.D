from picamera import PiCamera
from time import sleep
from motion import motion
#from predict import Predict
#from servo import Servo

camera = PiCamera()
    
motion_obj = motion()

rows = 4
cols = 2
j=0
i=0
while(j<cols):
    i=0
    while(i<rows):
        if (j%2==0):
            motion_obj.forward()
            motion_obj.stop()
        else:
            motion_obj.reverse()
            motion_obj.stop()
            
        camera.start_preview()
        sleep(1)
        camera.capture('captured_img/'+str(j+1)+'_'+str(i+1)+'.jpg')
        camera.stop_preview()
        sleep(1)
        i+=1
    
    if (j%2==0):
        motion_obj.left()
        motion_obj.stop()
        motion_obj.forward()
        motion_obj.stop()
        motion_obj.right()
        motion_obj.stop()
    else:
        motion_obj.right()
        motion_obj.stop()
        motion_obj.forward()
        motion_obj.stop()
        motion_obj.left()
        motion_obj.stop()
        
    j+=1

camera.close()
#Servo()
#print(Predict())



