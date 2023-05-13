from ip_range_scanner import scan_ip_range
from port_scanner import port_scan
from service_detector import detect_service
import tkinter as tk
from tkinter import messagebox

def network_scan():
    # Get IP range (textbox)
    ip_range = ip_range_text.get()
    
    # Scan the range (only interested in live hosts)
    _, live_hosts = scan_ip_range(ip_range)

    # Get port range
    start_port, end_port = map(int, port_range_text.get().split("-"))

    # Scan the range & detect services
    for ip in live_hosts:
        open_ports = port_scan(ip, start_port, end_port)
        services = detect_service(open_ports)
        
        results_listbox.insert(tk.END, f"{ip}: Open ports: {open_ports}, Services: {services}")





window = tk.Tk()
window.geometry('500x500')

# Frames
ip_frame = tk.Frame(window, padx=10, pady=10)
ip_frame.pack()
port_frame = tk.Frame(window, padx=10, pady=10)
port_frame.pack()
result_frame = tk.Frame(window, padx=10, pady=10)
result_frame.pack()

# Text boxes for ranges (port and ip)
tk.Label(ip_frame, text="Enter IP range. Example Format: 192.168.1.1-192.168.1.100 ").pack(side=tk.TOP)
ip_range_text = tk.Entry(ip_frame)
ip_range_text.pack(side=tk.TOP)

tk.Label(port_frame, text="Enter port range. Example Format: 1-1024").pack(side=tk.TOP)
port_range_text = tk.Entry(port_frame)
port_range_text.pack(side=tk.TOP)

# Scan button

scan_button = tk.Button(window, text="Scan Network", command=network_scan)
scan_button.pack(pady=10)

# Results listbox
results_scrollbar = tk.Scrollbar(result_frame)
results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
results_listbox = tk.Listbox(result_frame, yscrollcommand=results_scrollbar.set)
results_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
results_scrollbar.config(command=results_listbox.yview)

# Main loop

window.mainloop()
