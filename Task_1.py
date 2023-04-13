import tkinter as tk
from tkinter import *
import datetime
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.title("Alarm Clock")
root.geometry("600x350")

head = Label(root, text='Alarm Clock', font=('comic sans',20))
head.grid(row=0, column=0, pady=10)

Clock_image = PhotoImage(file="Alarm_clock.png")
image = Label(root, image=Clock_image)
image.grid(rowspan=5, column=0)

select_hour = Label(root, text="Select Hour", font=('comic sans',17))
select_hour.grid(row=1, column=1)

options_hours = [str(i) for i in range(1, 13)]

Selected_option_hour = tk.StringVar()
Selected_option_hour.set(str(options_hours[0]))

select_box_hour = tk.OptionMenu(root, Selected_option_hour, *options_hours)
select_box_hour.config(width= 6)
select_box_hour.grid(row=1, column=2, padx=15 )

select_minutes = Label(root, text="Select Minutes", font=('comic sans',17))
select_minutes.grid(row=2, column=1)

options_minutes = [str("{:02d}".format(i)) for i in range(60)]

Selected_option_minutes = tk.StringVar()
Selected_option_minutes.set(str(options_minutes[0]))

select_box_minutes = tk.OptionMenu(root, Selected_option_minutes, *options_minutes)
select_box_minutes.config(width= 6)
select_box_minutes.grid(row=2, column=2, padx=15 )

select_am_pm = Label(root, text="Select AM/PM", font=('comic sans',17))
select_am_pm.grid(row=3, column=1)

option_am_pm = ['AM', 'PM']

selected_option_am_pm = tk.StringVar()
selected_option_am_pm.set(option_am_pm[0])

select_box_am_pm = tk.OptionMenu(root, selected_option_am_pm, *option_am_pm)
select_box_am_pm.grid(row=3, column=2)

def check_alarm():
    time = datetime.datetime.now()
    current_time = time.strftime('%I:%M %p')
    hour = int(Selected_option_hour.get())
    minute = int(Selected_option_minutes.get())
    ampm = selected_option_am_pm.get()
    alarm_time = datetime.time(hour, minute).strftime("%I:%M ") + ampm
    
    print(current_time,'\t\t',alarm_time)
    if current_time == alarm_time:
        playsound("Alarm_sound.mp3")
        messagebox.showinfo(title='Alarm', message='Time to wake up!')
    else:
        root.after(10000, check_alarm)

def set_alarm():
    hour = int(Selected_option_hour.get())
    minute = int(Selected_option_minutes.get())
    ampm = selected_option_am_pm.get()
    alarm_time = f"{hour}:{minute} {ampm}"
    messagebox.showinfo(title= "Alarm", message=f"Alarm set for {alarm_time}", parent= root)
    root.after(1000, check_alarm)

submit = Button(root, text='Set Alarm', font=('comic sans',20), background="gray", command=set_alarm)
submit.grid(row=4, column=1, columnspan=2, pady=10)

print("Current time","\tAlarm time")

root.mainloop()