from threading import Thread
import tkinter as t
from tkinter.ttk import *
from datetime import datetime
import time
from pygame import mixer
from tkinter import messagebox
from PIL import ImageTk, Image

window = t.Tk() # initializes tkinter to create display window
window.title("Alarm Clock") # gives the window a title
window.geometry('500x250') # width and height of the window
photo=t.PhotoImage(file='icon_clock.png') #icon image
window.iconphoto(False,photo)
selected = t.IntVar()

tabs_control = Notebook(window) #create 3tabs
clock_tab = Frame(tabs_control)
alarm_tab = Frame(tabs_control)
timer_tab = Frame(tabs_control)

#several tabs
tabs_control.add(clock_tab, text="Clock")
tabs_control.add(alarm_tab, text="Alarm")
tabs_control.add(timer_tab, text="Countdown timer")
tabs_control.pack(expand = 1, fill ="both")

def clock():
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date, time1 = date_time.split()
    time2, time3 = time1.split('/')
    hour, minutes, seconds = time2.split(':')
    if int(hour) > 12 and int(hour) <= 24:
        time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
    else:
        time = time2 + ' ' + time3
    time_label.config(text=time)
    date_label.config(text=date)
    time_label.after(1000, clock)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('Deactivated alarm: ', selected.get())
    mixer.music.stop()
rad1 = Radiobutton(alarm_tab, text = "Activate", command=activate_alarm, variable=selected)
rad1.place(x = 250, y=95)

def sound_alarm():
    mixer.music.load('dance.wav')
    mixer.music.play()
    selected.set(0)

    rad2 = Radiobutton(alarm_tab, text = "Deactivate", command=deactivate_alarm, variable=selected)
    rad2.place(x = 330, y=95)

def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        print(time.strftime("%H:%M:%S")) #show current time and countdown in the console
        time.sleep(1) # Wait for one seconds
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        period = time.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a coffee!")
                            sound_alarm()
                            messagebox.showinfo("TIME'S UP!!!")


def start_timer():
    global timer_running, timer_seconds, timer_after_id

    if not timer_running:
        # convert input values to seconds
        hours = int(hour_entry.get())
        minutes = int(minute_entry.get())
        seconds = int(second_entry.get())
        timer_seconds = hours*3600 + minutes*60 + seconds

        # start timer
        timer_running = True
        update_timer()

def stop_timer():
    global timer_running, timer_after_id

    if timer_running:
        # stop timer
        timer_tab.after_cancel(timer_after_id)
        timer_running = False

def reset_timer():
    global timer_running, timer_seconds, timer_after_id

    # reset timer values
    stop_timer()
    timer_seconds = 0
    hour_entry.delete(0,t.END)
    hour_entry.insert(0, "00")
    minute_entry.delete(0,t.END)
    minute_entry.insert(0, "00")
    second_entry.delete(0,t.END)
    second_entry.insert(0, "00")
    timer_label.config(text="00:00:00")

def update_timer():
    global timer_running, timer_seconds, timer_after_id

    # update timer label
    hours = timer_seconds // 3600
    minutes = (timer_seconds % 3600) // 60
    seconds = timer_seconds % 60
    timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    if timer_seconds > 0:
        # continue countdown
        timer_seconds -= 1
        timer_after_id = timer_tab.after(1000, update_timer)
    else:
        # countdown finished
        timer_running = False
        sound_alarm()

#clock image
time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
time_label.pack(anchor='center')
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.pack(anchor='s')
img = Image.open('clock.png')
img.resize((90, 90))
img = ImageTk.PhotoImage(img)
app_image = Label(clock_tab,image=img)
app_image.place(x=5, y=30)

#alarm image
img2 = Image.open('red_alarm.png')
img2.resize((90, 90))
img2 = ImageTk.PhotoImage(img2)
app_image = Label(alarm_tab, image=img2)
app_image.place(x=10, y=10)
name = Label(alarm_tab, text = "Alarm", font=('Ivy 18 bold'))
name.place(x=300, y=10)

#timer image
img3 = Image.open('timer1.png')
img3.resize((90, 90))
img3 = ImageTk.PhotoImage(img3)
app_image = Label(timer_tab, image=img3)
app_image.place(x=20, y=30)
name_timer = Label(timer_tab, text = "Timer", font=('Ivy 18 bold'))
name_timer.place(x=290, y=5)

#alarm entry hour
hour = Label(alarm_tab, text = "hour", font=('Ivy 10 bold'))
hour.place(x=250, y=40)
c_hour = Combobox(alarm_tab, width=2, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=250, y=58)
#alarm entry minutes
min = Label(alarm_tab, text = "min", font=('Ivy 10 bold'))
min.place(x=300, y=40)
c_min = Combobox(alarm_tab, width=2, font=('arial 15'))
c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(0)
c_min.place(x=300, y=58)
#alarm entry second
sec = Label(alarm_tab, text = "sec", font=('Ivy 10 bold'))
sec.place(x=350, y=40)
c_sec = Combobox(alarm_tab, width=2, font=('arial 15'))
c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_sec.current(0)
c_sec.place(x=350, y=58)
#alarm entry am/pm
period = Label(alarm_tab, text = "period", font=('Ivy 10 bold'))
period.place(x=400, y=40)
c_period = Combobox(alarm_tab, width=3, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=400, y=58)

# declaration of variables
hour = t.StringVar()
minute = t.StringVar()
second = t.StringVar()
chose = t.StringVar()
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

#timer
# create time input fields
hour_entry = Entry(timer_tab, width=4)
hour_entry.insert(0, "00")
hour_entry.place(x=230,y=40)
minute_entry = Entry(timer_tab, width=4)
minute_entry.insert(0, "00")
minute_entry.place(x=310,y=40)
second_entry = Entry(timer_tab, width=4)
second_entry.insert(0, "00")
second_entry.place(x=390,y=40)

# create start button
start_button = Button(timer_tab, text="Start", command=start_timer)
start_button.place(x=200,y=70)

# create stop button
stop_button = Button(timer_tab, text="Stop", command=stop_timer)
stop_button.place(x=280,y=70)

# create reset button
reset_button = Button(timer_tab, text="Reset", command=reset_timer)
reset_button.place(x=360,y=70)

# create timer label
timer_label = Label(timer_tab, text="00:00:00", font=("Arial", 30))
timer_label.place(x=240,y=120)
# set initial timer values
timer_seconds = 0
timer_running = False
timer_after_id = None

clock()
mixer.init()
window.mainloop()