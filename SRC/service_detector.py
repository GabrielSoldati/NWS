import socket
# dict for services
COMMON_SERVICES = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    993: 'IMAPS',
    995: 'POP3S'
}


def detect_service(ip_address, open_ports):
    services = []

    for port in open_ports:
        service = COMMON_SERVICES.get(port)
        if service:
            services.append((port, service))
    return services


#test
def test_detect_service():
    ip_address = '192.168.0.100'  
    open_ports = [443, 21, 22, 23, 80]  #asuming open.. just a test
    services = detect_service(ip_address, open_ports)

    for port, service in services:
        print(f"Port {port} is open and running {service} service.")

if __name__ == "__main__":
    test_detect_service()