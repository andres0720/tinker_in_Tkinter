import tkinter as tk

root = tk.Tk()
root.geometry('400x300')
root.title("To-Do List 1.1")
#Title
label = tk.Label(root, text="My To-Do List!", font=('arial', 18))
label.pack(padx=20, pady=20)

# textbox = tk.Text(root, height=1, font=('arial', 11))
# textbox.pack(padx=10, pady=10)

#define the button configuration
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
#define grid for the main buttons
btn1 = tk.Button(buttonframe, text='Add Task', font=('arial', 11))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='Delete A Task', font=('arial', 11))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='View Your Tasks', font=('arial', 11))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack(padx=10, pady=10)





root.mainloop()
