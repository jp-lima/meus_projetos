import pyautogui
import time
import pandas
pyautogui.PAUSE=0.8
pyautogui.hotkey('winleft')
time.sleep(2)
pyautogui.write('firefox')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
time.sleep(2)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')  
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=856, y=406)
pyautogui.write('jotagol157@gmail.com')
pyautogui.press('tab')
pyautogui.write('2007*11')
pyautogui.press('enter')
pyautogui.click(x=837, y=291)
produtos = pandas.read_csv('produtos.csv')
for linha in produtos.index:
    pyautogui.click(x=895, y=290)
    codigo = produtos.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    marca = produtos.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo  = produtos.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')
    categoria = produtos.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    preço_unitario  = produtos.loc[linha, 'preco_unitario']
    pyautogui.write(str(preço_unitario))
    pyautogui.press('tab')
    custo = produtos.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    obs = produtos.loc[linha, 'obs']
    pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)