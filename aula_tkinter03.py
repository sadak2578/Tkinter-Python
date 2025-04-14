 # obs: lembrar de que se usar (from módulo import *) seria uma má prática de programação, não fazer isso, ou usar o módulo todo como import <módulo> ou partes do módulo
import tkinter
root = tkinter.Tk()
root.title('Aula 02 de Tkinter')
root.geometry('500x250+200+200')
root.resizable(True, True)

# root.minsize(width=500, height=250)
# root.maxsize(width=700, height=400)
root.state('iconic') # zoomed é para iniciar a aplicação na janela maximizada, e o iconic é para iniciar na janela minimizada
root.mainloop()