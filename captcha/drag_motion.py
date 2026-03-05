from tkinter import *
import webbrowser
import time
import math
import pandas as pd
import os

coordinates = []
times = []
log = {}

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    if 120 <= x <= 180 and 120 <= y <= 180:
       widget.place(x=1000,y=1000)

def redirect(risk):
    url = "https://www.google.com/"
    if risk == 'Likely Bot' or risk == 'Bot':
       exit
    webbrowser.open_new(url)


def record_coordinates(event):
    widget = event.widget
    record_on = True
    while record_on:
         coordinates.append((widget.winfo_x(),widget.winfo_y()))
         times.append(time.localtime().tm_sec)
         widget.update()
         time.sleep(0.1)
         if widget.winfo_x() == 1000 and widget.winfo_y() == 1000:
            record_on = False

def calculate_time_risk(time_taken):
    if time_taken < 0.30:
        return 0.95
    elif 0.30 <= time_taken <= 0.60:
        return 0.80
    elif 0.60 < time_taken <= 1.20:
       return 0.40
    elif 1.20 < time_taken <= 3:
        return 0.10
    elif 3 < time_taken <= 6:
        return 0.20
    elif time_taken > 6:
        return 0.30
    
def calculate_speed_risk(speed):
    if speed > 3500:
        return 0.85
    elif 2000 <= speed < 3500:
        return 0.60
    elif 800 <= speed < 2000:
        return 0.15
    elif 300 <= speed < 800:
        return 0.20
    elif speed < 300:
        return 0.35
    
def calculate_stops_risk(stops):
    if stops == 0:
        return 0.85
    elif stops == 1:
        return 0.30
    elif 2 <= stops <+ 4:
        return 0.0
    elif 5 <= stops <= 8:
        return 0.25
    elif stops > 8:
        return 0.50
    
def calculate_total_risk(time_risk, speed_risk, stops_risk):
    Risk = 0.35*time_risk + 0.40*speed_risk + 0.25*stops_risk
    if Risk < 0.25:
        return 'Human'
    if 0.25 < Risk <= 0.45:
        return 'Probably Human'
    if 0.45 < Risk <= 0.65:
        return 'Suspicious'
    if 0.65 < Risk <= 0.80:
        return 'Likely Bot'
    if Risk > 0.80:
        return 'Bot'
            
def log_info():
    if 59 in times and 0 in times:
       for i in range(len(times)):
           if 0<= times[i] <= 10:
              times[i] += 60
        
    log['time_taken_in_seconds'] = times[-1] - times[0]
    distance = 0
    stops = []
    for i in range(len(coordinates)):
        if i+1 < len(coordinates):
           distance += math.dist(coordinates[i],coordinates[i+1])
           if coordinates[i] == coordinates[i+1] and (coordinates[i],coordinates[i+1]) not in stops:
              stops.append((coordinates[i],coordinates[i+1]))
    if log['time_taken_in_seconds'] == 0:
        log['average_speed'] = distance
    else:
        log['average_speed'] = distance/log['time_taken_in_seconds']
    log['no_of_stops'] = len(stops)
    
    time_risk = calculate_time_risk(log['time_taken_in_seconds'])
    speed_risk = calculate_time_risk(log['average_speed'])
    stops_risk = calculate_stops_risk(log['no_of_stops'])

    log['risk'] = calculate_total_risk(time_risk,speed_risk,stops_risk)
    df = pd.DataFrame([log])
    file = "mouse.csv"
    df.to_csv(
        file,
        mode = "a",
        index = False,
        header = not os.path.exists(file)
    )

def checkout():
    log_info()
    redirect(log['risk'])

window = Tk()
window.geometry("600x400")
label = Label(window, text = "🛒", font = ("Segor UI Emoji",70))
label2 = Label(window, text = "🍞", font = ("Segoe UI Emoji",30))
label3 = Label(window, text = "Drag And Drop The Bread\nInto The Shopping Cart",font = ("Ariel",20))

label.place(x = 150, y = 150)
label2.place(x = 380, y = 180)
label3.place(x = 150, y = 30)

button = Button(window,text="Check Out",command=checkout)
button.place(x=280,y=300)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)
label2.bind("<Button-1>",record_coordinates,add="+")


window.mainloop()
