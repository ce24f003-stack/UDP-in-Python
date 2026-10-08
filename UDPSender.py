import os
import socket
import time

RECEIVER_IP = "127.0.0.1"
RECEIVER_PORT = 9876
BUFFER_SIZE = 4096
FILE_PATH = "test.txt"

if not os.path.exists(FILE_PATH):
    print("Error: Source file does not exist.")
    print("Looking for:", os.path.abspath(FILE_PATH))
    raise SystemExit(1)

print("Starting file transfer...")
print("File:", os.path.abspath(FILE_PATH))

client_socket = None
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with open(FILE_PATH, "rb") as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break

            client_socket.sendto(data, (RECEIVER_IP, RECEIVER_PORT))
            time.sleep(0.001)

    client_socket.sendto(b"EOF", (RECEIVER_IP, RECEIVER_PORT))
    print("File sent successfully!")
except Exception as error:
    print("Error during file transmission:", error)
finally:
    if client_socket is not None:
        client_socket.close()
