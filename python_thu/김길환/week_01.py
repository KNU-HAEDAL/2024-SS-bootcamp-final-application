from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox

def new_file():
    text_area.delete(1.0, END)

def save_file():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding='utf-8') as file:
            file.write(text_area.get(1.0, END))

def show_creator():
    messagebox.showinfo("만든 이", "Made by 김길환!")

window = Tk()
window.title('Notepad')
window.geometry('400x400+800+300')
window.resizable(0,0)
window.iconbitmap("C:/WORK/notepad-icon_34386.ico")

text_area = Text(window, undo=True)
text_area.grid(sticky=N+E+S+W)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

menuMaker = Menu(window)

file_menu = Menu(menuMaker, tearoff=0)
file_menu.add_command(label='새 파일', command=new_file)
file_menu.add_command(label='저장', command=save_file)
file_menu.add_separator()
file_menu.add_command(label="종료", command=window.destroy)
menuMaker.add_cascade(label='파일', menu=file_menu)

menuMaker.add_command(label="만든 이", command=show_creator)

window.config(menu=menuMaker)

window.mainloop()
