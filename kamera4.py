#/usr/bin/python3
from tkinter import * #Tk, Label, Frame, Button
from PIL import Image, ImageTk
WIDTH = 400
HEIGHT = 300
PATH = '/tmp/image.jpg'
import os, time
import picamera
import datetime
from io import BytesIO

class App:
    def __init__(self):
        self.window = Tk()
        self.window.configure(background='white')
        self.window.title("Kamera")
        self.window.geometry("550x400")
        self.label = Label(master=self.window)
        self.photo = Button(master=self.window,
                        text="Photo",
                        command=self.take,
                        font=("Arial", 18), fg="blue" )
        self.shot = Button(master=self.window,
                        text="Film 30s",
                        command=self.film,
                        font=("Arial", 18), fg="blue" )
        self.show = Button(master=self.window,
                        text="Zeige Film",
                        command=self.play,
                        font=("Arial", 18), fg="blue" )
        self.label.pack(anchor=N)
        self.run()
        self.photo.pack(anchor=S)
        self.shot.pack(anchor=S)
        self.show.pack(anchor=S)
        self.window.mainloop()

    def take(self):
        with picamera.PiCamera() as camera:
            camera.start_preview()
            camera.framerate = 30
            time.sleep(5)
            i=datetime.datetime.now() 
            camera.capture('/home/pi/Pictures/%s.jpg' %i)
            camera.stop_preview()

    def film(self):
        with picamera.PiCamera() as camera:
            self.shot.config(state='disabled')
            camera.start_preview()
            camera.start_recording('/home/pi/Videos/video.h264')
            time.sleep(30)
            camera.stop_recording()
            camera.stop_preview()
            self.shot.config(state='normal')

    def play(self):
        os.system('omxplayer /home/pi/Videos/video.h264')

    def takePhoto(self):
        with picamera.PiCamera() as camera:
            camera.framerate = 5
            camera.resolution = (500, 250)
            camera.capture('/tmp/image.jpg')
            img = Image.open('/tmp/image.jpg')
            self.image=ImageTk.PhotoImage(img)
            self.label.config(image=self.image)

    def run(self):
        self.takePhoto()
        time.sleep(0.1)
        self.window.after(100, self.run)

App()
