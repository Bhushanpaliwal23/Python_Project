# creation of 'GUI' based EMPLOYEE MANAGEMENT SYSTEM using 'SQL' and 'Python' and 'tkinter' liabrary


import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

win = Tk()
win.title('Employee Management System')
win.configure(bg = 'Skyblue')
win.geometry('1250x600')

def show():
    conn = mysql.connector.connect(user = 'root',password = 'Bhushan@23',
                              host = 'localhost',database = 'mydb')
    
    qur = 'select * from Employee'
    
    mycur = conn.cursor()
    mycur.execute(qur)
    list1 = mycur.fetchall()
    mycur.close()
    conn.close()
    for i in list1:
        treev.insert('',END, values = (i[0],i[1],i[2],i[3]))
    
def add():
    name = n1.get()
    mob_no = m1.get()
    dept = d1.get()
    salary = s1.get()
    if name=='' or mob_no=='' or dept=='' or salary=='':
        messagebox.showinfo('Warning!','Its mandatory to fill all the values') 
    else:
        conn = mysql.connector.connect(user = 'root',password = 'Bhushan@23',
                              host = 'localhost',database = 'mydb')
        
        qur = f'INSERT INTO Employee VALUES("{name}","{mob_no}","{dept}","{salary}")'
        
        mycur = conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('Sussessful','Data added susseccfully')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')
        
def salary():
    root = Tk()
    root.title('Salary Management')
    root.configure(bg = 'Skyblue')
    root.geometry('700x400')
    
    def disp():
        salary = e7.get()
        conn = mysql.connector.connect(user = 'root',password = 'Bhushan@23',
                              host = 'localhost',database = 'mydb')
    
        qur = f'select sal from Employee where mob = "{salary}"'
    
        mycur = conn.cursor()
        mycur.execute(qur)
        tup1 = mycur.fetchone()
        l8.config(text = tup1[0] +' '+ 'RS')
        mycur.close()
        conn.close()
    
    l7 = Label(root,text = 'ENTER MOB_NO', width = 15, bd = 5, relief = 'ridge')
    l7.place(x=100,y=100)
    sal1 = StringVar()
    e7 = Entry(root,width = 20, bd = 5, relief = 'ridge', textvariable = sal1)
    e7.place(x=300,y=100)
    b9 = Button(root, text = 'SHOW', bd = 5, relief = 'ridge', command = disp)
    b9.place(x=300,y=140)
    l8 = Label(root,text = 'SALARY', width = 20, bd = 5, relief = 'ridge')
    l8.place(x=100,y=180)
    
    root.mainloop()

def delete():
    delete = del1.get()
    
    if delete == '':
        messagebox.showinfo('Warning!','Its mandatory to fill all the values') 
    else:
        conn = mysql.connector.connect(user = 'root',password = 'Bhushan@23',
                              host = 'localhost',database = 'mydb')
        
        qur = f'DELETE FROM Employee where mob = "{delete}"'
        
        mycur = conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('Sussessful','Data deleted susseccfully')
        del1.set('')

def select():
    select = sel1.get()
    
    if select == '':
        messagebox.showinfo('Warning!','Its mandatory to fill all the values') 
    else:
        conn = mysql.connector.connect(user = 'root',password = 'Bhushan@23',
                              host = 'localhost',database = 'mydb')
        
        qur = f'select * from Employee where mob = "{select}"'
        
        mycur = conn.cursor()
        mycur.execute(qur)
        tup1 = mycur.fetchone()
        e1.insert(0,tup1[0])
        e2.insert(0,tup1[1])
        e3.insert(0,tup1[2])
        e4.insert(0,tup1[3])
        mycur.close()
        conn.close()

def update():
    select = sel1.get()
    name = n1.get()
    mob_no = m1.get()
    dept = d1.get()
    salary = s1.get()
    if name=='' or mob_no=='' or dept=='' or salary=='':
        messagebox.showinfo('Warning!','Its mandatory to fill all the values') 
    else:
        conn = mysql.connector.connect(user = 'root',password = 'Bhushan@23',
                              host = 'localhost',database = 'mydb')
        
        qur = f'UPDATE Employee SET NAME = "{name}",MOB = "{mob_no}",DEPT = "{dept}",SAL = "{salary}" WHERE MOB = "{select}"'
        
        mycur = conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('Sussessful','Data updated susseccfully')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')
        sel1.set('')

def clear():
    treev.delete(*treev.get_children())

# main label
l0 = Label(win,text = 'EMPLOYEE MANAGEMENT SYSTEM', bg = 'white', fg = 'black',
           bd = 5, relief = 'ridge', width = 40, font = ('times new roman', 16, 'bold'))
l0.pack()


# name label and entry
l1 = Label(win,text = 'EMPLOYEE NAME', bg = 'white', fg = 'black',
           bd = 5, relief = 'ridge', width = 20,font = ('times new roman', 12,'bold'))
l1.place(x=100,y=100)
n1 = StringVar()
e1 = Entry(win,text = 'enter name', bg = 'white', fg = 'black',textvariable = n1,
           bd = 5, relief = 'ridge', width = 40,font = ('times new roman', 12,'bold'))
e1.place(x=300,y=100)


# mob_no label and entry
l2 = Label(win,text = 'MOB_NO', bg = 'white', fg = 'black',
           bd = 5, relief = 'ridge', width = 20,font = ('times new roman', 12,'bold'))
l2.place(x=100,y=140)
m1 = StringVar()
e2 = Entry(win,text = 'Enter Mob No', bg = 'white', fg = 'black',textvariable = m1,
           bd = 5, relief = 'ridge', width = 40,font = ('times new roman', 12,'bold'))
e2.place(x=300,y=140)


# dept label and entry
l3 = Label(win,text = 'DEPARTMENT', bg = 'white', fg = 'black',
           bd = 5, relief = 'ridge', width = 20,font = ('times new roman', 12,'bold'))
l3.place(x=100,y=180)
d1 = StringVar()
e3 = Entry(win,text = 'Enter Dept', bg = 'white', fg = 'black',textvariable = d1,
           bd = 5, relief = 'ridge', width = 40,font = ('times new roman', 12,'bold'))
e3.place(x=300,y=180)


# salary label and entry
l4 = Label(win,text = 'SALARY', bg = 'white', fg = 'black',
           bd = 5, relief = 'ridge', width = 20,font = ('times new roman', 12,'bold'))
l4.place(x=100,y=220)
s1 = StringVar()
e4 = Entry(win,text = 'Enter Salary', bg = 'white', fg = 'black',textvariable = s1,
           bd = 5, relief = 'ridge', width = 40,font = ('times new roman', 12,'bold'))
e4.place(x=300,y=220)


# buttons for show , add , exit and salary

b1 = Button(win,text = 'Show', width = 15, command = show )
b1.place(x=150,y=260)

b2 = Button(win,text = 'Add', width = 15, command = add )
b2.place(x=350,y=260)

b3 = Button(win,text = 'Exit', width = 15, command = win.destroy )
b3.place(x=150,y=300)

b4 = Button(win,text = 'Salary', width = 15, command = salary )
b4.place(x=350,y=300)


# label, entry AND button  for the delete

l5 = Label(win,text = 'ENTER MOB_NO', bg = 'white', fg = 'black',
           bd = 5, relief = 'ridge', width = 20,font = ('times new roman', 12,'bold'))
l5.place(x=100,y=340)

del1 = StringVar()

e5 = Entry(win, bg = 'white', fg = 'black',textvariable = del1,
           bd = 5, relief = 'ridge', width = 40,font = ('times new roman', 12,'bold'))
e5.place(x=300,y=340)

b5 = Button(win,text = 'Delete', width = 15, command = delete )
b5.place(x=300,y=380)


# label,entry and buttons for Select and update 


l6 = Label(win, text = 'ENTER MOB_NO', bg = 'white', fg = 'black',
           bd = 5, relief = 'ridge', width = 20,font = ('times new roman', 12,'bold'))
l6.place(x=100,y=420)
sel1 = StringVar()
e6 = Entry(win, bg = 'white', fg = 'black',textvariable = sel1,
           bd = 5, relief = 'ridge', width = 40,font = ('times new roman', 12,'bold'))
e6.place(x=300,y=420)


b6 = Button(win,text = 'Select', width = 15, command = select )
b6.place(x=100,y=460)

b7 = Button(win,text = 'Update', width = 15, command = update )
b7.place(x=300,y=460)


# treeview
treev = ttk.Treeview(win,height = 15)
treev.place(x=700,y=100,width = 500)

treev["columns"] = ("1","2","3","4")
treev['show'] = 'headings'


treev.column("1", width = 90, anchor = 'c')
treev.column("2", width = 90, anchor = 'se')
treev.column("3", width = 90, anchor = 'se')
treev.column("4", width = 90, anchor = 'se')
             
treev.heading("1", text = 'NAME')
treev.heading("2", text = 'MOB_NO')
treev.heading("3", text = 'DEPT')
treev.heading("4", text = 'SALARY')

b7 = Button(win,text = 'Clear', width = 15, command = clear)
b7.place(x=900,y=460)
             

win.mainloop()
