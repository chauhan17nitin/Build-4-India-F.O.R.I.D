from picamera import PiCamera
from time import sleep

def Capture():
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture('image.jpg')
    camera.stop_preview()
