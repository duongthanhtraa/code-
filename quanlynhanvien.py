import tkinter
from tkinter.scrolledtext import ScrolledText
import connectsql
from tkinter import END


giaodien = tkinter.Tk()
giaodien.title("Quản lý nhân viên")

giaodien.geometry('600x400')

connection = connectsql.getConnection()
dulieu = connection.cursor()
ketnoi = connectsql.getConnection()

def kiemtraketnoi():
    if(connection.is_connected):
        label8.config(text = "Kết nối thành công")
    else:
        label8.config(text = "Kết nối không thành công")

def hienthinhanvien():
    dulieu.execute("SELECT * FROM Quan_ly_nhan_vien.Nhanvien")
    ketqua = dulieu.fetchall()
    scrolled.configure(state="normal")
    scrolled.delete("1.0", END)
    for i in ketqua:
        ketqua = str(i) + ","
        scrolled.configure(state="normal")
        scrolled.insert(tkinter.INSERT, ketqua + "\n")
        scrolled.configure(state = "disable")
    return 

def themnhanvien():
    ID = textbox1.get()
    Name = textbox2.get()
    Age = textbox3.get()
    Country = textbox4.get()
    Sex = textbox5.get()
    Position = textbox6.get()

    sql = "INSERT INTO Quan_ly_nhan_vien.`Nhanvien`(Id,Name,Age,Country,Sex,Position) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (ID,Name,Age, Country,Sex,Position)
    dulieu.execute(sql, val)

def xoanhanvien():
    ID = textbox1.get()
    sql = "DELETE FROM Quan_ly_nhan_vien.`Nhanvien` WHERE ID = %s"
    val = (ID,)
    dulieu.execute(sql,val)
    ketqua = dulieu.fetchall()
    ketnoi.commit()

def capnhatnhanvien():
    ID = textbox1.get()
    Name = textbox2.get()
    Age = textbox3.get()
    Country = textbox4.get()
    Sex = textbox5.get()
    Position = textbox6.get()
    sql = "UPDATE Quan_ly_nhan_vien.Nhanvien SET Name = %s, Age = %s, Country = %s, Sex = %s, Position = %s WHERE Id = %s"
    val = (Name,Age, Country,Sex,Position,ID)
    dulieu.execute(sql, val)
    ketqua = dulieu.fetchall()
    ketnoi.commit()

label1 = tkinter.Label(giaodien,text="CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN",fg="black",bg="white",font=("Arial Bold",15))
label1.grid(column=3,row=0)

label2 = tkinter.Label(giaodien,text="ID",fg="black",bg="white",font=("Arial Bold",10))
label2.grid(column=1,row=1)

label3 = tkinter.Label(giaodien,text="Name",fg="black",bg="white",font=("Arial Bold",10))
label3.grid(column=1,row=2)

label4 = tkinter.Label(giaodien,text="Age",fg="black",bg="white",font=("Arial Bold",10))
label4.grid(column=1,row=3)

label5 = tkinter.Label(giaodien,text="Country",fg="black",bg="white",font=("Arial Bold",10))
label5.grid(column=1,row=4)

label6 = tkinter.Label(giaodien,text="Sex",fg="black",bg="white",font=("Arial Bold",10))
label6.grid(column=1,row=5)

label7 = tkinter.Label(giaodien,text="Position",fg="black",bg="white",font=("Arial Bold",10))
label7.grid(column=1,row=6)

label8 = tkinter.Label(giaodien,text="",fg="black",bg="white",font=("Arial Bold",10))
label8.grid(column=3,row=11)

textbox1 = tkinter.Entry(giaodien,width=30)
textbox1.grid(column=3,row=1)

textbox2 = tkinter.Entry(giaodien,width=30)
textbox2.grid(column=3,row=2)

textbox3 = tkinter.Entry(giaodien,width=30)
textbox3.grid(column=3,row=3)

textbox4 = tkinter.Entry(giaodien,width=30)
textbox4.grid(column=3,row=4)

textbox5 = tkinter.Entry(giaodien,width=30)
textbox5.grid(column=3,row=5)

textbox6 = tkinter.Entry(giaodien,width=30)
textbox6.grid(column=3,row=6)

button1 = tkinter.Button(giaodien, text="Kiểm tra kết nối",fg="black",bg="white",command= kiemtraketnoi)
button1.grid(column=3,row=10)

button3 = tkinter.Button(giaodien, text="Thêm nhân viên",fg="black",bg="white",command= themnhanvien)
button3.grid(column=4,row=6)

button2 = tkinter.Button(giaodien, text="Hiển thị nhân viên",fg="black",bg="white",command= hienthinhanvien)
button2.grid(column=3,row=7)

button4 = tkinter.Button(giaodien, text="Cập nhật nhân viên",fg="black",bg="white",command= capnhatnhanvien)
button4.grid(column=4,row=7)

button4 = tkinter.Button(giaodien, text="Xóa nhân viên",fg="black",bg="white",command= xoanhanvien)
button4.grid(column=4,row=5)

scrolled = ScrolledText(giaodien,width=50,height = 10,state = "disable")
scrolled.grid(column=3,row=8)

giaodien.mainloop()