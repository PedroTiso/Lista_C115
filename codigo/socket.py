import socket

# Questões: [pergunta, opções, resposta_correta]
questoes = [
    {
        "pergunta": "Qual é a capital da Itália?",
        "opcoes": ["a) Roma", "b) Paris", "c) Madrid", "d) Lisboa"],
        "resposta": "a"
    },
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["a) Rio de Janeiro", "b) Brasília", "c) São Paulo", "d) Salvador"],
        "resposta": "b"
    }
]

def main():
    host = '127.0.0.1'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("Servidor aguardando conexão...")

    conn, addr = s.accept()
    print(f"Conexão estabelecida com {addr}")

    acertos = 0
    resultados = []

    for i, questao in enumerate(questoes, start=1):
        # Envia pergunta e opções
        mensagem = f"\nQuestão {i}: {questao['pergunta']}\n"
        for opcao in questao['opcoes']:
            mensagem += opcao + "\n"
        mensagem += "Digite a letra da resposta: "
        conn.send(mensagem.encode())

        # Recebe resposta
        resposta = conn.recv(1024).decode().strip().lower()
        if resposta == questao['resposta']:
            acertos += 1
            resultados.append(f"Questão {i}: Acerto")
        else:
            resultados.append(f"Questão {i}: Erro (resposta correta: {questao['resposta']})")

    # Envia resultados
    resultado_msg = "\n".join(resultados) + f"\nTotal de acertos: {acertos}/{len(questoes)}"
    conn.send(resultado_msg.encode())
    conn.close()
    s.close()

if _name_ == "_main_":
    main()