import hs_sr04
import time
import mail
import PI_cam
import sound

if __name__ == '__main__':
    try:
        x=1
        while True:
            dist = hs_sr04.distance()
            print ("Measured Distance = %.1f cm" % dist)
            if dist < 50:
                sound.soundd()
                PI_cam.PI_camera_en(x)
                x += 1
                if PI_cam.PI_camera_en(x):
                    print("now you need to get the mail and sms")
                    mail.mail_sender()
            time.sleep(1)
 
    #Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        PI_cam.camera.close()
