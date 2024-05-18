import socket
from colorama import init, Fore, Style

# Inicializar colorama
init()

def print_banner():
    banner = """
    ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░

    """
    print(Fore.YELLOW + banner + Style.RESET_ALL)

def print_menu():
    menu = """
    Seleccione una opción:
    1. Escanear puertos
    2. Resolver nombre de dominio a dirección IP
    3. Salir
    """
    print(Fore.CYAN + menu + Style.RESET_ALL)

def scan_ports(target, start_port, end_port):
    print(f"Escaneando puertos del {start_port} al {end_port} eno {target}")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"{Fore.GREEN}Puerto {port}: Abierto{Fore.RESET}")
        else:
            print(f"{Fore.RED}Puerto {port}: Cerrado{Fore.RESET}")
        sock.close()

def resolve_domain(domain):
    ip = socket.gethostbyname(domain)
    print(f"El nombre de dominio {domain} se resuelve a la dirección IP: {ip}")

# Si el script se ejecuta directamente, mostrar el banner y el menú
if __name__ == "__main__":
    print_banner()

    while True:
        print_menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            target = input("Ingrese la dirección IP o el dominio a escanear: ")
            start_port = int(input("Ingrese el puerto inicial: "))
            end_port = int(input("Ingrese el puerto final: "))
            scan_ports(target, start_port, end_port)
        elif opcion == "2":
            domain = input("Ingrese el nombre de dominio que desea resolver: ")
            resolve_domain(domain)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida del menú.")