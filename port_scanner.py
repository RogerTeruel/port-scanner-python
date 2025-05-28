import socket
import sys
print(r"""
╔═════════════════════════════════════════════════════════════════════════════════════╗
║                ██████╗                                                              ║
║     █████╗     ██╔══██╗     █████╗                                                  ║
║     █████║     ██████╔╝     █████║                                                  ║
║     █████║     ██╔██╔╝      █████║                                                  ║
║     █████║     ██║ ██╗      █████║                                                  ║
║     █████║     ╚═╝ ╚═╝      █████║                                                  ║
║     █████║                  █████║     Made for Cybersecurity & Pentesting          ║
║     █████████████████████████████║     LinkedIn --> www.linkedin.com/in/roger-tm    ║
║     █████████████████████████████║     GitHub ----> github.com/RogerTeruel          ║
║     █████╔══════════════════█████║     Email -----> rodhammer.forge@proton.me       ║
║     █████║   Powered by:    █████║                                                  ║
║     █████║                  █████║                                                  ║
║     █████║ RodHammer.forge  █████║                                                  ║
║     █████║                  █████║                                                  ║
║     █████║                  █████║                                                  ║
║     ╚════╝                  ╚════╝                                                  ║
╚═════════════════════════════════════════════════════════════════════════════════════╝
""")
def scan_ports(host, start_port, end_port):
    print(f"\n[+] Escaneando {host} desde el puerto {start_port} hasta {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[OPEN] Puerto {port}")
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Escaneo cancelado por el usuario.")
            sys.exit()
        except socket.gaierror:
            print("[!] Host no encontrado.")
            sys.exit()
        except socket.error:
            print("[!] Error de conexión.")
            sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python3 port_scanner.py <host> <puerto_inicial> <puerto_final>")
        sys.exit()

    target_host = sys.argv[1]
    port_start = int(sys.argv[2])
    port_end = int(sys.argv[3])

    scan_ports(target_host, port_start, port_end)
