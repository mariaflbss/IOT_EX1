import socket
from threading import Thread


def atender_cliente(con, cliente):
    print('Thread iniciada para:', cliente)

    while True:
        msg = con.recv(1024)

        if not msg:
            break

        print('Cliente:', cliente)
        print('Mensagem:', msg.decode())

    print('Finalizando conexão:', cliente)

    con.close()


HOST = ''
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.bind((HOST, PORT))
tcp.listen(5)

print('Servidor TCP com Threads aguardando conexões...')

while True:
    con, cliente = tcp.accept()

    print('Conectado por:', cliente)

    thread = Thread(
        target=atender_cliente,
        args=(con, cliente)
    )

    thread.start()
