# Multi-threaded TCP Port Scanner

A lightweight port scanner written in Python. Developed as a practical project to understand network sockets, multi-threading, and CLI tool development.

## 🚀 Features
- **Concurrent Scanning**: Uses Python's `threading` module to scan multiple ports simultaneously.
- **Robust Argument Parsing**: Powered by `argparse` for a better CLI experience.
- **Input Validation**: Strictly adheres to the TCP/IP port range (1-65535).
- **Error Handling**: Gracefully handles invalid inputs and connection timeouts.

## 🛠️ Requirements
- Python 3.x
- No external dependencies (uses standard library).

## 📖 Usage
Clone the repository:
```bash
git clone [https://git@github.com:yuniopq/threaded-network-scanner.git](https://git@github.com:yuniopq/threaded-network-scanner.git)
cd threaded-network-scanner

```

Run the scanner:

```bash
python threaded-network-scanner.py <target_ip> -p <port_range>

```

Example:

```bash
python threaded-network-scanner.py 127.0.0.1 -p 1-1024

```

## ⚖️ Disclaimer

This tool is for educational and ethical testing purposes only. Only use it against targets you own or have explicit permission to test.
