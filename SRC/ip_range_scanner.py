import ipaddress
import subprocess
import re

# Help functions

# Checks if range matches format
def valid_range(range_string):
    ip_format = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})-(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$'
    match = re.match(ip_format, range_string)

    if match:
        start_ip, end_ip = match.groups()
        try:
            start_ip = ipaddress.IPv4Address(start_ip)
            end_ip = ipaddress.IPv4Address(end_ip)
            return start_ip <= end_ip
        except ipaddress.AddressValueError:
            return False
    else:
        return False

# Asks user for input until correct format is met   
def get_range():
        while True:
            ip_range = input("Enter Ip range (format example : 192.168.1.1-192.168.1.254)")
            if valid_range(ip_range):
                return ip_range
                
            else:
                print ("Invalid range. Enter a valid range.") 

# Checks if the device in question is online
def online_check(ip_address):
    try: 
        subprocess.check_output(["ping", "-c", "1", ip_address], timeout=5)
        return True
    except subprocess.CalledProcessError:
        return False
    except subprocess.TimeoutExpired:
        return False

# Main function
def scan_ip_range():
    ip_range = get_range()
    start_ip, end_ip = ip_range.split("-")
    start_ip_int = int(ipaddress.IPv4Address(start_ip))
    end_ip_int = int(ipaddress.IPv4Address(end_ip))
    ip_list = []
    live_host = []

    for ip_int in range(start_ip_int, end_ip_int + 1):
        ip = ipaddress.IPv4Address(ip_int)
        ip_str = str(ip)
        ip_list.append(ip_str)

        if online_check(ip_str):
            live_host.append(ip_str)

    return ip_list, live_host


## test
if __name__ == "__main__":
    ip_list, live_hosts = scan_ip_range()
    print("\nAll IP addresses in the range:")
    print("\n".join(ip_list))
    print("\nLive hosts in the range:")
    print("\n".join(live_hosts))

    

    





