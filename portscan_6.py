# Code by: SAYKE - ISL
# Github: https://github.com/NullByteCode


import sys
import socket


logo = """
██████╗  ██████╗  ██████╗ ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗██╔════╝
██║  ██║██║   ██║██║   ██║██████╔╝███████╗
██║  ██║██║   ██║██║   ██║██╔══██╗╚════██║
██████╔╝╚██████╔╝╚██████╔╝██║  ██║███████║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
---------------- by SAYKE ----------------
------------------ ISL -------------------

(01) Enter The Port
(02) Default
(03) Full
(00) Exit
"""


def portscan_manual():
    try:
        host = input("\033[1;97m[+] Enter the target: \033[0;0m")
        ports = input("\033[1;97m[+] Enter the ports: \033[0;0m")
        for port in ports.split(","):
            sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, int(port)))
            if result == 0:
                print("---------------------------------")
                print("\033[1;32m[✓] Port {} is open.\033[0;0m".format(port))
            else:
                print("---------------------------------")
                print("\033[1;31m[✘] Port {} is closed.\033[0;0m".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("\n \033[1;91m[!] Exiting program.\033[0;0m")
        sys.exit()
    except socket.gaierror:
        print("\033[1;91m[!] Hostname could not be resolved.\033[0;0m")
        sys.exit()
    except socket.timeout:
        print("\033[1;91m[!] Connection timed out.\033[0;0m")
        sys.exit()
    except socket.error:
        print("\033[1;91m[!] Couldn't connect to server.\033[0;0m")
        sys.exit()


def portscan_default():
    try:
        host = input("\033[1;97m[+] Enter the target: \033[0;0m")
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("---------------------------------")
                print("\033[1;32m[✓] Port {} is open.\033[0;0m".format(port))
            else:
                print("---------------------------------")
                print("\033[1;31m[✘] Port {} is closed.\033[0;0m".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("\n \033[1;91m[!] Exiting program.\033[0;0m")
        sys.exit()
    except socket.gaierror:
        print("\033[1;91m[!] Hostname could not be resolved.\033[0;0m")
        sys.exit()
    except socket.timeout:
        print("\033[1;91m[!] Connection timed out.\033[0;0m")
        sys.exit()
    except socket.error:
        print("\033[1;91m[!] Couldn't connect to server.\033[0;0m")
        sys.exit()


def portscan_full():
    try:
        host = input("\033[1;97m[+] Enter the target: \033[0;0m")
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("---------------------------------")
                print("\033[1;32m[✓] Port {} is open.\033[0;0m".format(port))
            else:
                print("---------------------------------")
                print("\033[1;31m[✘] Port {} is closed.\033[0;0m".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("\n \033[1;91m[!] Exiting program.\033[0;0m")
        sys.exit()
    except socket.gaierror:
        print("\033[1;91m[!] Hostname could not be resolved.\033[0;0m")
        sys.exit()
    except socket.timeout:
        print("\033[1;91m[!] Connection timed out.\033[0;0m")
        sys.exit()
    except socket.error:
        print("\033[1;91m[!] Couldn't connect to server.\033[0;0m")
        sys.exit()


def main():
    while True:
        print("\033[1;94m" + logo + "\033[0;0m")

        ent = input("\033[1;97m[+] Enter the option:\033[0;0m")

        if (ent == "01"):
            portscan_manual()
            break
        elif (ent == "02"):
            portscan_default()
            break
        elif (ent == "03"):
            portscan_full()
            break
        elif (ent == "00"):
            print("\033[1;97m[~] Exiting...\033[0;0m")
            break
        else:
            print("\033[1;97m[~] Invalid option.\033[0;0m")


if __name__ == "__main__":
    main()
