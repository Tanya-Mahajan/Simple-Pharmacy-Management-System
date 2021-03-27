from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title("Simple Pharmacy Management System")
root.configure(bg='MINT CREAM')
root.geometry("1100x700")



var=-1

# Add new item
def additem():
    global var
    num_lines = 0
    with open("database_proj", 'r') as f10:
        for line in f10:
            num_lines += 1
    var=num_lines-1
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    e6=entry6.get()
    with open("database_proj", 'a+') as f12:
        f12.write('{0} {1} {2} {3} {4} {5}\n'.format(str(e1), e2, e3, str(e4), e5, str(e6)))

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)

# Delete item
def deleteitem():
    e1=entry1.get()
    with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
        for line in f:
            print(line)
            if str(e1) not in line:
                working.write(line)
    f.close()
    working.close()
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)

# View first item
def firstitem():
    global var
    var=0
    try:
        with open("database_proj") as f:
            f.seek(var)
            c = f.readline()

        v=list(c.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)


        entry1.insert(0,str(v[0]))
        entry2.insert(0,str(v[1]))
        entry3.insert(0,str(v[2]))
        entry4.insert(0,str(v[3]))
        entry5.insert(0,str(v[4]))
        entry6.insert(0, str(v[5]))
    except:
        messagebox.showinfo("Title", "SORRY ! NO RECORDS TO SHOW")

# View next item
def nextitem():
    global var
    var = var + 1
    try:
        with open("database_proj") as f:
            f.seek(var)
            c=f.readlines()
        xyz = c[var]
        v = list(xyz.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)

        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
        entry6.insert(0, str(v[5]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

# view previous item
def previousitem():
        global var
        var=var-1

        try:
            with open("database_proj") as f:
                f.seek(var)
                z = f.readlines()
            xyz=z[var]
            v = list(xyz.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)

            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
            entry6.insert(0, str(v[5]))
        except:
            messagebox.showinfo("Title", "SORRY!...NO PREVIOUS RECORDS")

# View last item
def lastitem():
    global var
    with open("database_proj",'r') as f4:
        x = f4.read().splitlines()

    last_line= x[-1]
    num_lines = 0
    with open("database_proj", 'r') as f8:
        for line in f8:
            num_lines += 1
    var=num_lines-1
    print(last_line)
    try:
        v = list(last_line.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)

        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
        entry6.insert(0, str(v[5]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")

# Update item
def updateitem():

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    e6 = entry6.get()
    with open(r"database_proj") as f1, open(r"database_proj1", "w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4} {5}'.format(str(e1), e2, e3, str(e4), e5, str(e6)))
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")

# Search item
def searchitem():
    i=0
    flag = False
    e11 = entry1.get()
    with open(r"database_proj") as working:
        for line in working:
            i=i+1
            if str(e11) in line:
                flag = True
                break
    if flag:
        try:
            v = list(line.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)

            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
            entry6.insert(0, str(v[5]))
        except:
            messagebox.showinfo("Title", "error end of file")
    working.close()

# Clear item
def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)

# Creating labels and input box(entry)
label0= Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bd="2",bg="skyblue1",fg="black",font=("Times", 30))
label1=Label(root,text="ENTER ITEM NAME",bg="skyblue1",relief="sunken",fg="black",font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12))
label2=Label(root, text="ENTER ITEM PRICE",bd="2",relief="sunken",height="1",bg="skyblue1",fg="black", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 12))
label3=Label(root, text="ENTER ITEM QUANTITY",bd="2",relief="sunken",bg="skyblue1",fg="black", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 12))
label4=Label(root, text="ENTER ITEM CATEGORY",bd="2",relief="sunken",bg="skyblue1",fg="black", font=("Times", 12),width=25)
entry4= Entry(root, font=("Times", 12))
label5=Label(root, text="ENTER ITEM DISCOUNT",bg="skyblue1",relief="sunken",fg="black", font=("Times", 12),width=25)
entry5= Entry(root, font=("Times", 12))
label6=Label(root, text="ENTER EXPIRE DATE",bg="skyblue1",relief="sunken",fg="black", font=("Times", 12),width=25)
entry6= Entry(root, font=("Times", 12))

# Creating button
button1= Button(root, text="ADD ITEM", bg="white", fg="black",relief="sunken", width=20, font=("Times", 12),activebackground="red",command=additem)
button2= Button(root, text="DELETE ITEM", bg="white", fg="black",relief="sunken", width =20, font=("Times", 12),activebackground="red",command=deleteitem)
button3= Button(root, text="VIEW FIRST ITEM" , bg="white", fg="black",relief="sunken", width =20, font=("Times", 12),activebackground="red",command=firstitem)
button4= Button(root, text="VIEW NEXT ITEM" , bg="white", fg="black",relief="sunken", width =20, font=("Times", 12),activebackground="red", command=nextitem)
button5= Button(root, text="VIEW PREVIOUS ITEM", bg="white", fg="black",relief="sunken", width =20, font=("Times", 12),activebackground="red",command=previousitem)
button6= Button(root, text="VIEW LAST ITEM", bg="white", fg="black",relief="sunken", width =20, font=("Times", 12),activebackground="red",command=lastitem)
button7= Button(root, text="UPDATE ITEM", bg="white", fg="black",relief="sunken", width =20, font=("Times", 12),activebackground="red",command=updateitem)
button8= Button(root, text="SEARCH ITEM", bg="white", fg="black",relief="sunken", width =20, font=("Times", 12),activebackground="red",command=searchitem)
button9= Button(root, text="CLEAR SCREEN", bg="white", fg="black",relief="sunken", width=20, font=("Times", 12),activebackground="red",command=clearitem)

# Adding image
Image = PhotoImage(file="Pharmacy3.png")
background = Label(image=Image, bd=2)
background.grid(row=0, columnspan=6, padx=10, pady=10)

label0.grid(row=1,columnspan=6, padx=10, pady=10)
label1.grid(row=3,column=0, sticky=W, padx=10, pady=10)
label2.grid(row=4,column=0, sticky=W, padx=10, pady=10)
label3.grid(row=5,column=0, sticky=W, padx=10, pady=10)
label4.grid(row=6,column=0, sticky=W, padx=10, pady=10)
label5.grid(row=7,column=0, sticky=W, padx=10, pady=10)
label6.grid(row=8,column=0, sticky=W, padx=10, pady=10)

entry1.grid(row=3,column=1, padx=40, pady=10)
entry2.grid(row=4,column=1, padx=10, pady=10)
entry3.grid(row=5,column=1, padx=10, pady=10)
entry4.grid(row=6,column=1, padx=10, pady=10)
entry5.grid(row=7,column=1, padx=10, pady=10)
entry6.grid(row=8,column=1, padx=10, pady=10)

button1.grid(row=3,column=4, padx=40, pady=10)
button2.grid(row=3,column=5, padx=40, pady=10)
button3.grid(row=4,column=4, padx=40, pady=10)
button4.grid(row=4,column=5, padx=40, pady=10)
button5.grid(row=5,column=4, padx=40, pady=10)
button6.grid(row=5,column=5, padx=40, pady=10)
button7.grid(row=6,column=4, padx=40, pady=10)
button8.grid(row=7,column=4, padx=40, pady=10)
button9.grid(row=8,column=4, padx=40, pady=10)

root.mainloop()
