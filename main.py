from tkinter import *
from tkinter import Listbox
from tkinter import messagebox


def add():
    task = EntryTask.get()
    if task != "":
        listbox.insert(END, task)
        EntryTask.delete(0, END)
    else:
        messagebox.showwarning("Attenzione", "Per favore, inserisci una task")

def remove():
    try:
        select = listbox.curselection()[0]
        listbox.delete(select)
    except:
        messagebox.showwarning("Attenzione", "Per favore, seleziona una task da eliminare")

def save ():
    task = listbox.get(0, END)
    with open("tasks.txt", "w") as file:
        for item in task:
            file.write(item + "\n")
    messagebox.showinfo("Salvataggio", "Task salvate correttamente")
    

    










main = Tk()

# titolo finestra
main.title("ToDoList") 

# dimensioni finestra
main.geometry("900x600")

#widget per inserire le task
EntryTask = Entry(main, width=50)
EntryTask.pack(pady=10)

#bottone per aggiungere le task
ButtonAdd = Button(main, text="Aggiungi Task", command=add)
ButtonAdd.pack(pady=5)

#bottone per rimuovere le task
ButtonRemove = Button(main, text="Elimina Task", command=remove)
ButtonRemove.pack(pady=5)

#bottone per salvare le task su file
ButtonSave = Button(main, text="Salva Task", command=save)
ButtonSave.pack(pady=5)


# Creazione della Listbox prima del ciclo principale
listbox = Listbox(main, width=50, height=25)
listbox.pack(side=LEFT, fill=BOTH)

# Avvio del ciclo principale
main.mainloop()