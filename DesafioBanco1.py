menu = """

############### MENU ###############

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

####################################

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    #DEPÓSITO
    if opcao.upper() == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Seu novo saldo é: R${saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    #SAQUE
    elif opcao.upper() == "S":
        valor = float(input("Informe o valor do saque: "))

        if (valor > 0 and valor <= limite):
          
            if (numero_saques < LIMITE_SAQUES and saldo >= valor):
                numero_saques += 1
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                print(f"Seu novo saldo é: R${saldo:.2f}")
            else:
                if numero_saques >= LIMITE_SAQUES:
                    print("Operação falhou! Número limite de saques atingido.")
                else:
                    print("Operação falhou! Saldo insuficiente.")

        else:
            print(f"Operação falhou! O valor informado é inválido ou excede o limite de R${limite:.2f}.")

    #EXTRATO
    elif opcao.upper() == "E":
        print("############## EXTRATO ##############\n")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo atual = R${saldo:.2f}\n")
        print("#####################################")

    #SAIR
    elif opcao.upper() == "Q":
        print("Tenha um bom dia e até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")