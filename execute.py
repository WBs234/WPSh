import os
import time

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
os.system("clear")
print("gerando wordlist...")
print("\n")


print("finalizado.")
