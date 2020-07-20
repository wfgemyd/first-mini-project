import os

def soundd():
    file = "/home/pi/Desktop/project/xxx.mp3"
    os.system("mpg123 " + file)
    
soundd()
    
    