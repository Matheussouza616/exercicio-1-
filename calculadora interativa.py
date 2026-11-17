
# 1. FUNÇÕES MATEMÁTICAS

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b


# 2. MENU PRINCIPAL

while True:
    print("\n===== CALCULADORA =====")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Sair")

    opcao = input("Escolha uma opção: ")

    # 3. VERIFICAR SE O USUÁRIO DESEJA SAIR

    if opcao == "5":
        print("Calculadora encerrada. Até mais!")
        break

    # 4. VERIFICAR OPÇÃO VÁLIDA

    elif opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # 5. EXECUTAR OPERAÇÃO ESCOLHIDA

        if opcao == "1":
            resultado = somar(num1, num2)

        elif opcao == "2":
            resultado = subtrair(num1, num2)

        elif opcao == "3":
            resultado = multiplicar(num1, num2)

        elif opcao == "4":
            resultado = dividir(num1, num2)

            if resultado is None:
                print("Erro: Divisão por zero não é permitida")
                continue

        print("Resultado:", resultado)

    else:
        print("Opção inválida! Tente novamente.")
