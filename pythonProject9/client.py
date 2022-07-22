import socket
import threading
import sys


# Wait для входящих данных с сервера
# .decode используется для преобразования сообщения в байтах в строку
##########################################################
# Wait for incoming data from server
# .decode is used to turn the message in bytes to a string
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break

# Get хост и порт
# Get host and port
host = input("Host: ")
port = int(input("Port: "))

# Attempt подключение к серверу
# Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

# Create новый поток для ожидания данны
# Create new thread to wait for data
receiveThread = threading.Thread(target=receive, args=(sock, True))
receiveThread.start()

# Send данных на сервер
# str.encode используется для преобразования строкового сообщения в байты, чтобы его можно было отправить по сети.
# Send data to server
# str.encode is used to turn the string message into bytes so it can be sent across the network
while True:
    message = input()
    sock.sendall(str.encode(message))
