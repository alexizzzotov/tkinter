from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import asksaveasfile, askopenfile

#глобальная переменная
FILE_NAME = NONE

def new_file():
    global FILE_NAME
    FILE_NAME = "Без имени"
    text.delete('1.0', END)

def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

def save_file():
    data = text.get('1.0', END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Упс!", message="Невозможно сохранить файл...")

def close_file():
    root.destroy()

def clear():
    text.delete(1.0, END)

def show_about():
    # второе окно (форма о программе)
    second = Tk()
    second.title('О программе')
    second.resizable(0, 0)
    second.geometry('200x200')
    lb1 = Label(second, text="Блокнот")
    lb2 = Label(second, text="Приятного использования!")
    lb3 = Label(second, text="© Изотов Александр")
    bt1 = Button(second, text="Закрыть", command=lambda: second.destroy())
    lb1.pack()
    lb2.pack()
    lb3.pack()
    bt1.pack()

def show_other():
    third = Tk()
    third.title('Окно программы')
    third.resizable(0, 0)
    third.geometry('300x300')
    lb1 = Label(third, text="Секретное окно")
    lb2 = Label(third, text="Можно закрыть")
    bt1 = Button(third, text="Закрыть", command=lambda: third.destroy())
    lb1.pack()
    lb2.pack()
    bt1.pack()

def show_help():
    showinfo(title="Помощь", message="Пусто...")

#Создаем основное окно
root=Tk()
root.title('Моя запись')

#Ограничиваем работу кнопки разворота окна
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

#Область для ввода текста
text = Text(root, font='Arial 20')
text.pack()

#Создать объект Меню на главном окне
menuBar =Menu(root)

#Создать пункт меню
fileMenu = Menu(menuBar)

#Пункт меню будет выпадающим
menuBar.add_cascade(label="Файл", menu=fileMenu)

#формируется список команд пункта меню
fileMenu.add_command(label = "Новый файл", command=new_file)
fileMenu.add_command(label = "Открыть...", command=open_file)
fileMenu.add_command(label="Сохранить...", command=save_file)
fileMenu.add_command(label="Сохранить как...", command=save_as)

#разделительная линия
fileMenu.add_separator()
fileMenu.add_command(label="Выход", command = close_file)

#Создаем второй выпадающий пункт меню
editMenu = Menu(menuBar)
menuBar.add_cascade(label="Редактировать", menu=editMenu)
editMenu.add_command(label = "Очистить все", command=clear)

#Создаем третий выпадающий пункт меню
helpMenu = Menu(menuBar)
menuBar.add_cascade(label="Помощь", menu=helpMenu)
helpMenu.add_command(label="Помощь", command=show_help)
helpMenu.add_command(label="О программе", command=show_about)

otherMenu = Menu(menuBar)
menuBar.add_cascade(label="Другое",menu=otherMenu )
otherMenu.add_command(label = "Нажми на меня!", command=show_other)

#Закрепляем объект Меню на главном окне
root.config(menu=menuBar)

root.mainloop()
