import tkinter as tk
from tkinter import ttk, font
import customtkinter as ctk
import time
import threading
from playsound import playsound

class WaterTimer:
    def __init__(self):
        #window
        self.window = ctk.CTk(fg_color="#131724")
        self.window.title("Water Timer")
        self.window.geometry("620x420")
        self.window.minsize(620, 420)
        self.window.maxsize(620, 420)
        #big timer
        self.timer = ctk.CTkCanvas(
            self.window,
            height = 300, width = 250, bg = "#131724",highlightthickness=0)
        self.timer.place(x = 85, y = 70)
        self.timer.create_oval(18, 18, 188, 188, width = 25, outline = "#3531FF")
        self.cancel_button = ctk.CTkButton(
            self.window,
            text = "Cancel",
            width = 117,
            height = 67,
            corner_radius = 90,
            fg_color = "#FF698D",
            hover_color = "#783041",
            text_color = "black",
            state= "disabled",
            command = self.stop)
        self.cancel_button.place(x = 133, y = 303)
        #Sound menu

        self.sounds = ["Sound 1", "Sound 2", "Sound 3", "Sound 4"]

        self.optionmenu = ctk.CTkOptionMenu(
        self.window,
        values = self.sounds,
        command = self.sound_picker,
        font = ('<Calibri>', 15),
        )
        self.optionmenu.place(x = 420, y = 250)

        self.hour = int(0)
        self.minute = int(0)
        self.second = int(0)

        #start button
        self.start_button = ctk.CTkButton(
            self.window,
            text = "Start",
            width = 100,
            height = 50,
            font = ('<Calibri>', 24),
            fg_color= "#328A4B",
            hover_color="#184625",
            command = self.start_thread)
        self.start_button.place(x = 440, y = 300)

        #time units
        self.time_units = ctk.CTkLabel(
            self.window,
            text = "hr            min           sec",
            font = ('<Calibri>', 15),)
        self.time_units.place(x = 420, y = 120)

        #Counter
        self.counter_second = ctk.CTkLabel(
            self.window,
            text = "00:00:00",
            font = ('<Calibri>', 25)
        )
        self.counter_second.place(x = 136, y = 155)
        #time values
        self.hour_value = ctk.CTkLabel(
            self.window,
            text = self.hour,
            font = ('<Calibri>', 15))
        self.minute_value = ctk.CTkLabel(
            self.window,
            text = self.minute,
            font = ('<Calibri>', 15))
        self.second_value = ctk.CTkLabel(
            self.window,
            text = self.second,
            font = ('<Calibri>', 15))
        self.hour_value.place(x = 400, y = 120)
        self.minute_value.place(x = 462, y = 120)
        self.second_value.place(x = 530, y = 120)

        #changing buttons
        self.hour_plus = ctk.CTkButton(
            self.window,
            text = "+",
            height = 25,
            width = 25,
            command = self.add_hour)
        self.hour_minus = ctk.CTkButton(
            self.window,
            text = "-",
            height = 25,
            width = 25,
            command = self.minus_hour)
        self.minute_plus = ctk.CTkButton(
            self.window,
            text = "+",
            height = 25,
            width = 25,
            command = self.add_minute)
        self.minute_minus = ctk.CTkButton(
            self.window,
            text = "-",
            height = 25,
            width = 25,
            command= self.minus_minute)
        self.second_plus = ctk.CTkButton(
            self.window,
            text = "+",
            height = 25,
            width = 25,
            command = self.add_second)
        self.second_minus = ctk.CTkButton(
            self.window,
            text = "-",
            height = 25,
            width = 25,
            command = self.minus_second)
        self.hour_plus.place(x = 405, y = 95)
        self.hour_minus.place(x = 405, y = 150)
        self.minute_plus.place(x = 473, y = 95)
        self.minute_minus.place(x = 473, y = 150)
        self.second_plus.place(x = 541, y = 95)
        self.second_minus.place(x = 541, y = 150)

        self.end_screen = ctk.CTkButton(
            self.window,
            text = "Tap this panel when you've drank water",
            font = ("<Calibri>", 24),
            width = 500,
            height = 250,
            fg_color = "#123549",
            command = self.start_thread,
            corner_radius = 20)
        
        self.stop_loop = False
        self.alarm_on = False
        self.sound = "Sound 1"

        self.window.mainloop()

    def add_hour(self):
        self.hour += 1
        self.hour_value.configure(text = self.hour)

        if self.hour == 24:
            self.hour = 23
            self.hour_value.configure(text = self.hour)

    def minus_hour(self):
        self.hour -= 1
        self.hour_value.configure(text = self.hour)

        if self.hour == -1:
            self.hour = 0
            self.hour_value.configure(text = self.hour)

    def add_minute(self):
        self.minute += 5
        self.minute_value.configure(text = self.minute)

        if self.minute > 55:
            self.minute = 55
            self.minute_value.configure(text = self.minute)

    def minus_minute(self):
        global minute
        self.minute = int(self.minute)-5
        self.minute_value.configure(text = self.minute)

        if self.minute < 0:
            self.minute = 0
            self.minute_value.configure(text = self.minute)

    def add_second(self):
        global second
        self.second = int(self.second)+5
        self.second_value.configure(text = self.second)

        if self.second > 55:
            self.second = 55
            self.second_value.configure(text = self.second)

    def minus_second(self):
        global second
        self.second = int(self.second)-5
        self.second_value.configure(text = self.second)

        if self.second < 0:
            self.second = 0
            self.second_value.configure(text = self.second)
            
    def sound_picker(self, choice):
        self.sound = str(choice)

    def start_thread(self):
        t = threading.Thread(target = self.start)
        t.start()

    def start(self):
        hours = self.hour
        minutes = self.minute
        seconds = self.second
        total_time = hours * 3600 + minutes * 60 + seconds
        if total_time == 0:
            pass
        else:
            self.stop_loop = False
            self.alarm_on = False
            self.end_screen.place_forget()
            self.hour_plus.configure(state = "disabled")
            self.hour_minus.configure(state = "disabled")
            self.minute_plus.configure(state = "disabled")
            self.minute_minus.configure(state = "disabled")
            self.second_plus.configure(state = "disabled")
            self.second_minus.configure(state = "disabled")
            self.start_button.configure(state = "disabled")
            self.optionmenu.configure(state = "disabled")
            self.cancel_button.configure(state = "normal")


            while total_time > 0 and not self.stop_loop:
                total_time -= 1

                minutes, seconds, = divmod(total_time, 60)
                hours, minutes = divmod(minutes, 60)

                self.counter_second.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
                self.window.update()
                time.sleep(1)
            
            self.alarm_on = True
            self.cancel_button.configure(state = "disabled")
            if self.stop_loop == False:
                self.end_screen.place(x = 60, y = 85)
                time.sleep(0.1)
                while self.alarm_on == True:
                    if str(self.sound) == "Sound 1":
                        playsound("alarm_1.mp3")
                        time.sleep(0.3)
                    if str(self.sound) == "Sound 2":
                        playsound("alarm_2.mp3")
                        time.sleep(0.3)
                    if str(self.sound) == "Sound 3":
                        playsound("alarm_3.mp3")
                        time.sleep(0.3)
                    if str(self.sound) == "Sound 4":
                        playsound("alarm_4.mp3")
                        time.sleep(0.3)

    def stop(self):
        self.stop_loop = True
        self.hour_plus.configure(state = "normal")
        self.hour_minus.configure(state = "normal")
        self.minute_plus.configure(state = "normal")
        self.minute_minus.configure(state = "normal")
        self.second_plus.configure(state = "normal")
        self.second_minus.configure(state = "normal")
        self.start_button.configure(state = "normal")
        self.optionmenu.configure(state = "normal")
        self.cancel_button.configure(state = "disabled")
        self.counter_second.configure(text = "00:00:00")
WaterTimer()