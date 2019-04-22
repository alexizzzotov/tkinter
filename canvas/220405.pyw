from tkinter import *
from random import randint,choice

colors = ['black' , 'blue' , 'red']

def draw_10(event):
    count=0
    for i in range(10):
        R = randint(10, 40)
        x = randint(R, 300 - R)
        y = randint(R, 300 - R)
        color = choice(colors)
        canv.create_oval(x-R, y-R, x+R, y+R, fill=color)
        if color == 'red':
            count += 1
    print(count,' circle(s)')

root = Tk()
root.geometry('400x400')
fr = Frame(root)
bt1 = Button(fr,width=8,text='Draw')
bt1.pack(side='left',padx=2)
fr.pack(pady=5)

canv = Canvas(root,width=800, height=550, bg='white')
canv.pack()

bt1.bind('<Button-1>',draw_10)

root.mainloop()
