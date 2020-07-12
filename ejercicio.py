from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("400x400")
ventana.config(
        bd=25
        )

#variables
num1 = StringVar()
num2 = StringVar()
resultado = StringVar()

#funciones
def multiplicar():
    try:
        resultado.set(float(num1.get()) * float(num2.get()))
        result()
    except:
        messagebox.showerror("error","Introduce bien los datos")
        limpiar()

def dividir():
    try:
        resultado.set(float(num1.get()) / float(num2.get()))
        result()
    except:
        messagebox.showerror("error", "Introduce bien los datos")
        limpiar()

def restar():
    try:
        resultado.set(float(num1.get()) - float(num2.get()))
        result()
    except:
        messagebox.showerror("error", "Introduce bien los datos")
        limpiar()

def sumar():
    try:
        resultado.set(float(num1.get()) + float(num2.get()))
        result()
    except:
        messagebox.showerror("error", "Introduce bien los datos")
        limpiar()

def result():
    messagebox.showinfo("resultado", f"El resultado de la operacion es: {resultado.get()}")
    limpiar()

def limpiar():
    num1.set('')
    num2.set('')

marco = Frame(ventana, width=305, height=200)
marco.config(
        padx= 15,
        pady= 15,
        bd=5,
        #relief=SOLID
        )
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

#campo para numero 1
lnum1 = Label(marco, text="Ingrese el numero 1: ")
lnum1.pack()

tnum1 = Entry(marco, textvariable=num1)
tnum1.pack()

#campo para numero 2
lnum2 = Label(marco, text="Ingrese el numero 2: ")
lnum2.pack()

tnum2 = Entry(marco, textvariable=num2)
tnum2.pack()

#botones
Button(marco, text='sumar', command= sumar).pack(side=LEFT, fill=X)
Button(marco, text='multiplicar', command= multiplicar).pack(side=LEFT, fill=X)
Button(marco, text='dividir', command = dividir).pack(side=LEFT, fill=X)
Button(marco, text='restar', command= restar).pack(side=LEFT, fill=X)

ventana.mainloop()
