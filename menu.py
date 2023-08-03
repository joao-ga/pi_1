from Funcoes import Adicionar, Alterar, Classificar, Excluir

#Frase inicial do menu:
print('Bem vindo ao avaliador de ar Sapovalo.')

#Variavel de controle:
num = 1
#Loop no menu:
while num != 0:
    # Apresentando as opções ao usuario
    print('*******************************')
    print('Escolha uma das opções abaixo:')
    print('1- Inserir')
    print('2- Alterar')
    print('3- Excluir')
    print('4- Classificar')
    print('0- Sair do sistema')
    print('*******************************')

    # Variável de controle
    while True:
        try:
            num = int(input('Digite o número (de 1 a 4) referente ao item que deseja: '))
            break
        except ValueError:
            print('Voce digitou um valor invalido')

    # Validações para abrir cada tela
    if num == 1:
        # Chamando função Adicionar
        Adicionar()
    elif num == 2:
        # ocorre os processos para Alterar algum valor
        Alterar()
    elif num == 3:
        # ocorre os processos para excluir as amostras
        Excluir()
    elif num == 4:
        # ocorre os processos para Classificação do ar
        Classificar()
    elif num == 0:
        print('Saindo do sistema')
    else:
        print('Digite um valor dentro do intervalo!')
