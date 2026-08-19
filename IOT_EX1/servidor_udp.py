import socket

HOST = ''
PORT = 5002

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST, PORT))

print('Servidor UDP aguardando mensagens...')

while True:
    msg, cliente = udp.recvfrom(1024)

    print('Cliente:', cliente)
    print('Mensagem:', msg.decode())

