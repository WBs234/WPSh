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
os.system(""""seq -w 0 9999 | while read -r number; do printf "%04d\n" "$number"; done > pin1.txt && seq -w 0 999 | while read -r number; do printf "%04d\n" "$number"; done > pin2.txt"""")
print("finalizado.")
printf("\n")
resp=input("Deseja executar o script agora?[S/N] ")
resp1==resp.upper()
if resp1==S:
  os.system("python3 Script.py")
else:
  os.system("clear")
