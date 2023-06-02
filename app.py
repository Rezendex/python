import pyautogui
import keyboard
from time import sleep
login='rezende'
senha= '123456'

#cadastra 
def cadastra_usuario():
    pyautogui.click(975,610, duration=1)
    #pyautogui.click(961,538, duration=1)
    pyautogui.write(login)
    #pyautogui.click(956,578, duration=1)
    pyautogui.keyDown('tab')
    pyautogui.write(senha)
    pyautogui.click(943,615, duration=1)
#entra
def entrar():
    #pyautogui.click(954, 541, duration=1)
    pyautogui.write(login)
    #pyautogui.click(946, 576, duration=1)
    pyautogui.keyDown('tab')
    pyautogui.write(senha)
    pyautogui.click(848,609, duration=1)

#chamando as funções 
cadastra_usuario()
entrar()
with open ('produtos.txt', 'r') as arquivo:
        for linha in arquivo:
            produto= linha.split(',') [0]
            quantidade= linha.split(',') [1]
            preco= linha.split(',') [2]
            pyautogui.click(616,524, duration=1)
            pyautogui.write(produto)
            pyautogui.keyDown('tab')
            pyautogui.write(quantidade)
            pyautogui.keyDown('tab')
            pyautogui.write(preco)
            pyautogui.click(495,789, duration=1)
            if keyboard.is_pressed('Esc'):
             break
            sleep(1)