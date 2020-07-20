from picamera import PiCamera
import time
import cv2
import datetime
camera = PiCamera()
datetime_ = str(datetime.datetime.now())
font = cv2.FONT_HERSHEY_SIMPLEX
camera.vflip = True

def PI_photo(x):
    camera.start_preview()
    time.sleep(2)

    camera.capture('intruder%s.jpg',%x)
    print("the camera finished to take the photo")

    img = cv2.imread('intruder%s.jpg',1) #reading image
    img = cv2.putText(img, datetime_, (10,50), font, 1,(255,255,0), 1, cv2.LINE_AA) #if its an video you need to mange it like an image, frame by frame
    cv2.imshow('image', img) #showing the image
    camera.stop_preview()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
#dont forget to put x+=1    and x=1 above the func

        