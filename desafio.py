#menu recriado do repositório trilha-python-dio

import os


menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """



saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
mensagem = ''


def limpa_tela():
    os.system('clear')

def pergunta(mensagem):
    resposta = ''
    while resposta is not float:
        try:
            resposta = float(input(mensagem))
            if resposta <= 0:
                resposta = ''
                limpa_tela()
                print('Valor deve ser positivo. Tente novamente\n')
            else:
                break
        except:
            limpa_tela()
            print("Valor Inválido. Tente Novamente.\n")
    return resposta


while True:
    opcao = input(menu)
    if opcao == 'd':
        limpa_tela()
        mensagem = "Qual valor a ser depositado?"
        valor = pergunta(mensagem)
        saldo += valor
        extrato += f'Depósito no valor de R$ {valor:.2f}\n'
                                                          
    elif opcao == 's':
        limpa_tela()
        if numero_saques < LIMITE_SAQUES:

            mensagem = 'Qual valor a ser sacado?'
            valor = pergunta(mensagem)
            if valor < 500:
                if saldo >= valor:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f'Saque no valor de R$ {valor:.2f}\n'
                else:
                    limpa_tela()
                    print('Saldo insuficiente! Não foi possível realizar a operação. \n')
            else:
                limpa_tela()
                print("Valor excede limite por saque de R$ 500.00")

        else:
            limpa_tela()
            print('Limite diário de saques atingido. Tente novamente amanhã\n')

        
    elif opcao == 'e':
        limpa_tela()
        print('EXTRATO \n')
        print("Não foram realizadas movimentações\n" if not extrato else extrato)
        print(f'Saldo Atual: R$ {saldo:.2f}')
    elif opcao == 'q':
        limpa_tela()
        break
    else:
        limpa_tela()
        print('Alternativa inválida! Tente novamente.')
