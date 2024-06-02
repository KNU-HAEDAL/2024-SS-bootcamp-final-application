import tkinter as tk
from tkinter import filedialog
from datetime import date
import json

MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday", "Sunday"]


def calendar_generator(start_weekday, days_in_month):
    def save_to_json():
        for day in range(1, len(text_object_dict) + 1):
            save_dict[day] = text_object_dict[day].get("1.0", "end - 1 chars")

        file_location = filedialog.asksaveasfilename(initialdir="/")
        if file_location:
            with open(file_location, 'w') as json_file:
                json.dump(save_dict, json_file)

    def load_from_json():
        file_location = filedialog.askopenfilename(initialdir="/", title="Select a JSON to open")
        if file_location:
            with open(file_location) as json_file:
                global save_dict
                save_dict = json.load(json_file)
                for day in range(1, len(text_object_dict) + 1):
                    text_object_dict[day].insert("1.0", save_dict.get(str(day), ""))


    for i, weekday in enumerate(WEEKDAYS):
        names_label = tk.Label(calendar_frame, text=weekday, fg="black")
        names_label.grid(column=i, row=1, sticky='nsew')

    row = 0
    col = start_weekday
    for day in range(1, days_in_month + 1):
        day_frame = tk.Frame(calendar_frame)
        day_frame.grid(row=row +2, column=col, sticky='nsew')

        # draw label
        day_number_label = tk.Label(day_frame, text=day)
        day_number_label.grid(row=0)

        # draw text_box
        text_box = tk.Text(day_frame, width=15, height=5)
        text_box.grid(row=1)

        text_object_dict[day] = text_box
        


        col += 1
        if col == 7:
            col = 0
            row = (row + 1) % 7
    
    load_button = tk.Button(calendar_frame, text="스케줄 불러오기", command=load_from_json)
    save_button = tk.Button(calendar_frame, text="스케줄 저장하기", command=save_to_json)
    load_button.grid(row=8, column=4)
    save_button.grid(row=8, column=2)



def get_days_in_month(moth, year):
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def print_month_year_label(month, year):
    month_name = MONTH_NAMES[month - 1]
    month_year_label = tk.Label(calendar_frame, text=f"{month_name} {year}", font=("Arial", 20))
    month_year_label.grid(column=2, row=0, columnspan=3)


def make_month_switch_buttons():
    def switch_months(direction):
        global month, year, calendar_frame  # 전역 변수를 함수 내에서 수정할 수 있게 해줌
        month += direction
        if month == 0:
            month = 12
            year -= 1
        elif month == 13:
            month = 1
            year += 1


        calendar_frame.destroy()
        calendar_frame = tk.Frame(window)
        calendar_frame.grid()
        print_month_year_label(month, year)

        start_weekday = date(year, month, 1).weekday()
        days_in_month = get_days_in_month(month, year)
        make_month_switch_buttons()
        calendar_generator(start_weekday, days_in_month)


    go_back = tk.Button(calendar_frame, text="<", command=lambda: switch_months(-1))
    go_back.grid(column=0, row=0)
    go_forward = tk.Button(calendar_frame, text=">", command=lambda: switch_months(1))
    go_forward.grid(column=6, row=0)

window = tk.Tk()
window.title("Calendar")
window.geometry("1000x800")
window.columnconfigure(0, weight=1)

calendar_frame = tk.Frame(window)
calendar_frame.grid()

month = date.today().month
year = date.today().year
text_object_dict = {}
save_dict = {}


start_weekday = date(year, month, 1).weekday()
days_in_month = get_days_in_month(month, year)
calendar_generator(start_weekday, days_in_month)
print_month_year_label(month, year)

make_month_switch_buttons()

window.mainloop()