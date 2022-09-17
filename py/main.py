from tkinter import *
from tkinter import messagebox  
#функция обработки нажатия
def clicked_btn1():
    messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')
def clicked_btn2():
    quit()
window = Tk() #создание окна
window.title('Окна и кнопки') #заголовок окна
window.geometry('400x250') #размеры окна
lbl = Label(window, text='Кнопка', font=('Arial Bold', 30))
lbl.grid(column=0, row=0)
#вызов функции clicked() при нажатии кнопки
btn1 = Button(window, text='Уведомление', command=clicked_btn1)
btn2 = Button(window, text='KILL', command=clicked_btn2)
btn1.grid(column=1, row=0)
btn2.grid(column=2, row=0)
window.mainloop() #бесконечный цикл окна, окно ждёт нажатий
