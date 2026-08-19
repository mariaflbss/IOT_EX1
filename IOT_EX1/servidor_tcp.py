import socket

HOST = ''
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.bind((HOST, PORT))
tcp.listen(1)

print('Servidor TCP aguardando conexão...')

while True:
    con, cliente = tcp.accept()

    print('Conectado por:', cliente)

    while True:
        msg = con.recv(1024)

        if not msg:
            break

        print('Mensagem:', msg.decode())

    print('Finalizando conexão do cliente:', cliente)

    con.close()
