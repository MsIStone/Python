from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=192)
#sleep(5)
#camera.capture("/home/pi/photos/image1.jpg")


for i in range(5):
    print (i)
    sleep(5)
    camera.capture("/home/pi/photos/image{}.jpg".format(i))

camera.stop_preview
camera.close()