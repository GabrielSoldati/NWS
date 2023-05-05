import ipaddress
import subprocess
import re

# Help functions

# Checks if range matches format
def valid_range(range_string):
    ip_format = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})-(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$'
    match = re.match()

    if match:
        start_ip, end_ip = match.groups()
        try:
            start_ip = ipaddress.IPv4Address(start_ip)
            end_ip = ipaddress.IPv4Address(end_ip)
            return start_ip <= end_ip
        except ipaddress.AdressValueError:
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
def online_check():
    try: 
        subprocess.check_output(["ping", "-c", "1", ip_address], timeout=2)
        return True
    except subprocess.CalledProcessError:
        return False

# Main function
def scan_ip_range():
    ip_range = get_range()
    start_ip, end_ip = ip_range.split("-")
    ip_list = []
    live_host = []

    for.... 

    

    





