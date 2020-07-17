from tkinter import *

ventana = Tk()

ventana.geometry('500x500')
ventana.title('APP Tkinter')
ventana.minsize(500,500)

#campos de cada ventana

#variables 

products = []
name_data= StringVar()
price_data= StringVar()



#funciones

def añadir():
    products.append([
        name_data.get(),
        price_data.get(),
        add_entry_description.get('1.0', 'end-1c')
        ])

    name_data.set("")
    price_data.set("")
    add_entry_description.delete('1.0', END)
    home()


def home():
    home_label.config(
            fg='white',
            bg='black',
            font=('arial',30),
            padx=210,
            pady=20
            )
    home_label.grid(row=0, column=0)

    frame_home.grid(row=1)

    #listar
    for pro in products:
        if len(pro) == 3:
            pro.append('AÑADIDO')
            Label(frame_home, text=pro[0]).grid()
            Label(frame_home, text=pro[1]).grid()
            Label(frame_home, text=pro[2]).grid() 
            Label(frame_home, text='------------').grid()

    #eliminar
    add_label.grid_remove()
    info_label.grid_remove()
    info_label_creador.grid_remove()
    frame.grid_remove()

def info():
    info_label.config(
            fg='white',
            bg='black',
            font=('arial',30),
            padx=150,
            pady=20
            )
    info_label.grid(row=0, column=0)
    info_label_creador.config()
    info_label_creador.grid(row=1, column=0)

    #eliminar
    add_label.grid_remove()
    home_label.grid_remove()
    frame.grid_remove()
    frame_home.grid_remove()

def add():
    add_label.config(
            fg='white',
            bg='black',
            font=('arial',30),
            padx=120,
            pady=20
            )
    add_label.grid(row=0,column=0, columnspan=6)

    #campos
    frame.grid()

    add_label_name.grid(row=1, column=0, padx=5, pady=5)
    add_entry_name.grid(row=1, column=2, padx=5, pady=5)

    add_label_price.grid(row=2, column=0, padx=5, pady=5)
    add_entry_price.grid(row=2, column=2, padx=5, pady=5)
    
    add_label_description.grid(row=3, column=0, padx=5, pady=5)
    add_entry_description.grid(row=3, column=2, padx=5, pady=5)
    add_entry_description.config(
            width=30,
            height=5
            )

    boton.grid(row=4, column=2)

    #eliminar
    home_label.grid_remove()
    info_label.grid_remove()
    info_label_creador.grid_remove()
    frame_home.grid_remove()

#home
home_label = Label(ventana, text='Inicio')
frame_home = Frame(ventana, width=250)

#add
add_label = Label(ventana, text='Añadir producto')

frame = Frame(ventana)

add_label_name = Label(frame, text='Nombre:')
add_entry_name = Entry(frame, textvariable= name_data)

add_label_price = Label(frame, text='Precio:')
add_entry_price = Entry(frame, textvariable= price_data)

add_label_description = Label(frame, text='Descripcion')
add_entry_description = Text(frame)

boton = Button(frame, text='Guardar', command= añadir)


#info
info_label = Label(ventana, text='Información')
info_label_creador = Label(ventana, text='Andres Camilo Plaza Jimenez 2020')

home()

#menu
menu = Menu(ventana)
menu.add_command(label='Inicio', command= home)
menu.add_command(label='Añadir', command= add)
menu.add_command(label='Información', command= info )
menu.add_command(label="Salir", command=ventana.quit)

#añadir menu
ventana.config(
        menu= menu
        )




ventana.mainloop()
