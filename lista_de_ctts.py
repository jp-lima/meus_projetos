import pandas as pd;import tkinter as tk;from time import sleep  
ctts_encontrados = ''
tabela = pd.read_csv('lista_contatos.csv')
def pesquisa():
      pesquisado = entrada_ctt.get().title()
      #tabela = pd.read_csv('lista_contatos.csv')
      n = 'continuar'
      ctts_encontrados = str()
      while n == 'continuar':
        for linha in tabela.index:
                nome=tabela.loc[linha, 'Nome']
                email=tabela.loc[linha, 'Email']
                telefone=tabela.loc[linha, 'Telefone']   
                contato_inteiro = f'{nome} // {email} // {telefone}'
                if pesquisado in nome or pesquisado in email or pesquisado in telefone:

                        ctts_encontrados += f'''
{contato_inteiro}'''
                        global indice
                        indice = str(linha)
        mostrar_os_contatos_encontrados.config(text=ctts_encontrados)
        n = 'parar'
        global contato
        contato = ctts_encontrados.splitlines()
        print (contato)


def apagador():
     vai_ser_apagado = (contato[1])
     for indices in tabela.index: 
        n = tabela.loc[indices, 'Nome']
        if n in vai_ser_apagado :
                tabela.drop(indices, axis='index', inplace=True)
                tabela.to_csv("lista_contatos.csv", index=False)
                sleep(1)
                aviso_q_vai_ser_apagado.config(text='CONFIRMADO! CONTATO DELETADO', font=('times new roman', 16))




def limpar_frame():
    for widget in frame.winfo_children():
        widget.pack_forget()

def apagar_ctt():
    limpar_frame()
    aviso=tk.Label(root,text="Digite o nome ou número que você deseja apagar", font=('times new roman',12), justify=('center'))
    aviso.pack()
    entrada_ctt.pack()
    button_pesquisador.pack()
    titulo_dos_contatos_encontrados.pack()
    mostrar_os_contatos_encontrados.pack()
    button_apagador.place(x=440,y=50)    
    aviso_q_vai_ser_apagado.place(x=40,y=50)
def adicionar_ctt():
        n=1


def encontrar_ctt():
        limpar_frame()
        aviso=tk.Label(root,text="Digite o nome ou número que você deseja encontrar", font=('times new roman',12), justify=('center'))
        aviso.pack()
        entrada_ctt.pack()
        button_pesquisador.pack()
        titulo_dos_contatos_encontrados.pack()
        mostrar_os_contatos_encontrados.pack()
        
root = tk.Tk()
root.title('LISTA DE CONTATOS')
root.geometry('800x600-210+40')
frame = tk.Frame(root)
frame.pack()

#2-BUSCADOR DOS CONTATOS
entrada_ctt = tk.Entry(root)
button_pesquisador=tk.Button (root, text="ENVIAR",font=('times new roman', 10) ,command=pesquisa)
mostrar_os_contatos_encontrados = tk.Label(root, text=ctts_encontrados, font=('times new roman',13), justify=('center'))
titulo_dos_contatos_encontrados = tk.Label(root, text='Nome // E-mail // Telefone')
escolha = tk.Label(frame,text='Escolha uma das opções',font=('Courier',15) ,justify=('center'))
escolha.pack()
#////////////

#3- APAGAR OS CONTATOS
button_apagador  = tk.Button (root, text='APAGAR', font=('times new roman', 10,) ,command=apagador,bg='red')
aviso_q_vai_ser_apagado = tk.Label(root, text='Aperte "APAGAR" para deletar o primeiro contato da linha abaixo dos seus contatos', font=('times new roman', 10,),justify='left' )

#////////////

#1-primeiro frame
button_encontrar=tk.Button (frame, text="BUSCAR CONTATO",font=('times new roman', 10) ,command=encontrar_ctt)
button_encontrar.pack()
button_apagar=tk.Button(frame, text="APAGAR CONTATO",font=('times new roman', 10) ,command=apagar_ctt)
button_apagar.pack()
button_adicionar=tk.Button(frame, text="ADICIONAR CONTATO",font=('times new roman', 10) ,command=adicionar_ctt)
button_adicionar.pack()
#//////

tk.mainloop()


#criar três botões para o usuário escolher
        # 1.encontrar contato
        # 2.apagar contato
 #4.adicionar contato
print ('jatal') 