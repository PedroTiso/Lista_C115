import socket

def main():
    host = '127.0.0.1'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Recebe e responde duas questões
    for _ in range(2):
        data = s.recv(1024).decode()
        print(data)
        resposta = input().strip()
        s.send(resposta.encode())

    # Recebe o resultado
    resultado = s.recv(1024).decode()
    print("\nResultado:")
    print(resultado)

    s.close()

if _name_ == "_main_":
    main()