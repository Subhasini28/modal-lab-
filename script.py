import os
import socket
import getpass

print("User:", getpass.getuser())
print("Hostname:", socket.gethostname())
print("Current Directory:", os.getcwd())
