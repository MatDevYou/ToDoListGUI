from tkinter import *
from tkinter import Listbox
from tkinter import messagebox

def add():
    '''
    Variabili:
    - task: contiene il testo inserito dall'utente
    
    Funzionalità:
    Permette all'utente di inserire un'attività nella lista. Se il campo di input non è vuoto, 
    l'attività viene aggiunta alla listbox e il campo di input viene cancellato. 
    Se il campo di input è vuoto, viene mostrato un messaggio di avviso.
    '''
    task = EntryTask.get()
    if task != "":
        listbox.insert(END, task)
        EntryTask.delete(0, END)
    else:
        messagebox.showwarning("Attenzione", "Per favore, inserisci una task")

# Funzione per rimuovere l'attività selezionata dalla lista
def remove():
    '''
    Variabili:
    - select: contiene l'indice dell'attività selezionata nella listbox
    
    Funzionalità:
    Permette all'utente di rimuovere un'attività selezionata dalla lista. Se un'attività è 
    selezionata, viene rimossa dalla listbox. Se nessuna attività è selezionata, viene mostrato 
    un messaggio di avviso.
    '''
    try:
        select = listbox.curselection()[0]
        listbox.delete(select)
    except:
        messagebox.showwarning("Attenzione", "Per favore, seleziona una task da eliminare")

# Funzione per salvare le attività in un file
def save():
    '''
    Variabili:
    - task: contiene tutte le attività presenti nella listbox
    
    Funzionalità:
    Permette all'utente di salvare tutte le attività presenti nella lista in un file di testo 
    chiamato "tasks.txt". Ogni attività viene scritta su una nuova riga del file. Dopo il salvataggio, 
    viene mostrato un messaggio di conferma.
    '''
    task = listbox.get(0, END)
    with open("tasks.txt", "w") as file:
        for item in task:
            file.write(item + "\n")
    messagebox.showinfo("Salvataggio", "Task salvate correttamente")
    


main = Tk()

# titolo finestra
main.title("ToDoList") 

# dimensioni finestra
main.geometry("900x650")

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

