import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
from datetime import date
from datetime import datetime
date = date.today()
now = datetime.now()
time = now.strftime("%I:%M:%S %p")
global fontv
global updatevar
updatevar = 0
fontv = "Arial"
fs1 = (30)
fs2 = (20)
fs3 = (10)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def setwin():
    a = Toplevel()
    a.geometry('800x600+0+0')
    a.title("Settings | Clock")
    a.iconbitmap('clock.ico')

    fontwinb=Button(a, text='Fonts', font = ((fontv), (fs3)), command = fwin)
    fontwinb.pack()
    fswinb=Button(a, text='Font Sizes', font = ((fontv), (fs3)), command = fswin)
    fswinb.pack()

    global updatevar
    def update():
        fontwinb.configure(font = ((fontv), (fs3)))
        fswinb.configure(font = ((fontv), (fs3)))
        fontwinb.pack()
        fswinb.pack()
        a.after(10, update)

    if(updatevar) == (0):
        update()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def fwin():
    b = Toplevel()
    b.geometry('800x600+0+0')
    b.title('Settings - Fonts | Clock')
    b.iconbitmap('clock.ico')

    def fontset(font):
        global fontv
        fontv = (f"{font}")

    fontl=Label(b, text='Preset Fonts', font = ((fontv), (fs2)))
    fontl.pack()

    fontab=Button(b, text='Arial', font = ('Arial', (fs3)), command =lambda: fontset("Arial"))
    fontab.pack()
    fontbb=Button(b, text='Times New Roman', font = ('Times New Roman', (fs3)), command =lambda: fontset("Times New Roman"))
    fontbb.pack()
    fontcb=Button(b, text='Terminal', font = ('Terminal',(fs3)), command =lambda: fontset("Terminal"))
    fontcb.pack()

    testtext=Label(b, text='The quick brown fox jumped over the lazy dog.', font = ((fontv), (fs2)))
    testtext.pack()

    global updatevar
    def update():
        fontl.configure(font = ((fontv), (fs2)))
        fontab.configure(font = (('Arial'), (fs3)))
        fontbb.configure(font = (('Times New Roman'), (fs3)))
        fontcb.configure(font = (('Terminal'), (fs3)))
        testtext.configure(font = ((fontv), (fs2)))
        testtext.pack()
        fontl.pack()
        fontab.pack()
        fontbb.pack()
        fontcb.pack()
        b.after(10, update)

    if(updatevar) == (0):
        update()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def fswin():
    c = Toplevel()
    c.geometry('800x600+0+0')
    c.title('Settings - Font Sizes | Clock')
    c.iconbitmap('clock.ico')

    def fs1set(size):
        global fs1
        fs1 = (f"{size}")
    def fs2set(size2):
        global fs2
        fs2 = (f"{size2}")
    def fs3set(size3):
        global fs3
        fs3 = (f"{size3}")

    fsl=Label(c, text="Preset Font Sizes", font = ((fontv), (fs2)))
    fsl.pack()

    fs11b=Button(c, text="Type One, Size One", font = ((fontv), (15)), command =lambda: fs1set(15))
    fs11b.pack()
    fs12b=Button(c, text="Type One, Size Two", font = ((fontv), (30)), command =lambda: fs1set(30))
    fs12b.pack()
    fs13b=Button(c, text="Type One, Size Three", font = ((fontv), (45)), command =lambda: fs1set(45))
    fs13b.pack()
    fs21b=Button(c, text="Type Two, Size One", font = ((fontv), (10)), command =lambda: fs2set(10))
    fs21b.pack()
    fs22b=Button(c, text="Type Two, Size Two", font = ((fontv), (20)), command =lambda: fs2set(20))
    fs22b.pack()
    fs23b=Button(c, text="Type Two, Size Three", font = ((fontv), (35)), command =lambda: fs2set(35))
    fs23b.pack()
    fs31b=Button(c, text="Type Three, Size One", font = ((fontv), (5)), command =lambda: fs3set(5))
    fs31b.pack()
    fs32b=Button(c, text="Type Three, Size Two", font = ((fontv), (10)), command =lambda: fs3set(10))
    fs32b.pack()
    fs33b=Button(c, text="Type Three, Size Three", font = ((fontv), (25)), command =lambda: fs3set(25))
    fs33b.pack()

    global updatevar
    def update():
        fsl.configure(font = ((fontv), (fs2)))
        fs11b.configure(font = ((fontv), (15)))
        fs12b.configure(font = ((fontv), (30)))
        fs13b.configure(font = ((fontv), (45)))
        fs21b.configure(font = ((fontv), (10)))
        fs22b.configure(font = ((fontv), (20)))
        fs23b.configure(font = ((fontv), (35)))
        fs31b.configure(font = ((fontv), (5)))
        fs32b.configure(font = ((fontv), (10)))
        fs33b.configure(font = ((fontv), (25)))
        fsl.pack()
        fs11b.pack()
        fs12b.pack()
        fs13b.pack()
        fs21b.pack()
        fs22b.pack()
        fs23b.pack()
        fs31b.pack()
        fs32b.pack()
        fs33b.pack()
        c.after(10, update)
    if(updatevar) == (0):
        update()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

###########################################################################
w = tk.Tk()
w.title('Clock')
w.geometry('1024x768+0+0')
w.minsize(320, 240)
w.maxsize(3840, 2160)
w.iconbitmap('clock.ico')
time_str = (now.strftime("%H:%M:%S"))

timel=Label(w, text=(time_str), font = ((fontv), (fs1)))
timel.pack()

datel=Label(w, text=(date), font = ((fontv), (fs2)))
datel.pack()

exitb=Button(w, text="Exit", font = ((fontv), (fs3)), command = w.destroy)
exitb.pack()
exitb.place(x = (0), y = (0))

setb=Button(w, text="Settings", font = ((fontv), (fs3)), command = setwin)
setb.pack()
setb.place(x = 0 + exitb.winfo_width(), y = 0)

def conf_timel():
    global fontv
    now = (datetime.now())
    time_str = (now.strftime("%I:%M:%S %p"))
    timel.configure(text=(time_str), font = ((fontv), (fs1)))
    timel.pack()
    timelh = (timel.winfo_height())
    timely = (timel.winfo_rooty())
    timel.place(x = w.winfo_width() / 2 - timel.winfo_width() / 2, y = w.winfo_height() / 2 - timel.winfo_height() / 2)

def conf_datel():
    datel.configure(text=(date), font = ((fontv), (fs2)))
###########################################################################
def update():
    conf_timel()
    conf_datel()
    exitb.configure(font = ((fontv), (fs3)))
    setb.configure(font = ((fontv), (fs3)))
    setb.place(x = 0 + exitb.winfo_width(), y = 0)
    w.after(10, update)
    
if(updatevar) == (0):
    update()

mainloop()
