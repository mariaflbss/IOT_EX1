import socket

SERVER = '127.0.0.1'
PORT = 5002

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

destino = (SERVER, PORT)

print('Cliente UDP iniciado.')
print('Digite uma mensagem. Para sair, use CTRL+X.')

msg = input()

while msg != '\x18':
    udp.sendto(msg.encode(), destino)
    msg = input()

udp.close()
