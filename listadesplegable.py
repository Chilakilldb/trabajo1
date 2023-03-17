import tkinter as tk
ventana = tk.Tk()
ventana.title("lista desplegable")

ventana.geometry('380x300+1200+100')
ventana.configure(background='dark turquoise')
var=tk.StringVar(ventana)
var.set('rojo')
opciones=['azul', 'rojo', 'morado', 'cafe', 'verde', 'gris']
opcion=tk.OptionMenu(ventana, var, *opciones)
opcion.config(width=20)
opcion.pack(side='left', padx=30, pady=30)


ventana.mainloop()