import tkinter as tkt # tk import



def on_click(number):
    entry.insert(tkt.END, number)


# 윈도우 생성
root = tkt.Tk()
root.title("계산기")



# 아이콘 설정
# photo = tkt.PhotoImage(file="C:/Study/해달/부트캠프/2024-1-파이썬응용/2주차/윈도우계산기아이콘.png")
photo = tkt.PhotoImage(file="/Users/kimseeun/Desktop/해달/2.png")
root.iconphoto(False, photo)


# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")  # borderwitdh: 테두리두께
entry.grid(row=0, column=0, columnspan=4, pady=10)
#borderwidth:
#justify:라벨의 문자열이 여러 줄 일 경우 정렬 방법



    
# def on_click(number):
    # entry.insert(tkt.END, number)



# -> 정리
#def create_button(text, row, column, command, width=40, height=20, columnspan=1, rowspan=1):
#    button = tkt.Button(root, text=text, padx=width, pady=height, command=command)
#    button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

# bg=bg 추가
def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1, bg=None):
   button = tkt.Button(root, text=text, padx=width, pady=height, command=command, bg= bg)
   button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')


for number in range(9):
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n), bg='gainsboro')
create_button("0", 5, 0, lambda: on_click(0), columnspan=2, bg='gainsboro')




def on_clear(): # 변수 없어도 됨
    entry.delete(0, tkt.END)
create_button("C", 1, 0, on_clear, bg='gray70')


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
    elif 연산자 == "-":
        result = first_num - second_num
    elif 연산자 == "*":
        result = first_num * second_num
    elif 연산자 == "/":
        result = first_num / second_num
    elif 연산자 == "%":
        result = first_num % second_num
        
    if result is not None:
        if result.is_integer():
            entry.insert(0, int(result))  # 정수일 때는 소수점 이하를 제거하여 출력
        else:
            entry.insert(0, result)  # 소수점까지 출력
    


create_button("%", 1, 2, None, bg='gray70')
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')



root.mainloop() # 항상 마지막에 !!



# 숙제: 소수점까지 계산, 소수점아래 0일때는 정수만보이게
# 정수랑 소수 나눠서 생각...
# create_button에는 나머지잇음
# 나머지연산 구현
# 음영 주기 (선택)
# 가벼운 마음으로...