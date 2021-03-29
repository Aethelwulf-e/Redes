from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 2211))
serverSocket.listen(1)

while True:
    print('Ready to server...')
    # Configura uma nova conexão do cliente
    connectionSocket, addr = serverSocket.accept()
    try:
        # Recebendo a mensagem requisitada pelo cliente
        msg = connectionSocket.recv(1024)
        
        # Se o tamanho de msg for 0, volto para o começo do laço,
        # sem isso o código gera erros de "index out of range"
        if not msg:
            continue

        # Extraindo o caminho do objeto solicitado da mensagem
        # O camindo é a segunda parte do cabeçalho HTTP, por isso o [1]
        filename = msg.split()[1]

        # Como o caminho extraído da solicitação HTTP inclui um caractere
        # "/", lemos o caminho do segundo caractere
        f = open(filename[1:])

        # Guardando todo o conteúdo o arquivo requisitado em um buffer temporário
        outputdata = f.read()

        # Enviando a linha do cabeçalho HTTP para o soquete de conexão
        connectionSocket.send('HTTP/1.1 200 OK\n\n'.encode())

        # Enviando o conteúdo do arquivo requisitado para o soquete
        for i in range (0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            #connectionSocket.send("\n\n".encode())

        # Fechando o soquete com o cliente
        connectionSocket.close()

    except IOError:
        #print('404 Not Found')

        # Enviando o cabeçalho HTTP para um arquivo não encontrado
        # e enviando a frase 404 NOT FOUND
        connectionSocket.send('HTTP/1.1 404 NOT FOUND\n\n <html><h1>404 Not Found</h1></html>'.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
