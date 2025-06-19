import tkinter as tk

login_user_pass = {

    "usuário":"megaprt",
    "senha":"senha1234"

}

root = tk.Tk()
root.title("Login")
root.geometry("670x540")

def clear_screen():
    usuario_frame.pack_forget()
    label_user.pack_forget()
    caixa_entrada_usuario.pack_forget()
    caixa_entrada_senha.pack_forget()
    b1.pack_forget()
    senha_frame.pack_forget()
    senha_label.pack_forget()

def mostrar_tela():
    usuario_frame.pack(pady=5)
    label_user.pack(side="left")
    senha_frame.pack(pady=5)
    senha_label.pack(side="left")
    caixa_entrada_usuario.pack()
    caixa_entrada_senha.pack()
    b1.pack(pady=20)

def botaovolta():
    clear_screen()
    for widget in root.pack_slaves():
        if widget not in [logo_label, usuario_frame, label_user, caixa_entrada_usuario, senha_frame, senha_label, caixa_entrada_senha, b1]:
            widget.pack_forget()
    caixa_entrada_usuario.delete(0, tk.END)
    caixa_entrada_senha.delete(0, tk.END)
    mostrar_tela()

def apertar_botao():
    user = caixa_entrada_usuario.get()
    password = caixa_entrada_senha.get()
    if user == login_user_pass['usuário'] and password == login_user_pass['senha']:
        clear_screen()

        l2 = tk.Label(root, text="bem vindo ao sistema!")
        l2.pack(pady=(20,5))

    else:
        clear_screen()

        label_erro = tk.Label(root, text='erro, seu usuário não corresponde')
        label_erro.pack(pady=(20,5))
    b_voltar = tk.Button(root, text="Voltar", command=botaovolta)
    b_voltar.pack(pady=(5,20))

# colocar a logo
logo = tk.PhotoImage(file="C:\\Users\\SadakWho\\Desktop\\MegaPrint_projetc\\area-testes\\testelogin\\imagem2.png")
logo = logo.subsample(5,)
logo_label = tk.Label(root, image=logo)
logo_label.pack(padx=0, pady=0)

# usuário
usuario_frame = tk.Frame(root)
usuario_frame.pack(pady=5)
label_user = tk.Label(usuario_frame, text="Usuário:")
label_user.pack(side="left")

caixa_entrada_usuario = tk.Entry(usuario_frame, width=40)
caixa_entrada_usuario.pack(side="left")

# senha
senha_frame = tk.Frame(root)
senha_frame.pack(pady=5)
senha_label = tk.Label(senha_frame, text="Senha:   ")
senha_label.pack(side="left")
caixa_entrada_senha = tk.Entry(senha_frame, width=40, show="*")
caixa_entrada_senha.pack(side="left")

# botão
b1 = tk.Button(root, text='Entrar', border=2, command=apertar_botao)
b1.pack(padx=5)

root.mainloop()
