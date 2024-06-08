from tkinter import *
from tkinter.filedialog import *

filename = "mynote.txt"
def new_file(): #초기화 함수    
    text_area.delete(1.0, END)

def save_file(): #저장
    f = asksaveasfile(mode="w",defaultextension=".txt", filetypes=[('Text files', ',txt')])
    text_save = str(text_area.get(1.0,END))
    f.write(text_save)
    f.close()

def maker(): #팝업띄우기 - > 무슨말이어도 상관x
    help_view = Toplevel(window)
    help_view.geometry("300x50+800+300")
    help_view.title("만든이")
    lb = Label(help_view, text = 'eneji')
    lb.pack()


#윈도우 생성하기
window = Tk() #위에서 import *이라고 했으니 따로 tkt.를 붙일 필요없음 ->창 열기
window.title("NotePad")
window.geometry('400x400+800+300') #위치를 직접 지정 너비x높이+
window.resizable(0,0) #사이즈 조정을 막음 ;True값으로 하면 조정가능 False는 불가

#아이콘넣기
window.iconbitmap("C:/Users/82108/Desktop/24_python/bootcamp/notepad-icon_34386.ico") #역슬래시 대신 / , 주소+아이콘명+확장자까지 적기

#텍스트창만들기
text_area = Text(window)

#고액설정하기
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)

text_area.grid(sticky=N+E+S+W)

#첫번쨰 메뉴만들기

#메뉴설정
menuMaker = Menu(window)
#첫번째 메뉴 만들기
first_menu = Menu(menuMaker,tearoff=0)
#첫번째 메뉴의 세부메뉴 추가 및 함수 연결
first_menu.add_command(label = '새파일', command = new_file)
first_menu.add_command(label = '저장', command = save_file)
#메뉴 바 추가
menuMaker.add_cascade(label = '파일',menu=first_menu)

#두번째 메뉴 추가
second_menu = Menu(menuMaker,tearoff = 0)
#세부 메뉴 추가, 함수연결
second_menu.add_command(label='만든 이',command = maker)
#메뉴 바 추가
menuMaker.add_cascade(label ='정보',menu = second_menu)

#메뉴 구성 -> 항상 필수로 잇어야댐
window.config(menu=menuMaker)

#첫번째 메뉴에 구분선 추가
first_menu.add_separator()

#구분선 아래에 종료 옵션 추가하기
first_menu.add_command(label = '종료',command = window.destroy)


window.mainloop() #항상 포함시켜야함 -> 창 닫기