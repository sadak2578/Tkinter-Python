import tkinter

root = tkinter.Tk()
root.title('Aula6 Tkinter')
root.geometry("670x540")
root.resizable(False, False)

label1 = tkinter.Label(root, text="oi", font=('Arial', 15))
label1.pack(padx=2, pady= 12)



root.mainloop()
