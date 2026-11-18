
# 1. FUNÇÃO PARA LER E VALIDAR NÚMEROS

def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero

        except ValueError:
            print("Valor inválido! Digite apenas números.")


# 2. PROGRAMA PRINCIPAL

print("===== CALCULADORA SEGURA =====")

# Solicitar os números ao usuário
dividendo = ler_numero("Digite o dividendo: ")
divisor = ler_numero("Digite o divisor: ")


# 3. REALIZAR A DIVISÃO

try:
    resultado = dividendo / divisor

    print("Resultado da divisão:", resultado)

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")


