import tkinter
from time import sleep
root = tkinter.Tk()
root.title('aula 05 de tkinter')
root.geometry('700x550')
root.resizable(False, False)

def btn_um():
	label.destroy()
	btn2.destroy()
	label2 = tkinter.Label(root, text='hehehe vc clicou no botão, saindo do código', font=('Times New Roman',15,'italic'))
	label2.pack(padx=0, pady=25)
	sleep(1)
	
	root.after(4000, root.quit)

def btn_dois():
	label.destroy()
	btn1.destroy()
	label3 = tkinter.Label(root, text='muahahaha vc clicou aqui dinoooovo', font=('Times New Roman', 15, 'italic'))
	label3.pack(padx=0, pady=35)
	sleep(1)
	
	root.after(4000, root.quit)

label = tkinter.Label(root, text='Título aqui', font=('Times New Roman',15,'italic'))
label.pack()

btn1 = tkinter.Button(root, text='clique aqui', command=btn_um)
btn1.pack(padx=0, pady=20)

btn2 = tkinter.Button(root, text='clique aqui dnv', command=btn_dois)
btn2.pack(padx=0, pady=30)

root.mainloop()