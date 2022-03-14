
from tkinter import *
from tkinter import messagebox
def a1():
    a.delete(0, END)
    b.delete(0,END)
def b1():
    messagebox.showinfo("Asliddin", a.get()+"    "+b.get()+"  "+"QALAYSIZ KATTA BOLA 😂😂😂😂😂😂️")
root=Tk()
root.title('mamatraimov')
ism=Label(text="isminizni kiriting katta bola ")
familiya=Label(text="familiyangizni kiriting katta bolla  ")
ism.grid(row=0, column=0 )
familiya.grid(row=1, column=0 )
a=Entry()
b=Entry()
a.grid(row=0, column=1 ,padx=10,pady=10)
b.grid(row=1, column=1 ,padx=10,pady=10)
btn=Button(text="DELETE", command=a1)
btn1=Button(text="OK", command=b1)
btn.grid(row=2, column=0 ,padx=10,pady=10  )
btn1.grid(row=2, column=1 ,padx=10,pady=10  )
root.mainloop()
