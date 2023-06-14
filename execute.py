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
with open('pin1.txt', 'w') as file:
    for i in range(10000):
        number = str(i).zfill(4)
        file.write(number + '\n')
with open('pin2.txt', 'w') as file:
    for i in range(10000):
        number = str(i).zfill(4)
        file.write(number + '\n')
print("finalizado.")
printf("\n")
resp=input("Deseja executar o script agora?[S/N] ")
resp1==resp.upper()
if resp1==S:
  os.system("python3 Script.py")
else:
  os.system("clear")
