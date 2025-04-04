import os
import random

#numeros_sorteados=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]


while True:
    numeros_sorteados=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    numero=random.choice(numeros_sorteados)
    
    if numero == 32:
        print(f"Parabens o numero sorteado é: {numero}")
        break
    else:
        continue

  
'''
def spac():
    print(" \n "* 3)
    
def ml():
    print("\033[;32m===\033[m"*15)
    
def num5():
    print("                     ===           ")
    print("                 === \033[7;31m   \033[m ===          ")
    print(f"              ===  \033[7;31m       \033[m  ===    ")
    print(f"             ===  \033[7;31m    5    \033[m  ===    ")
    print(f"              ===  \033[7;31m       \033[m  ===    ")
    print("                 === \033[7;31m   \033[m ===    ")
    print("                     ===           ")
    ml()
    
def num4():
    print("                     ===           ")
    print("                 === \033[7;32m   \033[m ===          ")
    print(f"              ===  \033[7;32m       \033[m  ===    ")
    print(f"             ===  \033[7;32m    4    \033[m  ===    ")
    print(f"              ===  \033[7;32m       \033[m  ===    ")
    print("                 === \033[7;32m   \033[m ===    ")
    print("                     ===           ")
    ml()
    
def num3():
    print("                     ===           ")
    print("                 === \033[7;33m   \033[m ===          ")
    print(f"              ===  \033[7;33m       \033[m  ===    ")
    print(f"             ===  \033[7;33m    3    \033[m  ===    ")
    print(f"              ===  \033[7;33m       \033[m  ===    ")
    print("                 === \033[7;33m   \033[m ===    ")
    print("                     ===           ")
    ml()
    
def num2():
    print("                     ===           ")
    print("                 === \033[7;34m   \033[m ===          ")
    print(f"              ===  \033[7;34m       \033[m  ===    ")
    print(f"             ===  \033[7;34m    2    \033[m  ===    ")
    print(f"              ===  \033[7;34m       \033[m  ===    ")
    print("                 === \033[7;34m   \033[m ===    ")
    print("                     ===           ")
    ml()
    
def num1():
    print("                     ===           ")
    print("                 === \033[7;35m   \033[m ===          ")
    print(f"              ===  \033[7;35m       \033[m  ===    ")
    print(f"             ===  \033[7;35m    1    \033[m  ===    ")
    print(f"              ===  \033[7;35m       \033[m  ===    ")
    print("                 === \033[7;35m   \033[m ===    ")
    print("                     ===           ")
    ml()
    
def numC():
    print('        \033[7;33m   O GANHADOR É O NUMERO   \033[m')
    print("                     ===           ")
    print("                 === \033[7;36m   \033[m ===          ")
    print(f"              ===  \033[7;36m       \033[m ===    ")
    print(f"             ===  \033[7;36;47m    {numero}    \033[m ===    ")
    print(f"              ===  \033[7;36m       \033[m ===    ")
    print("                 === \033[7;36m   \033[m ===    ")
    print("                     ===           ")
    ml()
  
  
#cabeçalho
def intro():
    spac
    ml()
    print("\033[7;34m|          SORTEADOR TEC.INFORMATICA        |\033[m")
    ml()

#sorteadores
def sort5():
    os.system("cls")
    intro()
    num5()
    enter=str(input(" \n   \033[7;32m   TECLES ENTER PARA CONTINUAR   \033[m"))
    sort4()
    
def sort4():
    os.system("cls")
    intro()
    num4()
    enter=str(input(" \n  \033[7;32m   TECLES ENTER PARA CONTINUAR   \033[m"))
    sort3()
    
def sort3():
    os.system("cls")
    intro()
    num3()
    enter=str(input(" \n  \033[7;32m   TECLES ENTER PARA CONTINUAR   \033[m"))
    sort2()

def sort2():
    os.system("cls")
    intro()
    num2()
    enter=str(input(" \n  \033[7;32m   TECLES ENTER PARA CONTINUAR   \033[m"))
    sort1()

def sort1():
    os.system("cls")
    intro()
    num1()
    enter=str(input(" \n  \033[7;32m   TECLES ENTER PARA CONTINUAR   \033[m"))
    sortC()
    
def sortC():
    os.system("cls")
    intro()
    numC()
    spac()
    spac()

  
    
os.system("cls")

    
sort5()

'''