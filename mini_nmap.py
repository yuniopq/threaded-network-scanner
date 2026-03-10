import socket
import threading
from datetime import datetime
import argparse

def scan_port(target, port):
    try:
        # Create the socket object (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        
        # result 0 means the port is open
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] Port {port:5}: OPEN")
        
        s.close()
    except Exception:
        # Silently ignore errors (closed ports, timeouts, etc.)
        pass

def main():
    # Setup Argument Parser for CLI usage
    parser = argparse.ArgumentParser(description="Multi-threaded TCP Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname to scan")
    parser.add_argument("-p", "--ports", help="Port range to scan (e.g. 1-1000)", default="1-1024")
    args = parser.parse_args()

    # Parse port range or single port
    try:
        if "-" in args.ports:
            start_port, end_port = map(int, args.ports.split("-"))
        else:
            start_port = end_port = int(args.ports)
            
        # Validate port boundaries (16-bit constraint)
        if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
            print("[-] Error: Port range must be between 1 and 65535.")
            return
            
    except ValueError:
        print("[-] Error: Invalid port format. Use '80' or '1-1024'.")
        return

    print("-" * 50)
    print(f"Scanning target: {args.target}")
    print(f"Time started:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    # List to keep track of threads
    threads = []
    
    # Spawn a thread for each port in the range
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(args.target, port))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("-" * 50)
    print("Scan completed.")

if __name__ == "__main__":
    main()