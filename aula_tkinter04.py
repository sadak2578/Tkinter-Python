# não colocar from tkinter import * pois é uma má prática de programação

import tkinter

root = tkinter.Tk()
root.title('Aula 04 de Tkinter')
root.geometry('600x400')
root.resizable(False, False)
label = tkinter.Label(root, text="Início da Label", font=('Arial', 16))
label.pack()




root.mainloop()
