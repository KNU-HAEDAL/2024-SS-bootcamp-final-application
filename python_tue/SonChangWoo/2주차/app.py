import tkinter as tkt
from tkinter import messagebox, filedialog

# 창 생성
root = tkt.Tk()
root.title("계산기")

# 아이콘 설정
# photo = tkt.PhotoImage(file="C:/Study/해달/부트캠프/2024-1-파이썬응용/2주차/윈도우계산기아이콘.png")
photo = tkt.PhotoImage(file="./윈도우계산기아이콘.png")
root.iconphoto(False, photo)


# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")  # borderwitdh: 테두리두께
entry.grid(row=0, column=0, columnspan=4, pady=10)




# # 엔트리 생성 (한줄 텍스트)
# entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")  # borderwitdh: 테두리두께
# entry.grid(row=0, column=0, columnspan=4, pady=100)

def on_click(number):
    entry.insert(tkt.END, number)



def create_button(text, row, column, command, width=10, height=9, columnspan=1, rowspan=1, bg=None):
   button = tkt.Button(root, text=text, padx=width, pady=height, command=command,  borderwidth=4, relief="raised",bg=bg)
   button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')


for number in range(9):
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n)) #, bg='gainsboro')
create_button("0", 5, 0, lambda: on_click(0), columnspan=2) #, bg='gainsboro')



def on_clear():
    entry.delete(0, tkt.END)

...


def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = int(entry.get())
    entry.delete(0, tkt.END)

def on_equal():
    second_num = int(entry.get())
    entry.delete(0, tkt.END)

    if 연산자 == "+":
        a=first_num + second_num
    elif 연산자 == "-":
        a=first_num - second_num
    elif 연산자 == "*":
        a=first_num * second_num
    elif 연산자 == "/":
        a=first_num / second_num
    elif 연산자 == "%":
        a=first_num % second_num

    if a==int(a):
        entry.insert(0, int(a))
    else:
        entry.insert(0, a)
 


create_button("%", 1, 2, lambda: operate("%"),bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')

create_button("C", 1, 0, on_clear, bg='gray70')

root.mainloop()

