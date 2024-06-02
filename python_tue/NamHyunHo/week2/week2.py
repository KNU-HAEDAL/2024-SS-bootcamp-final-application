import tkinter as tkt

# 창 생성
root = tkt.Tk()
root.title("계산기")

# 아이콘 설정
photo = tkt.PhotoImage(file="C:\\Users\\AERO\\Downloads\\haedal\\2024-SS-bootcamp-final-application\\python_tue\\NamHyunHo\\week2\\윈도우계산기아이콘.png")
#photo = tkt.PhotoImage(file="./윈도우계산기아이콘.png")
root.iconphoto(False, photo)

# 글 적을 공간 생성!
# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")  # borderwitdh: 테두리두께
entry.grid(row=0, column=0, columnspan=4, pady=10)

def on_click(number):
    entry.insert(tkt.END, number)

def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1, bg=None):
    button = tkt.Button(root, text=text, padx=width, pady=height, command=command, borderwidth=5) # 버튼의 테두리 두께를 5으로 설정
    button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')


for number in range(9):
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n)) #, bg='gainsboro')
create_button("0", 5, 0, lambda: on_click(0), columnspan=2) #, bg='gainsboro')

def on_clear():
    entry.delete(0, tkt.END)

create_button("C", 1, 0, on_clear, bg='gray70')

def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = float(entry.get())
    entry.delete(0, tkt.END)

# 소수점 연산 구현
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')

def on_equal():
    second_num_str = entry.get()
    second_num = float(second_num_str) if '.' in second_num_str else int(second_num_str)
    entry.delete(0, tkt.END)

    result = 0  # result 변수 초기화

    if 연산자 == "+":
        result = first_num + second_num
    elif 연산자 == "-":
        result = first_num - second_num
    elif 연산자 == "*":
        result = first_num * second_num
    elif 연산자 == "/":
        result = first_num / second_num
    elif 연산자 == "%":
        result = first_num % second_num
    
    if result == int(result):  # 결과가 정수일 때
        entry.insert(0, int(result))  # 정수로 변환하여 결과 표시
    else:
        entry.insert(0, result)  # 그 외에는 그대로 표시


create_button("%", 1, 2, lambda: operate("%"), bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')



    
root.mainloop()
