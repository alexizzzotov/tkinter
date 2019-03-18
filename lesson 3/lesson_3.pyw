from tkinter import *

root = Tk()

def summa(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    t3['text'] = str(x1+x2)

def minus(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    s = str(x1-x2)
    v2.set(s)

def delenie(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    t5['text'] = str(x1/x2)

def umnozhenie(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    t6['text'] = str(x1*x2)

def clear(event):
    e1.delete(0, END)
    e2.delete(0, END)
    s = ''
    t3['text'] = ''
    v2.set(s)
    
t1 = Label(root, text = 'Введите первое число')
t1.pack()
e1 = Entry(root)
e1.pack(pady=5)

t1 = Label(root, text = 'Введите второе число')
t1.pack(pady=5)
e2 = Entry(root)
e2.pack(pady=5)

btn = Button(root, text = 'Сложить', width = 10, font = 'Arial 14')
btn.pack(pady=5)
btn.bind('<Button-1>',summa)
t3 = Label(root, font = 'Arial 20')
t3.pack()

btn2 = Button(root, text = 'Вычесть', width = 10, font = 'Arial 14')
btn2.pack(pady=5)
btn2.bind('<Button-1>',minus)
v2 = StringVar()
t4 = Label(root, textvariable = v2, font = 'Arial 20')
t4.pack()

btn3 = Button(root, text = 'Разделить', width = 10, font = 'Arial 14')
btn3.pack(pady=5)
btn3.bind('<Button-1>',delenie)
t5 = Label(root, font = 'Arial 20')
t5.pack()

btn4 = Button(root, text = 'Умножить', width = 10, font = 'Arial 14')
btn4.pack(pady=5)
btn4.bind('<Button-1>',umnozhenie)
t6 = Label(root, font = 'Arial 20')
t6.pack()

btn5 = Button(root, text = 'Очистить', width = 10, font = 'Arial 14')
btn5.pack(pady=5)
btn5.bind('<Button-1>',clear)

root.mainloop()
