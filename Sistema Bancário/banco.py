def printExt():
    with open('extrato.txt', 'rt') as file:
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
    

def extrato(caixa, T, operacao_desc):
    with open ('extrato.txt', 'a') as file:
        if file.tell() == 0:  # Verifica se o arquivo está vazio
            file.write('- EXTRATO DIO BANK - \n')  # Adiciona a informação no topo
        if operacao_desc == 'Depósito':
            s = f'Valor depositado: R${caixa:.2f}\n'
        elif operacao_desc == 'Saque':
            s = f'Valor sacado: R${caixa:.2f}\n'
        else:
            s = 'Operação desconhecida\n'
        file.write(s)
        t = f'TOTAL: {T:.2f}\n'
        file.write(t)

    file.close()

def deposito():
    D = float(input('Digite o valor que deseja depositar: '))
    return D


def main():
    menu = '''\n   - DIO BANK -
    Olá usuário, que operação deseja realizar hoje?
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

    m = [0,1,2,3]

    while operacao != 0:
        if operacao not in m:
            operacao = int(input('N° inválido. Digite novamente: '))
        elif operacao == 0:
            break
        elif operacao == 1:
            D = deposito()
            caixa = D
            T += caixa 
            extrato(caixa, T, 'Depósito')  # Passa a descrição da operação 'Depósito'
            operacao = int(input(menu))
        elif operacao == 2:
            S = saque(T, NumS)
            T -= S
            extrato(S, T, 'Saque')  # Passa a descrição da operação 'Saque'
            NumS += 1
            operacao = int(input(menu))
        elif operacao == 3:
            printExt()
            operacao = int(input(menu))
    
    print('Volte sempre o DIO BANK')

  
if __name__ == '__main__':
    main()