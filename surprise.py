import socket

try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(r'''
   _____ _    _ _____  _____  _____  _____  _____ ______ 
  / ____| |  | |  __ \|  __ \|  __ \|_   _|/ ____|  ____|
 | (___ | |  | | |__) | |__) | |__) | | | | (___ | |__   
  \___ \| |  | |  _  /|  ___/|  _  /  | |  \___ \|  __|  
  ____) | |__| | | \ \| |    | | \ \ _| |_ ____) | |____ 
 |_____/ \____/|_|  \_\_|    |_|  \_\_____|_____/|______|
''')
    print("Here's your IP address:", ip_address)
except socket.error as e:
    print("Oops! An error occurred while retrieving the IP address:", e)