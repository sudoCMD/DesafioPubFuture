from datetime import datetime
import json

try:
    with open('carteira.json', 'r') as c:
        carteira = json.loads(c.read())
    id_movitencao = carteira["idmovimentacao"]
    carteira.pop("idmovimentacao")
    
except:
    carteira = {}
    id_transacao = 1

def listarTransacoes():
    if len(carteira) == 0:
        print('\nSem transações!')
        return
    print('\nSuas transações: ')

    for transacao in sorted(
        carteira.values(), 
        key=lambda transacao: str(transacao["identificador"]),
        reverse=True):
            print(f'{transacao["identificador"]} - {transacao["data"]} - {transacao["descricao"]}: R${transacao["valor"]:.2f}')

#funçao que irá adcionar uma depspesas e receitas
def adicionarTransacao():
    global id_transacao, saldo

    #input que recebe um valor de descrição que pode ser uma despesa ou uma receita 
    descricao = input('\nDigite a descrição da transação: ')



    #aqui a diferenciação de uma receita será feita atraves do prefixo (-) adcionado pelo usuario. sendo um valor positivo correspondente a uma receita e o valor negativo a uma despesa
    valor = float(input('Digite o valor da transação (com sinal negativo se for despesa): '))
    data = str(datetime.now())

    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "identificador": str(id_transacao),
    }

    carteira["id_" + str(id_transacao)] = transacao
    id_transacao += 1
    print('Transação adicionada com sucesso!')

#função dedicada a delatar alguma transação seja ela uma depesa ou receita
def deletarTransacao():
    identificador = "id_" + input('\nDigite o id da transação que quer deletar: ')
    transacao = carteira.pop(identificador)
    print(f'Transação {transacao["identificador"]} - "{transacao["descricao"]}", no valor de R${transacao["valor"]:.2f} foi excluída!')

#função dedicada a editar transacao
def editarmovimentacao():
    id_transacao = int(input('\nDigite o id da transação que quer editar: '))
    identificador = "id_" + str(id_transacao)

    descricao = input('Digite a nova descrição da transação: ')
    valor = float(input('Digite o novo valor da transação: '))
    mudar_data = input('Digite S para mudar a data da transação para a data atual ou N para manter a data antiga: ').upper()
    if mudar_data == 'S':
        data = str(datetime.now())
    else:
        data = carteira[identificador]["data"]

    transacao = {
        "valor": valor,
        "descricao": descricao,
        "data": data,
        "identificador": id_transacao,
    }

    carteira["id_" + str(id_transacao)] = transacao

    print(f'Movimentação {id_transacao} editada com sucesso!')


def consultarSaldo():
    saldo = 0
    for transacao in carteira.values():
        saldo += transacao["valor"]
    
    print(f'Seu saldo atual é R${saldo:.2f}')

#função dedicada a quebra de linha
def quebralinha():
    print("""
    """)

#função dedicada a adcionar uma linha personalizada a "interface grafica"
def linha():
    print('-'*15)




#aqui será o menu de seleção: *simulação de interface grafica*

while True:
    linha()
    escolha = input("""\nDigite:
        \r1: Listar Movimentações
        \r2: Adicionar movimetaçao
        \r3: Deletar movimentaão
        \r4: Editar Movimentação
        \r5: Consultar saldo atual
        \r6: Sair do programa
        \n\rSua escolha: """)
    linha()


#condições de escolha do usuário postas no input de escolha
    if escolha == '2':
        adicionarTransacao()
        

    elif escolha == '3':
        deletarTransacao()
       

    elif escolha == '4':
        editarmovimentacao()
       

    elif escolha == '1':
        listarTransacoes()
    elif escolha == '5':
        consultarSaldo()
    elif escolha == '6':
        


        exit()
   
   
    else:
        print('Número inválido\n')






