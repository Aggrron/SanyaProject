import tkinter as tk
from tkinter import *
from Q import question_list
from random import randrange
from tkinter import messagebox

w, h = 860, 400


def size_string(w, h):
    return str(w) + "x" + str(h)




root = tk.Tk()
root.title("Questions")
root.geometry(size_string(w, h))

questionFrame = tk.Frame(root, height=250, width=860)
questionFrame.pack(side=TOP)

buttonFrame = tk.Frame(root, height=150, width=860)
buttonFrame.pack(side=TOP)
#TEXT
label1 = Label(questionFrame, text="Вопрос:", font=("Courier", 20), justify=RIGHT)
label1.pack()

qLabel = Label(questionFrame, font=("Courier", 20), wraplength=860)
qLabel.pack()

var = IntVar()

a1 = Radiobutton(text="", variable=var, value=1)
a2 = Radiobutton(text="", variable=var, value=2)
a3 = Radiobutton(text="", variable=var, value=3)
a4 = Radiobutton(text="", variable=var, value=4)
a1.place(x=125, y=150)
a2.place(x=125, y=200)
a3.place(x=125, y=250)
a4.place(x=125, y=300)
a1.config(font=("Courier", 12), wraplength=860-125)
a2.config(font=("Courier", 12), wraplength=860-125)
a3.config(font=("Courier", 12), wraplength=860-125)
a4.config(font=("Courier", 12), wraplength=860-125)


corr_count = 0
q_count = 1
used = []
def onClick():
    global corr_count
    global q_count
    global question
    q_count += 1
    if var.get() == question.corr:
        corr_count += 1
    if q_count == 21:
        finish()
    qNum = randrange(len(question_list)-1)
    while qNum in used:
        qNum = randrange(len(question_list) - 1)
    used.append(qNum)
    question = question_list[qNum]
    q = question
    label1.config(text="Вопрос: " + str(q_count))
    qLabel.config(text=q.text)
    a1.config(text=q.a)
    a2.config(text=q.b)
    a3.config(text=q.c)
    a4.config(text=q.d)
    var.set(-1)

def finish():
    perc = corr_count/q_count * 100
    if perc <= 65:
        grade = 2
    elif 65 < perc <= 79:
        grade = 3
    elif 79 < perc < 90:
        grade = 4
    elif perc >= 90:
        grade = 5
    res_text = str("{0:.2f}".format(perc)) + '%' + '\n' + "Оценка: " + str(grade)
    text = str(corr_count) + '/' + str(q_count-1) + '\n' + res_text
    messagebox.showinfo("Результат", text)
    root.destroy()

#BUTTONS
butt1 = Button(text='Ответить', command=onClick)
butt1.place(x=50, y=300)

#First question
qNum = randrange(len(question_list)-1)
used.append(qNum)
question = question_list[qNum]
qLabel.config(text=question.text)
label1.config(text="Вопрос: " + str(q_count))
a1.config(text=question.a)
a2.config(text=question.b)
a3.config(text=question.c)
a4.config(text=question.d)














root.mainloop()
