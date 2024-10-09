from tkinter import *
import calendar

root = Tk()
root.title("Calendar")

year = 2024  # Change year


cal = calendar.TextCalendar().formatyear(year)


cal_label = Label(root, text=cal, font=("Courier", 10), justify=LEFT)
cal_label.pack(padx=10, pady=10)


root.mainloop()
