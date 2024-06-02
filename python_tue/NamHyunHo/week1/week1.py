import tkinter as tkt
from tkinter.filedialog import *

# 윈도우 생성
window = tkt.Tk()
window.title('Notepad')
window.geometry('400x400+800+300') # 400x400 : 창 크기 #창이 800,300 위치에 띄워진다
window.resizable(0,0) # 창 크기 설정 불가


# 아이콘 입력
window.iconbitmap("C:\\Users\\AERO\\Downloads\\haedal\\2024-SS-bootcamp-final-application\\python_tue\\NamHyunHo\\week1\\memo.ico")
#photo = tkt.PhotoImage(file="C:\\Users\\AERO\\Downloads\\haedal\\bootcamp\\0week\\해달로고.png")
#window.iconphoto(False, photo)


#텍스트 창 만들기 
text_area = tkt.Text(window)

#공백 설정하기 
window.grid_rowconfigure(0, weight =1)
window.grid_columnconfigure(0, weight = 1)

#텍스트 화면을 윈도우에 동서남북으로 붙인다
text_area.grid(sticky = tkt.N+tkt.E+tkt.S+tkt.W)


# 메뉴 클릭 시 함수 정의

# 텍스트 영역 지우기
def new_file():
      text_area.delete(1.0, tkt.END) 

# 저장    
def save_file():        
    f = asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('Text files', '.txt')]) # 파일 저장 물어보기
    text_save = str(text_area.get(1.0, tkt.END)) # 텍스트 영역에 있는 것들을 문자화 시켜서 저장
    f.write(text_save)
    f.close()                    

# 만든 이
def maker():
    # 새 창 만들고 내용 적기
    help_view = tkt.Toplevel(window)
    help_view.geometry('300x50+850+400')
    help_view.title('만든 이')
    lb = tkt.Label(help_view, text = '\ndesigned by hyeonho')
    lb.pack()


#메뉴 생성
menuMaker = tkt.Menu(window)

#첫번째 메뉴 만들기 
first_menu = tkt.Menu(menuMaker, tearoff=0)

#첫번째 메뉴의 세부메뉴 추가 및 함수 연결
first_menu.add_command(label = '새 파일', command = new_file)
first_menu.add_command(label = '저장', command = save_file)

#메뉴 바 추가 
menuMaker.add_cascade(label='파일', menu=first_menu)
first_menu.add_separator()

#메뉴 구성
window.config(menu = menuMaker)

#종료 옵션 추가하기
first_menu.add_command(label='종료', command=window.destroy)


#두번째 메뉴 추가 
second_menu = tkt.Menu(menuMaker, tearoff=0)

#세부 메뉴 추가, 함수 연결
second_menu.add_command(label = '만든 이', command = maker)

#메뉴 바 추가
menuMaker.add_cascade(label='정보', menu = second_menu)


# 창 실행 (맨 마지막 줄)
window.mainloop()
