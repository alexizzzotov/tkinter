from tkinter import *
root = Tk()

def summa(event):
    x1 = int(e1.get())
    x2 = int(e2.get())
    t3['text'] = str(x1+x2)

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
root.mainloop()
