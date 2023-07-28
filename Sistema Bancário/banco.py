from random import randint
import os
from datetime import datetime


def printExt(numero_conta):
    with open(f'{numero_conta}.txt', 'rt') as file:
        linha = file.readline()
        while linha != '':
            print(linha)
            linha = file.readline()  # Mover o ponteiro de leitura para a próxima linha
    file.close()


def saque(T, NumS):
    if NumS >= 3:
        print('O n° de saques diários já atingiu o limite de 3')
        return 0

    S = float(input('Digite o valor que deseja sacar R$: '))

    while S > T or S > 500:
        if S > T:
            print(f'Valor de saque maior que em caixa. Total: {T}')
        elif S > 500:
            print('O valor limite para saque é de R$ 500.00')
        S = float(input('Digite o valor que deseja sacar R$: '))

    return S


def extrato(numero_conta, caixa, T, operacao_desc, cliente):
    nome_arquivo = f'{numero_conta}.txt'
    with open(nome_arquivo, 'a') as file:
        if file.tell() == 0:  # Verifica se o arquivo está vazio
            # Adiciona a informação no topo
            file.write(f'- EXTRATO DIO BANK - \nConta: {numero_conta} - \n')
            # Escreve as informações do cliente no topo
            file.write(formatar_cliente(cliente))

        if operacao_desc == 'Depósito':
            s = f'Valor depositado: R${caixa:.2f}\n'
        elif operacao_desc == 'Saque':
            s = f'Valor sacado: R${caixa:.2f}\n'
        else:
            s = 'Operação desconhecida\n'

        file.write(s)
        t = f'TOTAL: R${T:.2f}\n'
        file.write(t)
    file.close()


def deposito():
    D = input('Digite o valor que deseja depositar: ')
    return float(D)


def lerconta(numero_conta):
    # Name of the file based on the account number
    nome_arquivo = f'{numero_conta}.txt'
    cliente = {}
    with open(nome_arquivo, 'rt') as file:
        # Skip the first two lines (header information)
        file.readline()
        file.readline()

        cliente['Nome'] = file.readline().split(': ')[1].strip()

    return cliente


def criarconta():
    D = {}
    cliente = []
    nome = input('Nome completo: ')
    idade = input('Data de nascimento[DD/MM/AA]: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone (DD)NNNN-NNNN: ')
    conta = ""
    for _ in range(5):
        conta += str(randint(0, 9))
    print(
        f'Seja bem vindo ao DIO BANK {nome.split()[0]}, o N° da sua conta é: {conta}')
    cliente = [nome, conta, idade, endereco, telefone]
    D[conta] = cliente
    return D


def formatar_cliente(cliente):
    nome, numero_conta, idade, endereco, telefone = cliente
    return f'Nome: {nome}\nNúmero da conta: {numero_conta}\nIdade: {idade}\nEndereço: {endereco}\nTelefone: {telefone}\n\n'


def primeironome(numero_conta):
    with open(f'{numero_conta}.txt', 'rt') as file:
        nome = file.readline()
        if nome.startswith('Nome: '):
            return nome.split(': ')[1].strip().split()[0]
    return None


def main():
    conta = input('''   - DIO BANK -
    Olá, bem vindo ao DIO BANK
    Possui conta [S|N]: ''').upper()[0]

    D = {}  # Defina D como um dicionário vazio no início da função
    numero_conta = ""  # Defina numero_conta como uma string vazia

    if conta == 'N':
        print('Você será direcionado ao sistema de criação de conta')
        D = criarconta()
        numero_conta = list(D.keys())[0]
    elif conta == 'S':
        numero_conta = input('Digite o N°  da conta: ')
        # Read the account information from the TXT file
        cliente = lerconta(numero_conta)
        if cliente:
            D[numero_conta] = cliente
            primeiro_nome = cliente["Nome"].split()[0]
            print(f'Bem-vindo(a) ao DIO BANK, {primeiro_nome}!')
        else:
            if numero_conta not in D:
                print('Conta não encontrada.')
            return

    menu = '''
        [1] Depósito
        [2] Saque
        [3] Extrato
        [0] Sair
        Digite o número desejado: '''

    operacao = int(input(menu))
    caixa = 0
    T = 0
    S = 0
    NumS = 0

    m = [0, 1, 2, 3]

    while operacao != 0:
        if operacao not in m:
            operacao = int(input('N° inválido. Digite novamente: '))
        elif operacao == 0:
            break
        elif operacao == 1:
            deposit_amount = deposito()  # Store the deposit amount in a separate variable
            caixa = deposit_amount
            T += caixa
            # Pass the 'cliente' information
            extrato(numero_conta, caixa, T, 'Depósito', D[numero_conta])
            operacao = int(input(menu))
        elif operacao == 2:
            S = saque(T, NumS)
            T -= S
            # Pass the 'cliente' information
            extrato(numero_conta, S, T, 'Saque', D[numero_conta])
            NumS += 1
            operacao = int(input(menu))
        elif operacao == 3:
            printExt(numero_conta)
            operacao = int(input(menu))

    print('Volte sempre ao DIO BANK')


if __name__ == '__main__':
    main()
