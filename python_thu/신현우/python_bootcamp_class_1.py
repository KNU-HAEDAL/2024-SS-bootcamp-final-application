#할거 1 파일 새로 만들 때 바탕화면에 안만들고 지정한 폴더에 만들어지게 하기.
#할거 2 vs코드 파일 내부에 제출할 파일 디렉토리 만들고 깃허브에 연동하기.
#할거 3 코드 줄 바꿔보면서 순서 확인해보기.
##
from tkinter import *
from tkinter.filedialog import *

def new_file():  #assignment 1 #초기화
    text_area.delete(1.0, END)
def save_file(): #assignment 2 #다시 저장
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            text = text_area.get(1.0, END)
            file.write(text)  
def maker(): #assignment 3 #팝업이 하나 더
    popup = Toplevel(window)
    popup.title("About")
    label = Label(popup, text="파이썬으로 메모장 만들기")
    label.pack()


window = Tk() #창을 열어준다
window.iconbitmap("C:/Users/shin/OneDrive - usk.ac.kr/바탕 화면/notepad-icon_34386.ico")
window.title('notepad')
window.geometry('400x400+800+300') #너비 x 높이 + (800,300) 모니터의 4분면 좌표.
window.resizable(0,0) # 윈도우 크기 고정 창 크기 조정이 불가능함.

#메뉴 생성
menuMaker = Menu(window)

#첫번째 메뉴 만들기
first_menu = Menu(menuMaker, tearoff=0)

#첫번째 메뉴의 세부 메뉴 추기 맟 함수 연결
first_menu.add_command(label = '새 파일', command = new_file)
first_menu.add_command(label = '저장',command = save_file)

#메뉴 바 추가
menuMaker.add_cascade(label='파일',menu=first_menu)


#메뉴 구성
window.config(menu=menuMaker)

first_menu.add_separator()

#종료 옵션 추가하기
first_menu.add_command(label='종료',command=window.destroy)

second_menu = Menu(menuMaker, tearoff=0)
second_menu.add_command(label = '만든 이',command = maker)
menuMaker.add_cascade(label='정보',menu = second_menu)

#텍스트 창 만들기
text_area = Text(window)
#공백 설정
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight =1)
text_area.grid(sticky = N+E+S+W)
#텍스트 화면을 윈도우에 동서남북으로 붙인다
window.mainloop() #창을 닫아준다 
#항상 마지막에 꼭 포함을 해줘야함.


