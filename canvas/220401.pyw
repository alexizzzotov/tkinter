from tkinter import *

def draw(event):
    canv.create_oval(30,30,90,90,fill='blue')

root = Tk()
root.geometry('400x400')
fr = Frame(root)
bt1 = Button(fr,width=8,text='Draw')
bt1.pack(side='left',padx=2)
fr.pack(pady=5)

canv = Canvas(root,width=800, height=550, bg='white')
canv.pack()

bt1.bind('<Button-1>',draw)

root.mainloop()
