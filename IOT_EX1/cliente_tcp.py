import socket

SERVER = '127.0.0.1'
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect((SERVER, PORT))

print('Cliente TCP conectado.')
print('Digite uma mensagem. Para sair, use CTRL+X.')

msg = input()

while msg != '\x18':
    tcp.send(msg.encode())
    msg = input()

tcp.close()
