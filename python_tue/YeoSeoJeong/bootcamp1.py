import tkinter as tkt
from tkinter.filedialog import *
from tkinter import messagebox

window = tkt.Tk()
window.title('Notepad')
window.geometry('400x400+800+300')  # 400x400: 창 크기   800+300: 창이 800,300 위치에 띄워진다
window.resizable(0,0)  # 창 크기 설정 불가

window.iconbitmap("C:\\Users\\User\\OneDrive\\바탕 화면\\memo.ico")
# photo = tkt.PhotoImage(file="C:\\Study\\해달\\부트캠프\\2024-1-파이썬응용\\해달로고.png")
# window.iconphoto(False, photo)

# 텍스트 창 만들기 
text_area = tkt.Text(window)
# 공백 설정하기 
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
# 텍스트 화면을 윈도우에 동서남북으로 붙인다
text_area.grid(sticky=tkt.N+tkt.E+tkt.S+tkt.W)


def new_file():
    text_area.delete("1.0", tkt.END)
def save_file():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get("1.0", tkt.END)
            file.write(content)

def maker():
    messagebox.showinfo("만든 이", "전자 B반 24학번 여서정")


menuMaker = tkt.Menu(window)

first_menu = tkt.Menu(menuMaker, tearoff=0)
first_menu.add_command(label='새 파일', command=new_file)
first_menu.add_command(label='저장', command=save_file)
menuMaker.add_cascade(label='파일', menu=first_menu)

first_menu.add_separator()

first_menu.add_command(label='종료', command=window.destroy)

window.config(menu=menuMaker)

second_menu = tkt.Menu(menuMaker, tearoff=0)

second_menu.add_command(label='만든 이', command=maker)

menuMaker.add_cascade(label='정보', menu=second_menu)

window.mainloop()  
