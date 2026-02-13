import os
import keyboard
import time

def 초기화() :
    os.system("cls" if os.name == "nt" else "clear")

def game():
    r = "ㅤ"
    y = ""
    while True:
        time.sleep(0.05)
        if keyboard.is_pressed("right"):
            초기화()
            r = r + 'ㅤ'
            print(y + r + "O]-")
        elif keyboard.is_pressed("left"):
            초기화()
            if len(r) > 0:
                r = r[:-1]
            print(y + r + "O]-")
        elif keyboard.is_pressed("down"):
            초기화()
            y = y + "\n"
            print(y + r + "O]-")
        elif keyboard.is_pressed("up"):
            초기화()
            if len(y) > 0:
                y = y[:-1]
            print(y + r + "O]-")
        elif keyboard.is_pressed("space"):
            초기화()
            print(y + r + 'O]-')
            time.sleep(0.05)
            초기화()
            print(y + r + 'O] -')
            time.sleep(0.05)
            초기화()
            print(y + r + 'O]  -')
            time.sleep(0.05)
            초기화()
            print(y + r + 'O]   -')
            time.sleep(0.05)
            초기화()
            print(y + r + 'O]    *')
            time.sleep(0.1)
            초기화()
            print(y + r + 'O]-')
초기화()
print("O]-")
game()