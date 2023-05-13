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


def detect_service(open_ports):
    services = []

    for port in open_ports:
        service = COMMON_SERVICES.get(port)
        if service:
            services.append((port, service))
    return services
