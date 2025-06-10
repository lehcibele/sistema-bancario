menu = """
---- Escolha uma opção ---- 
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

"""

saldo = 0 
lista_valores_deposito = []
lista_valores_saque = []
saque_limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == 'd':
        valor_deposito = input("Qual o valor do depósito? ")

        try: 
            # converter o valor para o tipo float
            valor_deposito = float(valor_deposito)

            # verifica se o valor inserido é válido, se não solicita novamente o valor
            while valor_deposito <= 0:
                print("valor negativo, depósito não efetuado!\n")
                valor_deposito = input("Qual o valor do depósito? ")
                valor_deposito = float(valor_deposito)

            # salva os valores do deposito em uma lista
            lista_valores_deposito.append(valor_deposito)
            # faz o deposito
            saldo += valor_deposito
            print("Depósito efetuado com sucesso!")
        except:
            print(" ")
            print("Valor informado não é um número.")
            print("Realize novamente a operação desejada!")

    elif opcao.lower() == 's':
        valor_saque = input("Qual o valor do saque? ")

        try: 
            valor_saque = float(valor_saque)
            
            # verifica se o valor inserido é um numero, caso não, solicita novamente o valor
            while valor_saque <= 0:
                print("valor negativo, saque não efetuado!\n")
                valor_saque = input("Qual o valor do saque? ")
                valor_saque = float(valor_saque)

            # verifica se o valor de saque é menor ou igual saldo
            if valor_saque <= saldo:
                saldo -= valor_saque    
                # salva os valores do saque na lista
                lista_valores_saque.append(valor_saque)
                print("Saque efetuado com sucesso!")
            else:
                print(f'Valor de saque {valor_saque:.2f} é maior que o saldo {saldo:.2f}')
                print("Realize novamente a operação desejada!")
            
        except:
            print(" ")
            print("Valor informado não é um número.")
            print("Realize novamente a operação desejada!")

    elif opcao.lower() == 'e':
        print("------Extrato------")

        print("Depósitos feitos: ")

        for index, valor in enumerate(lista_valores_deposito):
            print(f'{index + 1}º {valor:.2f}')

        print('')
        print("Saques feitos:")

        for index, valor in enumerate(lista_valores_saque):
            print(f'{index + 1}º {valor:.2f}')

        print('')
        print(f'SALDO = R$ {saldo:.2f}')
        

    elif opcao.lower() == 'q':
        print("Operação finalizada!")
        break
    else: 
        print("Operação inválida, por favor selecione a operação desejada.")