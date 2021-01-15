import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+3000+500") # 가로x세로 + x좌표 + y좌표

menu = Menu(root)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both",expand=True,side="left")
scrollbar.config(command=txt.yview)

def open_file():
    with open("mynote.txt", "r", encoding="utf8") as mynote_open:
        txt.delete("1.0",END)
        txt.insert(END,mynote_open.read())

def save_file():
    with open("mynote.txt", "w", encoding="utf8") as mynote_save:
        save = txt.get("1.0",END)
        mynote_save.write(save)


menu_file = Menu(menu, tearoff=0)
if os.path.isfile("mynote.txt"):
    menu_file.add_command(label="열기", command=open_file)
else:
    menu_file.add_command(label="열기", command=open_file,state="disable")
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")


root.config(menu=menu)
root.mainloop() 