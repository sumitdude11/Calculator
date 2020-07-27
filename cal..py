from tkinter import *
import tkinter.messagebox
import time
import random

operator =""
operator1=""
d=""# global variable operator
##creating window and its geometry ###

rt = Tk()
rt.config(background="orange")
rt.geometry("380x750+200+2")
rt.title("calc")

## creating frame ###
'''top = Frame(rt,width =150,height=10,bg="orange" ,relief = SUNKEN)
top.pack(side =TOP)'''
left=Frame(rt,width=1,height=50,bg="blue",relief=SUNKEN)
left.pack(side=LEFT)
right = Frame(rt,width=1250,height=750,bg="green",relief=SUNKEN)
right.pack(side=RIGHT)

## creating calc ##
txt = StringVar()
txt2 = StringVar()
e1 = Entry(right,textvariable=txt2,width=9,bg="aqua",font=("arial",55),justify='right')
e1.grid(row=2,columnspan=295,rowspan=1,column=1)
e2 = Entry(right,textvariable=txt,width=9,bg="aqua",font=("arial",55),justify='right')
e2.grid(row=1,columnspan=295,rowspan=1,column=1)

def l(txt2):
    b(txt2)


def b3():
    global operator1
    global operator
    global d
    if(d=="+"):
        operator=float(operator)
        operator1=float(operator1)
        txt2.set("%d+%d="%(operator1,operator)) 
        operator=operator+operator1
        txt.set(str(operator))
    elif(d=="-"):
        operator=float(operator)
        operator1=float(operator1)
        txt2.set("%d-%d="%(operator1,operator)) 
        operator=float(operator1)-float(operator)
        txt.set(str(operator))
    elif(d=="*"):
        operator=float(operator)
        operator1=float(operator1)
        txt2.set("%dx%d="%(operator1,operator)) 
        operator=float(operator1)*float(operator)
        txt.set(str(operator))
    elif(d=="/"):
        operator=float(operator)
        operator1=float(operator1)
        txt2.set("%d/%d="%(operator1,operator)) 
        operator=float(operator1)/float(operator)
        txt.set(str(operator))
    elif(d=="%"):
        operator=float(operator)
        operator1=float(operator1)
        txt2.set("%d%d="%(operator1,operator)) 
        operator=float(operator1)%float(operator)
        txt.set(str(operator))


    
def b1(sign):
    global operator1
    global operator
    global d
    operator1=str(operator)
    operator=""
    d=sign
    txt2.set(operator1+sign)
    
    #txt.set(operator)

def bv():
    if(d!=""):
        b3()
    

def b(num2):
    global operator
    global operator1
    global d
    operator=str(operator)+str(num2)
    txt2.set(operator)
    txt2.set(operator1+d+operator)
    bv()
   # txt.set(operator)
    
def b2():
    global operator
    global operator1
    
    operator=str(operator)
    operator1=str(operator1)
    operator=(operator[:-1])
    operator1=(operator1[:-1])
    txt.set(str(operator))
    txt2.set(str(operator1))
def b101(num3):
    global operator
    global operator1
    global d
    operator=str(num3)
    operator1=str(num3)
    d=num3
    txt.set(operator)
    txt2.set(operator)
  
#=============first row button=====#
b11 = Button(right,text="C",padx=14,pady=5,bd=3,fg="black",bg="yellow",font=("arial",34),command =lambda: b101(""))
b11.grid(row=3,column=7)
b12 = Button(right,text="/",padx=16,pady=5,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda:b1("/"))
b12.grid(row=3,column=8)
b13 = Button(right,text="X",padx=14,pady=8,bd=3,fg="black",bg="yellow",font=("arial",30),command=lambda:b1("*"))
b13.grid(row=3,column=9)
b14 = Button(right,text="⌫",padx=1,pady=5,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda:b2())
b14.grid(row=3,column=10)

#=============second row button=====#
b100 = Button(right,text="7",padx=18,pady=12,bd=3,fg= "black",bg="yellow",font=("arial",34),command=lambda: b(7))
b100.grid(row=4,column=7)
b200=Button(right,text="8",padx=12,pady=12,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(8))
b200.grid(row=4,column=8)
b300 = Button(right,text="9",padx=12,pady=12,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(9))
b300.grid(row=4,column=9)
b8 = Button(right,text="-",padx=22,pady=12,bd=3,fg= "black",bg="yellow",font=("arial",34),command=lambda: b1("-"))
b8.grid(row=4,column=10)

#=============third row button=====#
b11 = Button(right,text="+",padx=17,pady=12,bd=3,fg= "black",bg="yellow",font=("arial",34),command=lambda: b1("+"))
b11.grid(row=5,column=10)

b6=Button(right,text="6",padx=12,pady=12,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(6))
b6.grid(row=5,column=9)
b7=Button(right,text="5",padx=12,pady=12,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(5))
b7.grid(row=5,column=8)
b8=Button(right,text="4",padx=18,pady=12,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(4))
b8.grid(row=5,column=7)

#=============fourth row button=====#
b4 = Button(right,text="3",padx=12,pady=3,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(3))
b4.grid(row=6,column=8)
b5 = Button(right,text="2",padx=12,pady=3,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(2))
b5.grid(row=6,column=9)
b5 = Button(right,text="1",padx=18,pady=3,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(1))
b5.grid(row=6,column=7)
b15 = Button(right,text="=",padx=15,pady=50,bd=5,fg= "black",bg="yellow",font=("arial",34),command=lambda: b3())
b15.grid(column=10,rowspan=2,row=6)
#=============fifth row button=====#
b6 = Button(right,text="%",padx=12,pady=3,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b1("%"))
b6.grid(row=7,column=7)
b9= Button(right,text="0",padx=12,pady=3,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b(0))
b9.grid(row=7,column=8)
b10 = Button(right,text=".",padx=18,pady=3,bd=3,fg="black",bg="yellow",font=("arial",34),command=lambda: b("."))
b10.grid(row=7,column=9)

#====================top====#
'''w=Label(top,text="WELCOME TO OUR TRANSPORT",fg="red",font=("Colonna MT",70,'bold'))
w.place(x=0,y=0)
local_time=time.asctime(time.localtime(time.time()))
w1=Label(top,font=('DigifaceWide',15,'bold','italic','underline'),text=local_time,bg="yellow",width=40,fg="black",bd=10)
w1.grid(row=1,column=0)'''
#==========left===#




