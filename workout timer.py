from tkinter import *
import tkinter.font as font
import threading
import time

# 20 Minutes

wait = 1800 


def alert_popup():
    root = Tk()
    root.title("EXERCISE TIME!")

    w = 1000     # popup window width
    h = 600     # popup window height

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    m = "12 Curls \n 12 Shoulder Press \n 20 Push ups \n 20 Chair Crunches \n\n NOW!!"
    m += '\n'

    myfont = font.Font(size=30)
    
    w = Label(root, text=m, width=120, height=10)
    w['font'] = myfont
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    mainloop()

    threading.Timer(wait, alert_popup).start()
    
alert_popup()

