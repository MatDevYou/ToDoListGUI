from tkinter import *
from tkinter import Listbox

main = Tk()

# titolo finestra
main.title("ToDoList") 

# dimensioni finestra
main.geometry("900x600")

# Creazione della Listbox prima del ciclo principale
listbox = Listbox(main, width=50, height=25)
listbox.pack(side=LEFT, fill=BOTH)

# Avvio del ciclo principale
main.mainloop()