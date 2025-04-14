import tkinter as tk

root = tk.Tk()
root.title('aula 13 de tkinter')
root.geometry('670x450')

label1 = tk.Label(root, text='frase de teste 1', font=('Arial 15'), bd=1, relief='solid', width=15)
label1.pack()


root.mainloop()