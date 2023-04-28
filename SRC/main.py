from ip_range_scanner import scan_ip_range
from ping_sweeper import ping_sweep
from port_scanner import port_scan
from service_detector import detect_service
from result_exporter import result_export

if __name__ == "__main__":
    scan_ip_range()
    ping_sweep()
    port_scan()
    detect_service()
    result_export()