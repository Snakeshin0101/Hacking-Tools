import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print('[+] Port Open ' + str(port))
        sock.close()

    except:
        pass

targets = input('[*] Enter targets to scan (split them by ,): ')
ports = int(input('[*] Enter how many ports you want to scan: '))

if ',' in targets:
    print('[*] Scanning Multiple Targets...')
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(''), ports)
else:
    scan(targets, ports)

scan(targets, ports)