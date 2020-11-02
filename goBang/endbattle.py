import tkinter as tk
from tkinter import messagebox

# class quit_ui:
#     def __init__(self):
#         self.qui=tk.TK()
#         self.t_lable=tk.Label(self.qui,text='对方已经退出！')
#         self.ok_button=tk.Button(self.qui,text='OK')
# def quit_ui():
# def guiend(a):
#     a.destroy()
# top=tk.Tk()
# top.title("opps!")
# top.minsize(300,150)
# t_lable=tk.Label(top,text='对方已经退出！')
# ok_button=tk.Button(top,text='OK',command=guiend(top))
# t_lable.pack()
# ok_button.pack()
# top.mainloop()
# qiut=quit_ui()
class quit_ui:
    def __init__(self):
        
        self.top=tk.Tk()
        self.top.title("opps!")
        self.top.minsize(300,120)
        self.t_lable=tk.Label(self.top,text='对方已经退出！')
        self.ok_button=tk.Button(self.top,text='OK',command=self.endui)
        self.t_lable.pack()
        self.ok_button.pack()
        self.top.mainloop()
    def endui(self):
        self.top.destroy()
m=quit_ui()
