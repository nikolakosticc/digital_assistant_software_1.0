import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import datetime
import time
import webbrowser
from playsound import playsound


#Set up the Program

root = tkinter.Tk()
root.title("Digital Assistant")
root.geometry("1120x540")
root.resizable(width=False, height=False)
root.configure(bg="#323999")


#Clock

Clock_Label = Label(root, text="Time", font=("Century Gothic", 20), fg="#fff", bg="#3841c7")
Clock_Label.place(x=853, y=75)


Clock = Label(root, font=('Century Gothic', 30), bg='#323999', fg="white")
Clock.place(x=800, y=110)

def tick():
    global time1
    time1 = ''
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        Clock.config(text=time2)
    Clock.after(200, tick)
tick()


#Calendar

today = datetime.date.today()

mindate = datetime.date(year=1900, month=1, day=1)
maxdate = datetime.date(year=2100, month=1, day=1)

Calendar_Label = Label(root, text="Calendar", font=("Century Gothic", 20), fg="#fff", bg="#3841c7", width=8)
Calendar_Label.place(x=820, y=195)

Calendar_Interface_Label = Calendar(root, font=("Century Gothic", 15), selectmode='day', locale='en_US',
mindate=mindate, maxdate=maxdate, disabledforeground='red',
cursor="hand1", year=2020, month=8, day=11)
Calendar_Interface_Label.place(x=700, y=250)


#Alarm

def alarm():
    
    #Set up the program

    root = tkinter.Tk()
    root.title("Alarm")
    root.geometry("400x270")
    root.resizable(width=False, height=False)
    root.configure(bg="#323999")

    Alarm_Label = Label(root, text="Alarm", font=("Century Gothic", 20), fg="#fff", bg="#3841c7", width=300)
    Alarm_Label.pack(side='top')
        
    Hours = Entry(root, font=("Century Gothic", 15), width=4)
    Hours.place(x=50, y=100)

    Minutes = Entry(root, font=("Century Gothic", 15), width=4)
    Minutes.place(x=200, y=100)

    Hours_Label = Label(root, text="Hours", font=("Century Gothic", 20), fg="#fff", bg="#323999")
    Hours_Label.place(x=100, y=90)

    Minutes_Label = Label(root, text="Minutes", font=("Century Gothic", 20), fg="#fff", bg="#323999")
    Minutes_Label.place(x=250, y=90)

    def activate_alarm():
        Hours_Info = int(Hours.get())
        Minutes_Info = int(Minutes.get())
        while True:
            if Hours_Info == datetime.datetime.now().hour and Minutes_Info == datetime.datetime.now().minute:
                playsound("alarm.mp3")
                break

    Enter_Button = Button(root, text="Enter", font=("Century Gothic", 15),
    fg="#fff", bg="#3841c7", width=10, command=activate_alarm, relief=FLAT)
    Enter_Button.place(x=135, y=200)

    root.mainloop()


#Menu Bar

menubar = Menu(root)
menubar.add_command(label="File")
menubar.add_command(label="Alarm", command=alarm)

root.config(menu=menubar)


#Close the window

def close_window():
    response = messagebox.askquestion("Exit the Program", "Do you really want to exit the program?")
    if response == 'yes':
        root.destroy()
    else:
        pass


#Labels

ChatBot_App_Label = Label(root, text="Digital Assistant", font=("Century Gothic", 20), fg="#fff", bg="#3841c7", width=300)
ChatBot_App_Label.pack(side='top')

Digital_Assistant_Label = Label(root, text="Digital Assistant", font=("Century Gothic", 20), fg="#fff", bg="#3841c7")
Digital_Assistant_Label.place(x=250, y=80)

Help_Label = Label(root, text="How can I help you?", font=("Century Gothic", 20), fg="#000", bg="#fff")
Help_Label.place(x=250, y=120)

Answer_Label = Label(root, text="Answer : ", font=("Century Gothic", 20), fg="#fff", bg="#323999")
Answer_Label.place(x=45, y=260)


#Entry Fields

Text_Entry = Entry(root, font=("Century Gothic", 15), width=30)
Text_Entry.place(x=50, y=460)


#Show the answer

def show_answer():
    question = Text_Entry.get()
    if "time" in question:
        Time = Label(root, font=("Century Gothic", 20), fg="#fff", bg="#323999", text=time)
        Time.place(x=165, y=260)
    if "google" in question:
        webbrowser.open("www.google.com")
    if "netflix" in question:
        webbrowser.open("www.netflix.com")
    if "spotify" in question:
        webbrowser.open("www.spotify.com")
    if "apple" in question:
        webbrowser.open("www.apple.com")


def delete_answer():
    Text_Entry.delete(0, 'end')


#User Picture

img = ImageTk.PhotoImage(Image.open("pic.png"))
panel = Label(root, image = img, relief=FLAT)
panel.place(x=50, y=60)


#Exit Icon

user_icon_path = r'exit.png'

user_icon = ImageTk.PhotoImage(Image.open(user_icon_path))
button1 = tk.Button(root, image=user_icon, relief=FLAT,
    text="optional text", bg='#3841c7', command=close_window)
button1.place(x=900, y=2)


#Buttons

Enter_Button = Button(root, text="Enter", font=("Century Gothic", 15),
                     fg="#fff", bg="#3841c7", width=10, command=show_answer, relief=FLAT)
Enter_Button.place(x=400, y=450)

Reset_Button = Button(root, text="Reset", font=("Century Gothic", 15),
                      fg="#fff", bg="#3841c7", width=10, command=delete_answer, relief=FLAT)
Reset_Button.place(x=550, y=450)


#Root Mainloop

root.mainloop()
