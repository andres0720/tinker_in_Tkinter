import tkinter as tk
from tkinter import Menu
root = tk.Tk()
root.geometry('300x300')
root.title("To Do List")
tasks = ['main']

#defining a menu bar window options
def file_new():
    pass
def file_open():
    pass
def file_save():
    pass
def file_exit():
    root.quit()

#setting up the menu bar
menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)  

file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Save", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=file_exit)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task) 
        entry.delete(0, tk.END)
        
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
        
buttonframe = tk.Frame(root)
buttonframe.pack(padx=5, pady=5)

entry = tk.Entry(root, font=('arial', 12))
entry.pack(padx=5, pady=5)


#create "Add Task Button"
btn1 = tk.Button(buttonframe, text='Add Task', font=('arial', 11), command=add_task)
btn1.pack(side="left", pady=10)

#Create the "Remove Task" button and associate the remove_task function with it
btn2 = tk.Button(buttonframe, text="Remove Task", font=('arial', 11), command=remove_task)
btn2.pack(side="left")

#display the task List box
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("arial", 12), height=10)
task_listbox.pack(padx=1, pady=1)


root.mainloop()