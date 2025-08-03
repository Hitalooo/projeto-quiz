import requests
import json
import os

BASE_URL = "http://127.0.0.1:8000"

respostas_armazenadas = {
    "multiple": {}, 
    "truefalse": {}
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def tratar_resposta(resposta):
    limpar_tela()
    if resposta.status_code in [200, 201]:
        print("Sucesso:")
        print(json.dumps(resposta.json(), indent=2, ensure_ascii=False))
    else:
        print(f"Erro {resposta.status_code}:")
        print(resposta.text)

def listar_questoes_com_respostas(tipo):
    limpar_tela()
    try:
        resposta = requests.get(f"{BASE_URL}/quizzes/{tipo}/perguntas")
        if resposta.status_code != 200:
            print("Erro ao buscar perguntas.")
            return
        perguntas = resposta.json()

        respostas_anteriores = respostas_armazenadas.get(tipo, {})

        print(f"--- Perguntas e respostas anteriores do quiz {tipo} ---")
        for p in perguntas:
            print(f"\n{p['id']}: {p['text']}")
            for i, opt in enumerate(p["options"], 1):
                print(f"  {i}. {opt}")

            resp = respostas_anteriores.get(p['id'])
            if resp:
                status = "Correta" if resp["correta"] else "Incorreta"
                print(f"Resposta anterior: {resp['resposta']} ({status})")
            else:
                print("Resposta anterior: (não respondida)")
    except Exception as e:
        print("Erro ao listar questões com respostas:", e)
    input("Pressione Enter para continuar...")

def realizar_quiz(tipo):
    limpar_tela()
    try:
        resposta = requests.get(f"{BASE_URL}/quizzes/{tipo}/perguntas")
        if resposta.status_code != 200:
            print("Erro ao buscar perguntas.")
            return
        perguntas = resposta.json()
        respostas_usuario = {}

        print(f"--- Quiz {tipo} ---")
        for p in perguntas:
            print(f"\n{p['id']}: {p['text']}")
            for i, opt in enumerate(p["options"], 1):
                print(f"  {i}. {opt}")
            while True:
                escolha = input("Escolha a opção (número): ")
                if escolha.isdigit() and 1 <= int(escolha) <= len(p["options"]):
                    respostas_usuario[p["id"]] = p["options"][int(escolha)-1]
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        dados = {"answers": respostas_usuario}
        resposta_corrigir = requests.post(f"{BASE_URL}/quizzes/{tipo}/corrigir", json=dados)
        if resposta_corrigir.status_code == 200:
            resultado = resposta_corrigir.json()
            print("\n--- Resultado ---")
            print(f"Pontuação: {resultado['score']} / {resultado['total']}")

            nova_armazenagem = {}

            for f in resultado["feedback"]:
                status = "Correta" if f["is_correct"] else "Incorreta"
                print(f"\nPergunta: {f['question']}")
                print(f"Sua resposta: {f['user_answer']} ({status})")
                if not f["is_correct"]:
                    print(f"Resposta correta: {f['correct_answer']}")

            for p in perguntas:
                resp = respostas_usuario.get(p["id"])
                f = next((item for item in resultado["feedback"] if item["question"] == p["text"]), None)
                if f:
                    nova_armazenagem[p["id"]] = {
                        "resposta": resp,
                        "correta": f["is_correct"]
                    }
            respostas_armazenadas[tipo] = nova_armazenagem

        else:
            print("Erro ao corrigir quiz:", resposta_corrigir.text)

    except Exception as e:
        print("Erro ao realizar quiz:", e)
    input("Pressione Enter para continuar...")

def solicitar_revisao():
    limpar_tela()
    try:
        id_pergunta = int(input("ID da pergunta para solicitar revisão: "))
        motivo = input("Motivo da revisão: ")
        dados = {"question_id": id_pergunta, "motivo": motivo}
        resposta = requests.post(f"{BASE_URL}/quizzes/revisoes", json=dados)
        
        limpar_tela()
        if resposta.status_code in [200, 201]:
            mensagem = resposta.json().get("message", "Solicitação realizada com sucesso!")
            print(mensagem)
        else:
            print(f"Erro {resposta.status_code}:")
            print(resposta.text)
        
    except Exception as e:
        print("Erro ao solicitar revisão:", e)
    input("Pressione Enter para continuar...")

def menu():
    while True:
        limpar_tela()
        print("\n--- Plataforma Quiz ---")
        print("1. Listar perguntas múltipla escolha (com respostas e status)")
        print("2. Fazer quiz múltipla escolha")
        print("3. Listar perguntas verdadeiro/falso (com respostas e status)")
        print("4. Fazer quiz verdadeiro/falso")
        print("5. Solicitar revisão de pergunta")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_questoes_com_respostas("multiple")
        elif opcao == "2":
            realizar_quiz("multiple")
        elif opcao == "3":
            listar_questoes_com_respostas("truefalse")
        elif opcao == "4":
            realizar_quiz("truefalse")
        elif opcao == "5":
            solicitar_revisao()
        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
