import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = ('localhost', 12000)
s.settimeout(1)

try:
    for i in range(1, 11):
        comeco = time.time()
        msg = "PING #" + str(i) + " " + time.ctime(comeco)
        try:
            enviar = s.sendto(msg.encode(), servidor)
            print("Enviado: " + msg)
            data, server = s.recvfrom(1024)
            print(("Recebido: " + str(data)))
            fim = time.time()
            duracao = fim - comeco
            print("RTT: " + str(duracao) + " segundos\n")

        except socket.timeout:
            print("Recebido: " + "#" + str(i) + " Solicitacao expirada\n")
finally:
    s.close()

