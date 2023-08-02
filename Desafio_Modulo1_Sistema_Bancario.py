# Sistema bancário

# Operações: Depósito, saque e extrato

# A versão 1 só se preocupará com um usuário.

# Depósito

# Valor inteiro e positivo
# Os depósitos precisam ser armazenados em uma variável para serem exibidos na operação de extrato.


# Saques

# Limite de 3 saques diários
# Limite de R$ 500,00 por saque
# Precisa de saldo para fazer o saque
# Os saques precisam ser armazenados em uma variável para serem exibidos na operação de extrato.

# Extrato

# Listar todos os depósitos e saques
# No final, mostrar o saldo atual no formato R$xxx.xx

menu = """
Digite a opção desejada
-----------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
-----------------
"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saque = 0
limite_operacoes_saque = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        print("Operação de depósito")
        valor_deposito = int(input("Digite o valor do depósito:"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\n Depósito de {valor_deposito}. Saldo = {saldo}"
        else:
            print("O valor informado é inválido. Operação não realizada.")

    elif opcao == "s":
        print("Operação de saque")
        valor_saque = float(input("Digite o valor de saque:"))

        if numero_saque >= limite_operacoes_saque:
            print("Limite atingido de saques no dia. Operação não realizada.")

        elif valor_saque >= limite_saque:
            print("Valor de saque excede o limite. Operação não realizada.")

        elif valor_saque > saldo:
            print("Saldo insuficiente. Operação não realizada.")

        else:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"\n Saque de {valor_saque}. Saldo = {saldo}"

    elif opcao == "e":
        print("Extrato bancário:")
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Opção inválida, digite novamente a chave da operação desejada")
