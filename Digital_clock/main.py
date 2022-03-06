from tkinter import *
from time import strftime

window = Tk()
window.title("My Clock")
window.geometry("800x300")
window.resizable(False,False)
window.config(bg='black')

def clock_date():
    display_date = strftime('%A %B %d %Y')
    Date.config(text=display_date)
    Date.after(1000,clock_date)

def clock_Time():
    display_time = strftime('%H:%M:%S %p')
    Time.config(text=display_time)
    Time.after(1000,clock_Time)

Date = Label(window,font=('ds-digital',20),background='black',foreground='white')
Date.pack(anchor= 'center')
Date.config(padx=(75),pady= (30))
Time = Label(window,font=('ds-digital',80),background='black',foreground='white')
Time.pack(anchor= 'center')
Time.config(padx=(50))

clock_date()
clock_Time()
mainloop()
