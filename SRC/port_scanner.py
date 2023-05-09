import socket

# Get range from user
def get_port_range():
    port_range_str = input("Enter port range. Format example: 1-1024")
    start_port, end_port = map(int, port_range_str.split("-"))
    return start_port, end_port

#scan the given port range for given ip
def port_scan(ip_address, port_range):
    open_ports = []
    start_port, end_port = port_range

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        status = sock.connect_ex((ip_address, port))

        if status == 0:
            open_ports.append(port)

        sock.close() 
    
    return open_ports


# testing
ip_address = "192.168.0.100"  # Example IP address
port_range = get_port_range()  # Get the port range from the user.

open_ports = port_scan(ip_address, port_range)
print("Open ports:", open_ports)