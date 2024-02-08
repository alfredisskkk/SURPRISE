import socket

def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to a remote server (doesn't matter which one)
        s.connect(("8.8.8.8", 80))
        # Get the local IP address
        ip_address = s.getsockname()[0]
        # Close the socket
        s.close()
        return ip_address
    except Exception as e:
        print("Error:", e)
        return None

ip_address = get_ip_address()
if ip_address:
    print("""
 _____ _    _ _____  _____  _____  _____  _____ ______ _ 
/ ____| |  | |  __ \|  __ \|  __ \|_   _|/ ____|  ____| |
| (___ | |  | | |__) | |__) | |__) | | | | (___ | |__  | |
 \___ \| |  | |  _  /|  ___/|  _  /  | |  \___ \|  __| | |
 ____) | |__| | | \ \| |    | | \ \ _| |_ ____) | |____|_|
|_____/ \____/|_|  \_\_|    |_|  \_\_____|_____/|______(_)
                                                        """)
    print("Your IP address is:", ip_address)
    print("You're mine lil bro")
else:
    print("Failed to retrieve IP address.")
