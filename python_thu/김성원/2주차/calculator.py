from tkinter import Tk
import tkinter as tkt

def on_click(number):
    entry.insert(tkt.END, number)
 
def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1,bg=None):
   button = tkt.Button(root, text=text, padx=width, pady=height, command=command, font=('Consolas', '14', 'bold'),bg= bg, borderwidth=4)
   button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')
 
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

    if 연산자 == "+":
        result = first_num + second_num
        if result % 1 == 0:
            result = int(result)
        entry.insert(0, result)
    elif 연산자 == "-":
        result = first_num - second_num
        if result % 1 == 0:
            result = int(result)
        entry.insert(0, result)
    elif 연산자 == "*":
        result = first_num * second_num
        if result % 1 == 0:
            result = int(result)
        entry.insert(0, result)
    elif 연산자 == "/":
        result = first_num / second_num
        if result % 1 == 0:
            result = int(result)
        entry.insert(0, result)
    elif 연산자 == "%":
        result = first_num % second_num
        if result % 1 == 0:
            result = int(result)
        entry.insert(0, result)

root = Tk()
root.title("계산기")

photo = tkt.PhotoImage(file="python_thu\김성원\\2주차\윈도우계산기아이콘.png")
root.iconphoto(False, photo)

# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")  # borderwitdh: 테두리두께
entry.grid(row=0, column=0, columnspan=4, pady=10)
#justify:라벨의 문자열이 여러 줄 일 경우 정렬 방법

for number in range(9):
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n), bg='gainsboro') #, bg='gainsboro')
create_button("0", 5, 0, lambda: on_click(0), columnspan=2, bg='gainsboro') #, bg='gainsboro')

create_button("C", 1, 0, on_clear, bg='gray70')

create_button("%", 1, 2, lambda: operate('%'), bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')

root.mainloop()