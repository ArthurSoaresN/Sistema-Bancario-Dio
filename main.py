#   Santander 2025 - Back-End com Python
#   Desafio Criando um Sistema Bancário em Python
#   Nivel Básico


#   Sistema Bancário
# Operações: Sacar, Depositar e Visualizar Extrato

#Saque 
# O sistema deve permitir realiar 3 saques diários
# Limite de R$500,00 por saque
# Ter robustez
# Armazenar todos os saques para operação Extrato

#Depósito
# Depositar valores positivos
# Armazenar todos os saques para operação de Extrato

#Extrato
# Listar todos os depósitos e saques realizados na conta.
# No fim da listagem deve ser exibido o saldo atual da conta.
# Formato dos valores: R$ 100.00

import os

LIMITE_DIARIO = 3
SAQUE_LIMITE = 500

def set_menu(saques):
    menu = f"""    ===  Sistema Bancário DIO  ===
    Bem-vindo! Selecione uma opção:

    (Limite de saques diário: {LIMITE_DIARIO})
    Saques feitos hoje: {saques}

    1. Depositar
    2. Sacar
    3. Visualizar Extrato
    
    4. Sair"""
    print(menu)

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def depositar(valor_depositado: float, conta: float, extrato: list) -> float:
    if valor_depositado <= 0:
        print("Não é permitido depositar saldo negativo")
        print(f"Saldo Atual: {conta:.2f}")
        return conta
    else:
        deposito = conta + valor_depositado
        print(f"Deposito de R${valor_depositado:.2f} realizado com sucesso")
        print(f"Saldo Atual: {deposito:.2f}")
        if extrato[0] == 'zero':
            extrato[0] = f"Deposito de R${valor_depositado:.2f} realizado"
        else:
            extrato.append(f"Deposito de R${valor_depositado:.2f} realizado")
        return deposito #Deposito Realizado

def sacar(valor_solicitado: float, conta: float, saques_realizados: int, extrato: list) -> tuple[float, int]:

    saque = conta - valor_solicitado

    if saques_realizados >= LIMITE_DIARIO:
        print("Você atingiu o número máximo de saques hoje")
    elif valor_solicitado <= 0:
        print("O valor do saque deve ser positivo")
        print(f"Saldo Atual: {conta:.2f}")
    elif valor_solicitado > SAQUE_LIMITE:
        print(f"Valor máximo para saque permitido é de R${SAQUE_LIMITE}")
    elif (conta < valor_solicitado):
        print("Saldo insuficiente para saque")
        print(f"Saldo Atual: {conta:.2f}")
    else:
        print(f"Saque de R${valor_solicitado:.2f} realizado com sucesso")
        print(f"Saldo Atual: {(saque):.2f}")
        saques_realizados = saques_realizados + 1

        if extrato[0] == 'zero':
            extrato[0] = f"Saque de R${valor_solicitado:.2f} realizado"
        else:
            extrato.append(f"Saque de R${valor_solicitado:.2f} realizado")
        return saque, saques_realizados #Saque Realizado

    return conta, saques_realizados

def exibir_extrato (conta: float, extrato: list):
    limpar_tela()
    print("=== EXTRATO ===")
    print()

    if extrato[0] == 'zero':
        print("Nenhuma operação realiada")
    else:
        for operacao in extrato:
            print(operacao)

    print()
    print(f"Saldo Atual: R${conta:.2f}")
    print()

def menu_opcao(): 
    print("\nOpções:")
    print(" 1. Voltar ao menu")
    print(" 2. Sair")
    
    while True: # Loop para garantir que a entrada seja válida
        try:
            escolha2 = int(input('    >>> '))
            if escolha2 == 1:
                limpar_tela()
                return 
            elif escolha2 == 2:
                limpar_tela()
                print("Obrigado por utilizar o Sistema Bancário DIO. Até mais!")
                exit()
            else:
                print("Opção inválida. Digite 1 para Voltar ou 2 para Sair.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# DESAFIO 2 -> Funções: Criar Usuário e Criar Conta Corrente

valor = 0.0 # Variavel que recebe o valor a ser retirado ou adicionado
conta = 0.0 # Variavel que controla o saldo do usuário
extrato = ['zero'] #Variavel para registrar as operações realizadas
saques_realizados = 0

limpar_tela()

while True:
    set_menu(saques_realizados)

    try:
        escolha = int(input('    >>> '))
    except ValueError:
        limpar_tela()
        print("Entrada inválida. Por favor, digite um número de 1 a 4.")
        menu_opcao() # Dá a opção de voltar ou sair após erro
        continue # Volta para o início do loop

    limpar_tela() # Limpa a tela após a escolha do menu

    if escolha == 1: # Depósito
        print("Digite o valor que deseja depositar:")
        try:
            valor_digitado = float(input('    >>> '))
            conta = depositar(valor_digitado, conta, extrato) # POSITIONAL ONLY
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
        menu_opcao()

    elif escolha == 2: # Saque
        print("Digite o valor que deseja sacar:")
        print(f"Saldo Atual: {conta}")
        try:
            valor_digitado = float(input('    >>> '))
            # A função sacar agora retorna uma tupla
            conta, saques_realizados = sacar(valor_digitado, conta, saques_realizados, extrato) # DESAFIO 2 -> KEYWORD ONLY
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
        menu_opcao()

    elif escolha == 3: # Extrato
        exibir_extrato(conta, extrato) # Passa o saldo e o extrato para a função / DESAFIO 2 -> HIBRIDO
        menu_opcao()

    elif escolha == 4: # Sair
        print("Obrigado por utilizar o Sistema Bancário DIO. Até mais!")
        exit()

    else: # Escolha inválida
        print("Opção inválida. Por favor, selecione uma opção de 1 a 4.")
        menu_opcao()