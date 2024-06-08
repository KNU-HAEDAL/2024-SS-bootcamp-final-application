from tkinter import *
from tkinter.filedialog import *
import tkinter as tkt


#버튼 눌렀을 때 실행될 함수 생성
def on_click(number):
    entry.insert(tkt.END, number) #number을 받아서 창에 입력해주기 

#bg(background color)설정 안하는 버전
#def create_button(text, row, column, command, width=40, height=20, columnspan=1, rowspan=1):
#    button = tkt.Button(root, text=text, padx=width, pady=height, command=command)
#    button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1, bg=None):
   button = tkt.Button(root, text=text, padx=width, pady=height, command=command, bg =bg)
   button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')

def on_clear():
    entry.delete(0, tkt.END)

def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = float(entry.get()) #float대신 int로 받으면 소수점 계산이 안됨
    entry.delete(0, tkt.END)

def on_equal():
    second_num = float(entry.get()) #두번째 정수받는 창 새로열기
    entry.delete(0, tkt.END)

    if 연산자 == "+":
        if first_num + second_num == int(first_num+second_num):
            entry.insert(0, int(first_num + second_num))
        else :
            entry.insert(0, first_num+second_num)
    elif 연산자 == "-":
        if first_num - second_num == int(first_num-second_num):
            entry.insert(0, int(first_num - second_num))
        else :
            entry.insert(0, first_num-second_num)
    elif 연산자 == "*":
        if first_num * second_num == int(first_num*second_num):
            entry.insert(0, int(first_num * second_num))
        else :
            entry.insert(0, first_num*second_num)
    elif 연산자 == "/":
        if first_num / second_num == int(first_num/second_num):
            entry.insert(0, int(first_num / second_num))
        else :
            entry.insert(0, first_num/second_num)
    elif 연산자 == "%":
        if first_num % second_num == int(first_num%second_num):
            entry.insert(0, int(first_num % second_num))
        else :
            entry.insert(0, first_num%second_num)


# 윈도우 생성
root = tkt.Tk()
root.title("계산기")

tkt.Label(root,border = 3, relief ="sunken", text = "sunken&borderwidth = 3")

# 아이콘 설정
# photo = tkt.PhotoImage(file="C:/Study/해달/부트캠프/2024-1-파이썬응용/2주차/윈도우계산기아이콘.png")
photo = tkt.PhotoImage(file="C:/Users/82108/Desktop/24_python/bootcamp/윈도우계산기아이콘.png")
root.iconphoto(False, photo)

# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")  # borderwitdh: 테두리두께
entry.grid(row=0, column=0, columnspan=4, pady=10)
#justify:라벨의 문자열이 여러 줄 일 경우 정렬 방법

#버튼 만들기
for number in range(9): #1~9까지의 버튼
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n), bg='gainsboro')
create_button("0", 5, 0, lambda: on_click(0), columnspan=2, bg='gainsboro')
#^얘가 0버튼 을 더 크게 만들기 위한 함수

create_button("C", 1, 0, on_clear, bg='gray70')

create_button("%", 1, 2, lambda: operate("%"), bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')

for number in range(9):
    create_button(number+1,4-number//3,number%3,lambda n = number+1: on_click(n),bg = 'gainsboro')
create_button(0,5,0,lambda:on_click(0),columnspan=2,bg='gainsboro')


root.mainloop() #항상 맨밑에.......