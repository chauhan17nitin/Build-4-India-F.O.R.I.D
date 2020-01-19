from picamera import PiCamera
from time import sleep
from motion import motion
from predict import Predict
from servo import Servo

camera = PiCamera()
    
motion_obj = motion()

rows = 4
cols = 2
j=0
i=0
while(j<cols):
    i=0
    while(i<rows):
        motion_obj.forward()
        motion_obj.stop()
        camera.start_preview()
        sleep(1)
        camera.capture('captured_img/'+str(j+1)+'_'+str(i+1)+'.jpg')
        camera.stop_preview()
        sleep(1)
        i+=1
    
    print('take the turn')
    j+=1
Servo()
print(Predict())



