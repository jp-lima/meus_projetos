import tkinter as tk
from random import randint 
letras_encontradas = letras_escritas = ''
palavras_forca = ("abacaxi","computador",
    "elefante","python","futebol","astronauta","borboleta","guitarra","paralelepipedo","oceano","camaleao","biblioteca",
    "jardim","montanha","estrela","praia","vulcao","aviador","telefone","tigre","xadrez","magia","planeta","cachorro",
    "girassol","diamante","castelo","viagem","pinguim","harmonia", #30
)
palavra = (palavras_forca [randint(0,len(palavras_forca)-1)])

def obter_informacao():
    global tracinhos_da_forca 
    #tracinhos_da_forca = ''
    pal = palpite.get().lower().strip()
    global letras_escritas
    letras_escritas += pal
    if pal in palavra:
        tracinhos_da_forca = ''
        for verificar in palavra:
            if pal == verificar:
                tracinhos_da_forca += (f' { pal}')
                global letras_encontradas
                letras_encontradas += (f' { pal}')
            elif verificar in letras_encontradas:
                tracinhos_da_forca += (f' { verificar}')  
            else:
                tracinhos_da_forca += ' _'
    escrever.config(text=(tracinhos_da_forca))
    encontradas.config(text=(letras_escritas))
root = tk.Tk()
root.title('JOG0 DA FORC4')
#root.resizable(False,False)
root.geometry("800x600-210+40")
tracinhos_da_forca = ' _'* len(palavra)


encontradas = tk.Label (root, text= letras_escritas.strip(), font=("Courier", 20), justify="center")
encontradas.pack()

palpite = tk.Entry(root)  # Campo de entrada
palpite.pack()
escrever = tk.Label (root, text= tracinhos_da_forca.strip(), font=("Courier", 24), justify="center")
escrever.pack()

botao = tk.Button(root, text="Enviar", command=obter_informacao)  # Botão para capturar a entrada
botao.pack()


root.mainloop()