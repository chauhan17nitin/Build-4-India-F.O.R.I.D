from picamera import PiCamera
from time import sleep

def capture():
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture('image.jpg')
    camera.stop_preview()
