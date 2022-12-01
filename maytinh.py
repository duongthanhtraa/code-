import tkinter
from tkinter import StringVar
def Click(numbers):
    global operator
    operator = operator + str(numbers)
    input.set(operator)

def Clear():
    global operator
    operator = ''
    input.set('')

def Equals():
    global operator
    result = str(eval(operator))
    input.set(result)


giaodien = tkinter.Tk()
giaodien.title("Calculator")
operator = ''


input = StringVar()

hienthi = tkinter.Entry(giaodien, width = 40, font = ('arial bold',20), textvariable = input, bg = 'aqua', justify ='right')
hienthi.grid(columnspan=4)

nutDel = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= 'C', bg='silver', command= Clear)
nutDel.grid(row=4, column=0)
nutPhay = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '.', bg='silver', command= lambda:Click('.'))
nutPhay.grid(row=4, column=1)
nut0 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '0', bg='silver', command= lambda:Click(0))
nut0.grid(row=4, column=2)
nutCong = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '+', bg='silver', command= lambda:Click('+'))
nutCong.grid(row=4, column=3)

nut1 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '1', command= lambda:Click(1),bg='silver')
nut1.grid(row=3, column=0)
nut2 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '2', bg='silver', command= lambda:Click(2))
nut2.grid(row=3, column=1)
nut3 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '3', bg='silver', command= lambda:Click(3))
nut3.grid(row=3, column=2)
nutTru = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '-', bg='silver', command= lambda:Click('-'))
nutTru.grid(row=3, column=3)

nut4 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '4', bg='silver', command= lambda:Click(4))
nut4.grid(row=2, column=0)
nut5 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '5', bg='silver', command= lambda:Click(5))
nut5.grid(row=2, column=1)
nut6 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '6', bg='silver', command= lambda:Click(6))
nut6.grid(row=2, column=2)
nutNhan = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= 'X', bg='silver', command= lambda:Click('X'))
nutNhan.grid(row=2, column=3)

nut7 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '7', bg='silver', command= lambda:Click(7))
nut7.grid(row=1, column=0)
nut8 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '8', bg='silver', command= lambda:Click(8))
nut8.grid(row=1, column=1)
nut9 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '9', bg='silver', command= lambda:Click(9))
nut9.grid(row=1, column=2)
nutChia = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '/', bg='silver', command= lambda:Click('/'))
nutChia.grid(row=1, column=3)

nutNgoac1 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= '(', bg='silver', command= lambda:Click('('))
nutNgoac1.grid(row=5, column=0)
nutNgoac2 = tkinter.Button(giaodien,padx=30, bd = 8, fg='black',font = ('arial bold',20),text= ')', bg='silver', command= lambda:Click(')'))
nutNgoac2.grid(row=5, column=1)
nutBang = tkinter.Button(giaodien,padx=95, bd = 8, fg='black',font = ('arial bold',20),text= '=', bg='silver', command= Equals)
nutBang.grid(row=5, column=2,columnspan=2)

giaodien.mainloop()