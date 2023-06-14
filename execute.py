import os
import time

ciano = '\033[36m'
print(ciano)
os.system("clear")
print("atualizando...")
print("\n")
os.system("apt update && pkg upgrade")
os.system("clear")
print("instalando recursos necessários...")
print("\n")
os.system("pkg install python python2")
os.system("pip install netifaces")
os.system("pip install subprocess")
os.system("pip install intertools")
os.system("clear")
print("gerando wordlist...")
print("\n")
with open('p1.txt', 'w') as file:
    for i in range(10000):
        number = str(i).zfill(4)
        file.write(number + '\n')
with open('p2.txt', 'w') as file:
    for i in range(10000):
        number = str(i).zfill(4)
        file.write(number + '\n')
print("finalizado.")
print("\n")
resp=input("Deseja executar o script agora?[S/N] ")
if resp1=="S":
  os.system("python3 Script.py")
else:
  os.system("clear")
