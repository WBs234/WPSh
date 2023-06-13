import os
import time

os.system("clear")
print("atualizando...")
os.system("apt update && pkg upgrade")
os.system("clear")
print("instalando recursos necessários...")
os.system("pkg install python python2")
os.system("pip install netifaces")
os.system("pip install subprocess")
print("gerando wordlist...")
os.system("seq 10000000 15000000 > wordlistofc1.txt && seq 15000000 20000000 > wordlistofc2.txt && seq 20000000 25000000 > wordlistofc3.txt && seq 25000000 30000000 > wordlistofc4.txt && seq 30000000 35000000 > wordlistofc5.txt && seq 35000000 40000000 > wordlistofc6.txt && seq 40000000 45000000 > wordlistofc7.txt && seq 45000000 50000000 > wordlistofc8.txt && seq 50000000 55000000 > wordlistofc9.txt && seq 55000000 60000000 > wordlistofc10.txt && seq 60000000 65000000 > wordlistofc11.txt && seq 65000000 70000000 > wordlistofc12.txt && seq 70000000 75000000 > wordlistofc13.txt && seq 75000000 80000000 > wordlistofc14.txt && seq 80000000 85000000 > wordlistofc15.txt && seq 85000000 90000000 > wordlistofc16.txt && seq 95000000 99999999 > wordlistofc17.txt")
print("finalizado.")
