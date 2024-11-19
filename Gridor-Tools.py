import subprocess
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

# Diccionario de servicios para optimizacióna
services = {
    "Administración de autenticación de Xbox Live": "XblAuthManager",
    "Servicio de red de Xbox Live": "XboxNetApiSvc",
    "Partida guardada de Xbox Live": "XblGameSave",
    "Servicio de directivas de diagnóstico": "DPS",
    "Tarjeta inteligente": "SCardSvr",
    "Servicio de enumeración de tarjetas inteligentes": "ScDeviceEnum",
    "Servicio enrutador de SMS de Microsoft Windows": "SmsRouter",
    "Servicio telefónico": "PhoneSvc",
    "Ubicador de llamada a procedimiento remoto (RPC)": "RpcLocator",
    "Windows Mixed Reality OpenXR Service": "MixedRealityOpenXRSvc",
    "Servicio Accessory Management de Xbox": "XboxGipSvc"
}

# Función para animar el ASCII art
def animated_ascii():
    ascii_art = r"""
   _____                                                                                                                                       _____ 
  ( ___ )                                                                                                                                     ( ___ )
   |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
   |   |                                                                                   ,----,                                              |   | 
   |   |                                                                                 ,/   .`|                                              |   | 
   |   |   ,----..                                                                     ,`   .'  :                         ,--,                 |   | 
   |   |  /   /   \               ,--,          ,---,                                ;    ;     /                       ,--.'|                 |   | 
   |   | |   :     :    __  ,-. ,--.'|        ,---.'|    ,---.     __  ,-.         .'___,/    ,'     ,---.      ,---.   |  | :                 |   | 
   |   | .   |  ;. /  ,' ,'/ /| |  |,         |   | :   '   ,'\  ,' ,'/ /|         |    :     |     '   ,'\    '   ,'\  :  : '      .--.--.    |   | 
   |   | .   ; /--`   '  | |' | `--'_         |   | |  /   /   | '  | |' |         ;    |.';  ;    /   /   |  /   /   | |  ' |     /  /    '   |   | 
   |   | ;   | ;  __  |  |   ,' ,' ,'|      ,--.__| | .   ; ,. : |  |   ,'         `----'  |  |   .   ; ,. : .   ; ,. : '  | |    |  :  /`./   |   | 
   |   | |   : |.' .' '  :  /   '  | |     /   ,'   | '   | |: : '  :  /               '   :  ;   '   | |: : '   | |: : |  | :    |  :  ;_     |   | 
   |   | .   | '_.' : |  | '    |  | :    .   '  /  | '   | .; : |  | '                |   |  '   '   | .; : '   | .; : '  : |__   \  \    `.  |   | 
   |   | '   ; : \  | ;  : |    '  : |__  '   ; |:  | |   :    | ;  : |                '   :  |   |   :    | |   :    | |  | '.'|   `----.   \ |   | 
   |   | '   | '/  .' |  , ;    |  | '.'| |   | '/  '  \   \  /  |  , ;                ;   |.'     \   \  /   \   \  /  ;  :    ;  /  /`--'  / |   | 
   |   | |   :    /    ---'     ;  :    ; |   :    :|   `----'    ---'                 '---'        `----'     `----'   |  ,   /  '--'.     /  |   | 
   |   |  \   \ .'              |  ,   /   \   \  /                                                                      ---`-'     `--'---'   |   | 
   |   |   `---`                 ---`-'     `----'                                                                                             |   | 
   |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
  (_____)                                                                                                                                     (_____)
    """
    for line in ascii_art.splitlines():
        print(Fore.CYAN + line)
        time.sleep(0.05)

# Función para mostrar el menú principal
def show_main_menu():
    print(f"\n{Fore.YELLOW}Menú Principal:")
    print(f"{Fore.GREEN}1. Instalar Programas")
    print(f"{Fore.GREEN}2. Descargar Repositorios")
    print(f"{Fore.GREEN}3. Herramientas de Escritorio")
    print(f"{Fore.RED}4. Salir")

# Submenú de instalación de programas
def show_install_menu():
    print(f"\n{Fore.YELLOW}Menú de Instalación:")
    print(f"{Fore.GREEN}1. Instalar Discord")
    print(f"{Fore.GREEN}2. Instalar Chrome")
    print(f"{Fore.GREEN}3. Instalar Python")
    print(f"{Fore.GREEN}4. Instalar Visual Studio Code")
    print(f"{Fore.RED}5. Volver")

# Submenú de descargas
def show_download_menu():
    print(f"\n{Fore.YELLOW}Menú de Descargas:")
    print(f"{Fore.GREEN}1. Descargar Reverse Shell")
    print(f"{Fore.GREEN}2. Descargar RAT Discord")
    print(f"{Fore.RED}3. Volver")

# Submenú de herramientas de escritorio
def show_tools_menu():
    print(f"\n{Fore.YELLOW}Menú de Herramientas de Escritorio:")
    print(f"{Fore.GREEN}1. Obtener Contraseña Wi-Fi")
    print(f"{Fore.GREEN}2. Optimización de Servicios")
    print(f"{Fore.RED}3. Volver")

# Función para optimizar servicios
def disable_service(service_name, display_name):
    try:
        print(f"Intentando detener el servicio: {display_name} ({service_name})")
        subprocess.run(f"net stop {service_name}", shell=True, check=True)
        print(f"Deshabilitando el servicio: {display_name} ({service_name})")
        subprocess.run(f"sc config {service_name} start= disabled", shell=True, check=True)
        print(f"{Fore.GREEN}Servicio '{display_name}' deshabilitado con éxito.")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error al deshabilitar el servicio '{display_name}'. Puede que ya esté deshabilitado o no exista.")

def optimize_services():
    print(Fore.CYAN + "Iniciando optimización de servicios...")
    for display_name, service_name in services.items():
        disable_service(service_name, display_name)
    print(Fore.GREEN + "Optimización completada.")

# Función para obtener la contraseña del Wi-Fi actual
def get_wifi_password():
    try:
        network_data = os.popen("netsh wlan show interfaces").read()
        ssid_line = [line for line in network_data.split("\n") if "SSID" in line and "BSSID" not in line]
        if not ssid_line:
            return "No estás conectado a ninguna red Wi-Fi."
        
        ssid = ssid_line[0].split(":")[1].strip()
        wifi_data = os.popen(f'netsh wlan show profile name="{ssid}" key=clear').read()
        password_line = [line for line in wifi_data.split("\n") if "Key Content" in line]
        if password_line:
            password = password_line[0].split(":")[1].strip()
            return f"El SSID es: {ssid}\nLa contraseña es: {password}"
        else:
            return f"El SSID es: {ssid}\nNo se encontró una contraseña (podría ser una red abierta o sin permisos)."
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"

# Función para ejecutar comandos
def ejecutar_comando(command):
    subprocess.run(["cmd", "/c", command], shell=True)

# Función para instalar programas
def instalar_programa(opcion):
    comandos = {
        "1": "winget install -e --id Discord.Discord",
        "2": "winget install -e --id Google.Chrome",
        "3": "winget install -e --id Python.Python.3",
        "4": "winget install -e --id Microsoft.VisualStudioCode",
    }
    comando = comandos.get(opcion, "")
    if comando:
        ejecutar_comando(comando)
        print(f"{Fore.GREEN}Instalación completada.")
    else:
        print(Fore.RED + "Opción no válida para instalación.")

# Función para descargar repositorios
def descargar_repositorio(opcion):
    repositorios = {
        "1": "git clone https://github.com/Maalfer/ReverseShell_Python.git",
        "2": "git clone https://github.com/rodrigog898/Discord-rat.git",
    }
    comando = repositorios.get(opcion, "")
    if comando:
        ejecutar_comando(comando)
        print(f"{Fore.GREEN}Descarga completada.")
    else:
        print(Fore.RED + "Opción no válida para descarga.")

# Menú principal
def main():
    while True:
        animated_ascii()
        show_main_menu()
        opcion_principal = input(f"{Fore.CYAN}Selecciona una opción: ")

        if opcion_principal == "1":
            while True:
                show_install_menu()
                opcion_instalar = input(f"{Fore.CYAN}Selecciona una opción: ")
                if opcion_instalar == "5":
                    break
                instalar_programa(opcion_instalar)

        elif opcion_principal == "2":
            while True:
                show_download_menu()
                opcion_descargar = input(f"{Fore.CYAN}Selecciona una opción: ")
                if opcion_descargar == "3":
                    break
                descargar_repositorio(opcion_descargar)

        elif opcion_principal == "3":
            while True:
                show_tools_menu()
                opcion_tools = input(f"{Fore.CYAN}Selecciona una opción: ")
                if opcion_tools == "1":
                    print(Fore.CYAN + get_wifi_password())
                elif opcion_tools == "2":
                    optimize_services()
                elif opcion_tools == "3":
                    break
                else:
                    print(Fore.RED + "Opción no válida. Intenta nuevamente.")

        elif opcion_principal == "4":
            print(f"{Fore.RED}Saliendo...")
            break
        else:
            print(f"{Fore.RED}Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
