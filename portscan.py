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
        host = input("Enter the target: ")
        ports = input("Enter the ports: ")
        for port in ports.split(","):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, int(port)))
            if result == 0:
                print("Port {} is open.".format(port))
            else:
                print("Port {} is closed.".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.timeout:
        print("Connection timed out.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()


def portscan_default():
    try:
        host = input("Enter the target: ")
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("Port {} is open.".format(port))
            else:
                print("Port {} is closed.".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.timeout:
        print("Connection timed out.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()


def portscan_full():
    try:
        host = input("Enter the target: ")
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((host, port))
            if result == 0:
                print("Port {} is open.".format(port))
            else:
                print("Port {} is closed.".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.timeout:
        print("Connection timed out.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()


if __name__ == "__main__":
    while True:
        print('\033[1;34m' + logo + '\033[0;0m')

        ent = input("Enter the option: ")

        if (ent == "01"):
            portscan_manual()
        elif (ent == "02"):
            portscan_default()
        elif (ent == "03"):
            portscan_full()
        elif (ent == "00"):
            print("Exiting...")
            break
        else:
            print("Invalid option.")
