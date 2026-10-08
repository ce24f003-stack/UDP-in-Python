import socket

HOST = "0.0.0.0"
PORT = 9876
BUFFER_SIZE = 4096
OUTPUT_FILE = "received_file.dat"

print("Receiver is running. Waiting for incoming file...")

server_socket = None
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    with open(OUTPUT_FILE, "wb") as file:
        while True:
            data, _ = server_socket.recvfrom(BUFFER_SIZE)

            if data == b"EOF":
                print("EOF marker received. File transfer complete.")
                break

            file.write(data)

    print("File received successfully!")
    print("Saved as:", OUTPUT_FILE)
except Exception as error:
    print("Error during file reception:", error)
finally:
    if server_socket is not None:
        server_socket.close()
