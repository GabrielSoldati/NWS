import socket


#scan the given port range for given ip
def port_scan(ip_address, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        status = sock.connect_ex((ip_address, port))

        if status == 0:
            open_ports.append(port)

        sock.close() 
    
    return open_ports

