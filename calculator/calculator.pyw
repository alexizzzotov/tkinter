from tkinter import *
import math
root=Tk()
root.title('Калькулятор')

root.resizable(0,0)

frame1 = Frame(root)
frame1.pack(side=TOP, pady=5)

frame2 = Frame(root)
frame2.pack(side=LEFT, anchor=N, pady=5, padx=5)

text1=Entry(frame1, font='Arial 30', justify='right', bd=20, insertwidth=-1)
text1.pack(side=RIGHT, anchor=N)

#functions

def number_button(num):
    text1.insert(END, str(num))

def clear():
    text1.delete(0,END)

#1 ряд

b_n = Button(frame2, text='n!', width=3, bd=8, fg="blue",font='Arial 30')
b_n.grid(row =1, column = 1)
#clear
b_ce = Button(frame2, text='CE', width=3, bd=8, fg="blue",font='Arial 30', command=clear)
b_ce.grid(row =1, column = 2)

b_c = Button(frame2, text='C', width=3, bd=8, fg="blue",font='Arial 30')
b_c.grid(row =1, column = 3)

b_sqrt = Button(frame2, text='sqrt', width=3, bd=8, fg="blue",font='Arial 30')
b_sqrt.grid(row =1, column = 4)

b_exp = Button(frame2, text='^', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button('**'))
b_exp.grid(row =1, column = 5)

#2 ряд

b_7 = Button(frame2, text='7', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(7))
b_7.grid(row =2, column = 1)

b_8 = Button(frame2, text='8', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(8))
b_8.grid(row =2, column = 2)

b_9 = Button(frame2, text='9', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(9))
b_9.grid(row =2, column = 3)

b_line = Button(frame2, text='/', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button('/'))
b_line.grid(row =2, column = 4)

b_left = Button(frame2, text='(', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button('('))
b_left.grid(row =2, column = 5)

#3 ряд

b_4 = Button(frame2, text='4', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(4))
b_4.grid(row =3, column = 1)

b_5 = Button(frame2, text='5', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(5))
b_5.grid(row =3, column = 2)

b_6 = Button(frame2, text='6', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(6))
b_6.grid(row =3, column = 3)

b_mult = Button(frame2, text='*', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button('*'))
b_mult.grid(row =3, column = 4)

b_right = Button(frame2, text=')', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(')'))
b_right.grid(row =3, column = 5)

#4 ряд

b_1 = Button(frame2, text='1', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(1))
b_1.grid(row =4, column = 1)

b_2 = Button(frame2, text='2', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(2))
b_2.grid(row =4, column = 2)

b_3 = Button(frame2, text='3', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(3))
b_3.grid(row =4, column = 3)

b_minus = Button(frame2, text='-', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button('-'))
b_minus.grid(row =4, column = 4)

b_eq = Button(frame2, text='=', width=3, height=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button('='))
b_eq.grid(row =4, column = 5, rowspan=2)

#5 ряд

b_0 = Button(frame2, text='0', width=8, bd=8, fg="blue",font='Arial 30', command = lambda : number_button(0))
b_0.grid(row =5, column = 1, columnspan=2)

b_comma = Button(frame2, text=',', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button('.'))
b_comma.grid(row =5, column = 3)

b_plus = Button(frame2, text='+', width=3, bd=8, fg="blue",font='Arial 30', command = lambda : number_button('+'))
b_plus.grid(row =5, column = 4)

root.mainloop()
