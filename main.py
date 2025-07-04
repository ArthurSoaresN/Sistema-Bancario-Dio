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

def set_menu(saques: int):
    limpar()
    menu = f"""    ===  Sistema Bancário DIO  ===
    Bem-vindo! Selecione uma opção:

    (Limite de saques diário: 3)
    Saques feitos hoje: {saques}

    1. Depositar
    2. Sacar
    3. Visualizar Extrato
    
    4. Sair"""
    print(menu)

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def depositar(valor: float) -> float:
    if valor < 0:
        print("Não é permitido depositar saldo negativo")
        print(f"Saldo Atual: {conta:.2f}")
        return conta
    else:
        print(f"Deposito de R${valor:.2f} realizado com sucesso")
        print(f"Saldo Atual: {(conta + valor):.2f}")
        extrato.append(f"Deposito de R${valor:.2f} realizado")
        return conta + valor

def sacar(valor: float) -> float:
    if saques >= LIMITE_DIARIO:
        ("Você atingiu o número máximo de saques hoje")
        return conta
    else:
        if (conta >= valor) and (valor <= SAQUE_LIMITE):
            print(f"Saque de R${valor:.2f} realizado com sucesso")
            print(f"Saldo Atual: {(conta - valor):.2f}")
            extrato.append(f"Saque de R${valor:.2f} realizado")
            saques = saques + 1
            return conta - valor
        elif valor > SAQUE_LIMITE:
            print()
        else:
            print("Saldo insuficiente para saque")
            print(f"Saldo Atual: {conta:.2f}")
            return conta
    


valor = 0 # Variavel que recebe o valor a ser retirado ou adicionado
conta = 0 # Variavel que controla o saldo do usuário
extrato = ['zero'] #Variavel para registrar as operações realizadas
escolha = int(input('    >>> '))
saques = 0
control = 1 #Variavel para controlar o while

while control == 1:
    set_menu(saques)

    if escolha == 1: #Deposito
        limpar()
        print("Digite o valor que deseja depositar")
        valor = float(input('   >>> '))
        conta = depositar(valor)

    elif escolha == 2: #Saque
        limpar()
        print("Digite o valor que deseja sacar")
        valor = float(input('   >>> '))
        conta = sacar(valor)

    



