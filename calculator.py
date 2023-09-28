from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox
win=Tk()
#Add Title and icon
win.title("Calculator")
win.geometry('400x400')
b_title=Label(win,text="Calculator",font=font.Font(size=20))
photo=PhotoImage(file="C://Users//miriy//OneDrive//Desktop//calsi.png")
win.iconphoto(False, photo)
b_title.pack(side="top")

#Function to perform basic arithmetic oprations.
def operate():
    no_1 = (value1.get())
    no_2 = (value2.get())
    operator = opt.get()
    
    if operator == '+':
        
            if (no_1).isnumeric() and (no_2).isnumeric():
              result.set(float(no_1) + float(no_2))
            else:
              result.set( "Input is not a numeric value")
            
    elif operator == '-':
        
            if (no_1).isnumeric() and (no_2).isnumeric():
              result.set(float(no_1) -float( no_2))
            else:
               result.set( "Input is not a numeric value")
        
    elif operator == '*':
        
            if (no_1).isnumeric() and (no_2).isnumeric():
              result.set(float(no_1) * float(no_2))
            else:
              result.set( "Input is not a numeric value")
    elif operator == '/':
        if float(no_2) == 0:
                result.set("Division by zero error")
        else:
            
             if (no_1).isnumeric() and (no_2).isnumeric():
              result.set(float(no_1) /float( no_2))
             else:
              result.set( "Input is not a numeric value")
                
    elif operator == '%':
        
            if (no_1).isnumeric() and (no_2).isnumeric():
              result.set(float(no_1)% float(no_2))
            else:
             result.set( "Input is not a numeric value")
        
    else:
        result.set("!!! Invalid Input !!!") 
    
    
    
        

#add necessary buttons, textboxes.
f=Frame(win)
lab=Label(f,text="enter first value :",font=font.Font(size=15))
lab.pack(side="left")
value1=Entry(f,font="lucida 20 bold")
value1.pack(side="left",padx=10,pady=10)
f.pack()


f=Frame(win)
lab=Label(f,text="enter next value :",font=font.Font(size=15))
lab.pack(side="left")
value2=Entry(f,font="lucida 20 bold")
value2.pack(padx=10,pady=10)
f.pack()


f=Frame(win)
lab=Label(f,text="enter   operator :",font=font.Font(size=15))
lab.pack(side="left")
opt=Entry(f,font="lucida 20 bold")
opt.pack(padx=10,pady=10)
f.pack()

f=Frame(win)
lab=Button(f,text="Result",font=font.Font(size=15),command=operate)
lab.pack(side="left",padx=20,pady=20)
f.pack()

result = tk.StringVar()
result_label = tk.Label(win, textvariable=result,font=font.Font(size=20))
result_label.pack()

win.mainloop()