import pyautogui
from time import sleep


# 1 - clicar e digitar meu usuario
pyautogui.click(970,540,duration=1)
pyautogui.write('teste')
# 2 - clicar e digitar minha senha
pyautogui.click(971,567,duration=1)
pyautogui.write('12345')
# 3 - clicar em "Entrar"
pyautogui.click(862,595)
# 4 - Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
#     1 - clicar e digitar produto
        pyautogui.click(695,528,duration=1)
        pyautogui.write(produto)
#     2 - clicar e digitar quantidade
        pyautogui.click(700,556,duration=1)
        pyautogui.write(quantidade)
#     3 - clicar e digitar preço
        pyautogui.click(700,582,duration=1)
        pyautogui.write(preco)
#     4 - clicar em registrar
        pyautogui.click(591,737,duration=1)
        sleep(1)
