from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor

camera = PiCamera()
pir = MotionSensor(4)

pir.wait_for_motion()
camera.start_preview(alpha=192)
sleep(5)
camera.capture("/home/pi/photos/motion.jpg")


#for i in range(5):
#    print (i)
#    sleep(5)
#    camera.capture("/home/pi/photos/image{}.jpg".format(i))

camera.stop_preview
camera.close()