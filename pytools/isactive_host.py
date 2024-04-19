import socket
import sys

def is_active(remote_host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  # Timeout in seconds
            s.connect((remote_host, port))
            return True
    except Exception as e:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python is_active.py <remote_host>")
        sys.exit(1)

    remote_host = sys.argv[1]
    port = 80  # Default port for testing, you can change it as needed
    if is_active(remote_host, port):
        print(f"{remote_host} is active and reachable.")
    else:
        print(f"{remote_host} is not active or unreachable.")
