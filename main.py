import api
import os
import platform

def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu():
    limpar_tela()
    print("--- Plataforma Quiz ---")
    print("1. Fazer quiz múltipla escolha")
    print("2. Fazer quiz verdadeiro/falso")
    print("3. Solicitar revisão de pergunta")
    print("4. Sair")

def ler_opcao_numerica(min_opcao, max_opcao, prompt="Escolha uma opção: "):
    while True:
        entrada = input(prompt)
        try:
            valor = int(entrada)
            if min_opcao <= valor <= max_opcao:
                return valor
            else:
                print(f"Digite um número entre {min_opcao} e {max_opcao}.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

def fazer_quiz(tipo):
    limpar_tela()
    perguntas = api.listar_questoes(tipo)
    respostas_usuario = {}

    print(f"Quiz {tipo} iniciado!")

    for q in perguntas:
        print(f"\n{q.id}: {q.text}")
        for i, opt in enumerate(q.options, 1):
            print(f"  {i}. {opt}")

        escolha = ler_opcao_numerica(1, len(q.options), prompt="Escolha a opção (número): ")
        respostas_usuario[q.id] = q.options[escolha - 1]

    resultado = api.corrigir_quiz(tipo, respostas_usuario)

    limpar_tela()
    print(f"Quiz {tipo} finalizado!")
    print(f"\nSua pontuação: {resultado['score']} / {resultado['total']}")
    print("Feedback:")
    for f in resultado["feedback"]:
        status = "Correta" if f["is_correct"] else "Incorreta"
        print(f" - {f['question']}")
        print(f"   Sua resposta: {f['user_answer']} ({status})")
        if not f["is_correct"]:
            print(f"   Resposta correta: {f['correct_answer']}")

    input("\nPressione ENTER para voltar ao menu...")

def solicitar_revisao():
    limpar_tela()
    print("--- Solicitar Revisão ---")
    question_id = input("Digite o ID da pergunta que quer revisar: ")
    motivo = input("Descreva o motivo da revisão: ")
    msg = api.solicitar_revisao(question_id, motivo)
    print("\n" + msg)
    input("\nPressione ENTER para voltar ao menu...")

def main():
    while True:
        mostrar_menu()
        opcao = ler_opcao_numerica(1, 4)
        if opcao == 1:
            fazer_quiz("multiple")
        elif opcao == 2:
            fazer_quiz("truefalse")
        elif opcao == 3:
            solicitar_revisao()
        elif opcao == 4:
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
