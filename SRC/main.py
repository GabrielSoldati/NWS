from ip_range_scanner import scan_ip_range
from ping_sweeper import ping_sweep
from port_scanner import port_scan
from service_detector import detect_service
from result_exporter import result_export
import tkinter as tk
from tkinter import messagebox

def network_scan():
    # Get IP range (textbox)
    ip_range = ip_range_text.get()
    
    # Scan the range
    ip_list, live_hosts = scan_ip_range(ip_range)

    # Get port range
    start_port, end_port = map(int, port_range_text.get().split("-"))

    # Scan the range & detect services
    for ip in live_hosts:
        






window = tk.Tk()

# Text boxes for ranges (port and ip)
ip_range_text = tk.Entry(window)
ip_range_text.pack()
port_range_text = tk.Entry(window)
port_range_text.pack()

# Scan button

scan_button = tk.Button(window, text="Scan Network", command=scan_network)
scan_button.pack()

# Main loop

window.mainloop()
