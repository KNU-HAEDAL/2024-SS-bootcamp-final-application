#2week assignments

import tkinter as tkt

def on_click(number):
    entry.insert(tkt.END, str(number))

def on_clear():
    entry.delete(0, tkt.END)

def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = float(entry.get())
    entry.delete(0, tkt.END)

def on_equal():
    second_num = float(entry.get())
    entry.delete(0, tkt.END)

    result = None
    if 연산자 == "+":
        result = first_num + second_num
        if result == int(result):
            entry.insert(0, int(result))
        else:
            entry.insert(0, result)
    elif 연산자 == "-":
        result = first_num - second_num
        if result == int(result):
            entry.insert(0, int(result))
        else:
            entry.insert(0, result)
    elif 연산자 == "*":
        result = first_num * second_num
        if result == int(result):
            entry.insert(0, int(result))
        else:
             entry.insert(0, result)
    elif 연산자 == "/":
        result = first_num / second_num
        if result == int(result):
            entry.insert(0, int(result))
        else:
            entry.insert(0, result)
    elif 연산자 == "%":
        result = first_num % second_num
        if result == int(result):
            entry.insert(0, int(result))
        else:
            entry.insert(0, result)

root = tkt.Tk()
root.title("계산기")

entry = tkt.Entry(root, width=20, borderwidth=5, font=("Verdana", 13), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1, bg=None):
    button = tkt.Button(root, text=text, padx=width, pady=height, command=command, bg=bg, font=('Helvetica',14, 'bold'))
    button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')

for number in range(9):
    create_button(number + 1, 4-number//3, number%3, lambda n=number+1: on_click(n), bg='gainsboro')
create_button(0, 5, 0, lambda: on_click(0), columnspan=2, bg='gainsboro')

create_button("C", 1, 0, on_clear, bg='gray70')
create_button("%", 1, 2, lambda: operate("%"), bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button(".", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')

root.mainloop()