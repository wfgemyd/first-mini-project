from picamera import PiCamera
import time
camera = PiCamera()

def PI_camera_en(x):
    camera.vflip = True 
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/project/vivi%s.h264'%x)
    time.sleep(2)
    camera.stop_recording()
    print("the camera finished to take the vid")
    camera.capture('/home/pi/Desktop/project/indruder%s.jpg'%x)
    print("the camera finished to take the photo")
    camera.stop_preview()
    return True

#dont forget to put x+=1    and x=1 above the func