#/usr/bin/python3
from tkinter import Tk, Label, Frame, Button
from PIL import Image, ImageTk
WIDTH = 400
HEIGHT = 300
PATH = '/tmp/image.jpg'
import os, time
import picamera
import datetime

class App:
    def __init__(self):
        self.window = Tk()
        self.label = Label(master=self.window)
        self.photo = Button(master=self.window,
                        text="Photo",
                        command=self.take,
                        font=("Arial", 18), fg="blue" )
        self.shot = Button(master=self.window,
                        text="Film",
                        command=self.film,
                        font=("Arial", 18), fg="blue" )
        self.strandtest = Button(master=self.window,
                        text="Promenade",
                        command=os.system('sudo python3 /home/pi/Programm/Grafisch/strandtest.py'),
                        font=("Arial", 18), fg="red" )
        self.label.pack()
        self.run()
        self.photo.pack()
        self.shot.pack()
        self.strandtest.pack()
        self.window.mainloop()

    def take(self):
        with picamera.PiCamera() as camera:
            camera.start_preview()
            camera.framerate = 15
            time.sleep(5)
            i=datetime.datetime.now() 
            camera.capture('/home/pi/Pictures/%s.jpg' %i)
            camera.stop_preview()

    def film(self):
        with picamera.PiCamera() as camera:
            camera.start_preview()
            i=datetime.datetime.now()
            camera.framerate = 15
            camera.start_recording('/home/pi/Videos/%s.h264' %i)
            time.sleep(10)
            camera.stop_recording()
            camera.stop_preview()

    def takePhoto(self):
        with picamera.PiCamera() as camera:
            camera.framerate = 5
            camera.resolution = (500, 300)
            camera.capture('/tmp/image.jpg')
            img = Image.open('/tmp/image.jpg')
            self.image=ImageTk.PhotoImage(img)
            self.label.config(image=self.image)

    def run(self):
        self.takePhoto()
        time.sleep(0.1)
        self.window.after(100, self.run)

App()
