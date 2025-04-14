import tkinter as tk

root = tk.Tk()
root.title('aula de tkinter 12')
root.geometry('700x500')

label1 = tk.Label(
	root, 
	text='frase1',
	font='Arial 20',
	bd=10,
	relief='solid'
	
).pack()
label2 = tk.Label(
	root, 
	text='frase2',
	font='Arial 20',
	bd=10,
	relief='solid'
	
).pack()
label3 = tk.Label(
	root, 
	text='frase3',
	font='Arial 20',
	bd=10,
	relief='solid'
	
).pack()
label4 = tk.Label(
	root, 
	text='frase4',
	font='Arial 20',
	bd=10,
	relief='solid'
	
).pack()
label5 = tk.Label(
	root, 
	text='frase5',
	font='Arial 20',
	bd=10,
	relief='solid'
	
).pack()
label6 = tk.Label(
	root, 
	text='frase6',
	font='Arial 20',
	bd=10,
	relief='solid'
	
).pack()


root.mainloop()