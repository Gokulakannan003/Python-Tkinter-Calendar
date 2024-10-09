from tkinter import *
import calendar

root = Tk()
root.title("Calendar")

year = 2024


cal = calendar.TextCalendar().formatyear(year)


cal_label = Label(root, text=cal, font=("Courier", 10), justify=LEFT)
cal_label.pack(padx=10, pady=10)


root.mainloop()
"""
from tkinter import *
import calendar

# Create the main application window
root = Tk()
root.title("Year 2024 Calendar")

# Define the year
year = 2024
current_month = 0  # Start from January

# Function to update the calendar display
def show_month(month):
    cal = calendar.month(year, month)
    cal_label.config(text=cal)

# Function to go to the next month
def next_month():
    global current_month
    if current_month < 11:  
        current_month += 1
        show_month(current_month + 1)

# Function to go to the previous month
def previous_month():
    global current_month
    if current_month > 0:
        current_month -= 1
        show_month(current_month + 1)

# Create a Label to display the calendar
cal_label = Label(root, text="", font=("Courier", 12), justify=LEFT)
cal_label.pack(padx=10, pady=10)

# Create navigation buttons
prev_button = Button(root, text="Previous", command=previous_month)
prev_button.pack(side=LEFT, padx=10, pady=10)

next_button = Button(root, text="Next", command=next_month)
next_button.pack(side=RIGHT, padx=10, pady=10)

show_month(current_month + 1)


root.mainloop()
"""