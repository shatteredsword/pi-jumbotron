#!/usr/bin/env python3
import gi
from tkinter import *
from tkinter import ttk
from tkinter import font
from picamera import PiCamera
import time
import datetime
import sys

global camera
global endTime1
global endTime2
global endTime3
global endTime4
global timerLength
global startTime1
global startTime2
global startTime3
global startTime4

def quit(*args):
    root.destroy()

def show_time():
    now = datetime.datetime.now()
    now = now - datetime.timedelta(microseconds=now.microsecond)
    if now == startTime1 or now == startTime2 or now == startTime3 or now == startTime4:
        camera.stop_preview()
    elif now == endTime1 or now == endTime2 or now == endTime3 or now == endTime4:
        time.sleep(10)
        camera.start_preview()
    elif now > startTime1 and now < endTime1:
        txt.set(endTime1 - now - fix)
    elif now > startTime2 and now < endTime2:
        txt.set(endTime2 - now - fix)
    elif now > startTime3 and now < endTime3:
        txt.set(endTime3 - now - fix)
    elif now > startTime4 and now < endTime4:
        txt.set(endTime4 - now - fix)

    # Trigger the countdown after 1000ms
    root.after(1000, show_time)

# Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("x", quit)
root.after(0, show_time)
endTime1 = datetime.datetime(2018, 11, 17, 18, 30, 0)
endTime2 = datetime.datetime(2018, 11, 17, 18, 40, 0)
endTime3 = datetime.datetime(2018, 11, 17, 18, 50, 0)
endTime4 = datetime.datetime(2018, 11, 17, 19, 0, 0)
timerLength = datetime.timedelta(minutes=5)
fix = datetime.timedelta(seconds=1)
startTime1 = endTime1 - timerLength
startTime2 = endTime2 - timerLength
startTime3 = endTime3 - timerLength
startTime4 = endTime4 - timerLength
camera = PiCamera()
camera.start_preview()
fnt = font.Font(family='Helvetica', size=200, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
