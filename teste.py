import pandas as pd
n = '33'
# Ler o arquivo CSV
df = pd.read_csv("lista_contatos.csv")

# Apagar a linha pelo índice
df.drop(51, axis='index', inplace=True)

# Salvar o DataFrame atualizado de volta no arquivo CSV
df.to_csv("lista_contatos.csv", index=False)
#print (df.index)
#for linha in df.index:
   # print (linha)
print (len(n))