import tkinter as tk

root = tk.Tk()
root.title('Aula 11 de Tkinter')
# root.geometry('780x560')

label1 = tk.Label(root, text='Este é um label 1', font='Arial 10',fg='red', width=20, height=15)
label1.pack()
label2 = tk.Label(root, text='Este é um label 2', font='Arial 50',fg='red', width=20, height=15)
label2.pack()


root.mainloop()