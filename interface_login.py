import tkinter as tk
root = tk.Tk()
root.title('LOGIN')
root.geometry('350x120')
tk.Label (root,text='Usuário:' ).grid(row=0, column=0)
entrada_usuario=tk.Entry (root)
entrada_usuario.grid(row=0,column=1)

tk.Label (root,text='Senha:').grid(row=4,column=0)
entrada_senha =tk.Entry (root)
entrada_senha.grid(row=4,column=1)

def pegar_usuario_senha():
    usur = entrada_usuario.get()
    senha = entrada_senha.get()
    print (usur,senha)
tk.Button(root, text='Enviar', command=pegar_usuario_senha).grid(row=5,columnspan=2)
tk.mainloop()