#importando bibliotecas para o banco de dados
import oracledb

#criando a conexão com o DB
connection = oracledb.connect(
    user="SAPOVALO_DB",
    password='123',
    dsn="localhost/xe"
)

print('Sucesso na conexão com o DB\n\n')

#definindo variável para a conexão
cursor = connection.cursor()

#Criando função para ser chamada em outro arquivo
def Adicionar():
    #Criando lista vazia para posteriormente inserir amostras
    amostras = []

    #Criando lista com os nomes dos parâmetros:
    nomes_parametros = ['Particulas inaláveis', 'Particulas inaláveis finas', 'Ozônio', 'Monóxido de carbono', 'Dióxido de nitrogênio', 'Dióxido de enxofre']

    #Criando loop para pedir os valores baseados no index do nomes_parametros
    for index in range (0,6):
        #validando input
        while True:
          try:
               valor = float(input(f'Digite um valor positivo para {nomes_parametros[index]}: '))
               break
          except ValueError:
               print('Voce digitou um valor invalido')
        if valor < 0:
            print('Digite um valor positivo!')
            valor = float(input(f'Digite um valor positivo para {nomes_parametros[index]}: '))
        amostras.append(valor)

    #Adicionando as amostras no banco de dados:
    cursor.execute("insert into parametros (mp10,mp2,o3,co,no2,so2) values(:1,:2,:3,:4,:5,:6)", amostras)
    connection.commit()
    print('Valores inseridos com sucesso\n\n')


#Criando variáveis para funcao alterar()
nomeElement = ''
newValue = 0
#Criando função para alterar valores:
def Alterar():
        connection.commit()
        #Print amostras do BD
        cursor.execute("SELECT * from parametros")
        result_0 = cursor.fetchall()
        for i in range(len(result_0)):
             res = result_0[i]
             print(f'Amostra ID {res[6]}: (mp10: {res[0]} mp2: {res[1]} o3: {res[2]} co: {res[3]} no2: {res[4]} so2: {res[5]})')
     #validando input
        while True:
             try:
                  ID_Element = int(input('Digite o ID das amostras: '))
                  ID = [ID_Element]
                  cursor.execute('SELECT mp10, mp2, o3, co, no2, so2 FROM parametros WHERE ID = :1', ID)
                  result = list(cursor.fetchone())
                  break
             except ValueError:
                  print('Voce digitou um valor invalido!')
             except TypeError:
                  print('O ID digitado nao existe!')

        print(f'Amostra selecionada: {result}')
        #validando input
        while True:
             try:    
               nomeElement = int(input('Digite o numero correspondente do parametro que deseja alterar\n (1- mp10, 2- mp2, 3- o3, 4- co, 5- no2, 6- so2): '))
               break
             except ValueError:
                  print('Digite um valor valido!')
        while True:
             try:
               newValue = int(input('Para qual valor você deseja atualizar?: '))
               break
             except ValueError:
               print('Digite um valor valido!')

        if nomeElement == 1:
             dados_mp10 = [newValue, ID_Element]
             cursor.execute("update parametros set mp10 = :1 where ID = :2", dados_mp10)
             connection.commit()
             #listando a nova amostra
             print('Valor do mp10 atualizado com sucesso!')
             cursor.execute('SELECT mp10, mp2, o3, co, no2, so2 FROM parametros WHERE ID = :1', ID)
             result = list(cursor.fetchone())
             print(f'nova amostra: {result}\n')
        elif nomeElement == 2:
             dados_mp2 = [newValue, ID_Element]
             cursor.execute("update parametros set mp2 = :1 where ID = :2", dados_mp2)
             print('Valor do mp2 atualizado com sucesso!')
             connection.commit()
             #listando a nova amostra
             cursor.execute('SELECT mp10, mp2, o3, co, no2, so2 FROM parametros WHERE ID = :1', ID)
             result = list(cursor.fetchone())
             print(f'nova amostra: {result}\n')
        elif nomeElement == 3:
             dados_o3 = [newValue, ID_Element]
             cursor.execute("update parametros set o3 = :1 where ID = :2", dados_o3)
             print('Valor do o3 atualizado com sucesso!')
             connection.commit()
             #listando a nova amostra
             cursor.execute('SELECT mp10, mp2, o3, co, no2, so2 FROM parametros WHERE ID = :1', ID)
             result = list(cursor.fetchone())
             print(f'nova amostra: {result}\n')
        elif nomeElement == 4:
             dados_co = [newValue, ID_Element]
             cursor.execute("update parametros set co = :1 where ID = :2", dados_co)
             print('Valor do co atualizado com sucesso!')
             connection.commit()
             #listando a nova amostra
             cursor.execute('SELECT mp10, mp2, o3, co, no2, so2 FROM parametros WHERE ID = :1', ID)
             result = list(cursor.fetchone())
             print(f'nova amostra: {result}\n')
        elif nomeElement == 5:
             dados_no2 = [newValue, ID_Element]
             cursor.execute("update parametros set no2 = :1 where ID = :2", dados_no2)
             print('Valor do no2 atualizado com sucesso!')
             connection.commit()
             #listando a nova amostra
             cursor.execute('SELECT mp10, mp2, o3, co, no2, so2 FROM parametros WHERE ID = :1', ID)
             result = list(cursor.fetchone())
             print(f'nova amostra: {result}\n')
        elif nomeElement == 6:
             dados_so2 = [newValue, ID_Element]
             cursor.execute("update parametros set so2 = :1 where ID = :2", dados_so2)
             print('Valor do so2 atualizado com sucesso!')
             connection.commit()
             #listando a nova amostra
             cursor.execute('SELECT mp10, mp2, o3, co, no2, so2 FROM parametros WHERE ID = :1', ID)
             result = list(cursor.fetchone())
             print(f'nova amostra: {result}\n')
        else:
             print('Digite um valor dentro do intervalo!')
        
#Criar funçao classificar
def Classificar():
#USAR AVG PARA REALIZAR A MEDIA
     cursor.execute("SELECT AVG(mp10) from parametros")
     result1 = cursor.fetchone()
     mp10 = result1[0]
     print(f'media mp10: {mp10:.2f}')

     cursor.execute("SELECT AVG(mp2) from parametros")
     result2 = cursor.fetchone()
     mp2 = result2[0]
     print(f'media mp2: {mp2:.2f}')

     cursor.execute("SELECT AVG(o3) from parametros")
     result3 = cursor.fetchone()
     o3 = result3[0]
     print(f'media o3: {o3:.2f}')

     cursor.execute("SELECT AVG(co) from parametros")
     result4 = cursor.fetchone()
     co = result4[0]
     print(f'media co: {co:.2f}')

     cursor.execute("SELECT AVG(no2) from parametros")
     result5 = cursor.fetchone()
     no2 = result5[0]
     print(f'media no2: {no2:.2f}')

     cursor.execute("SELECT AVG(so2) from parametros")
     result6 = cursor.fetchone()
     so2 = result6[0]
     print(f'media so2: {so2:.2f}')

     #classificacao
     if mp10 > 250 or mp2 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 > 800:
          print("\n\nA qualidade do ar está PÉSSIMA,\nou seja, toda a população pode apresentar sérios riscos de manifestações de doençasrespiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.\n\n")

     elif 150 < mp10 <= 250 or 75 < mp2 <= 125 or 160 < o3 <= 200 or 13 < co <= 15 or 320 < no2 <= 1130 or 365 < so2 <= 800:
          print(
               "\n\nA qualidade do ar está MUITO RUIM,\nou seja, toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaçom ardor nos olhos, nariz e garganta e ainda falta de ar e rspiração ofegante. "
               "Efeitos ainda mais graves á saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).\n\n")

     elif 100 < mp10 <= 150 or 50 < mp2 <= 75 or 130 < o3 <= 160 or 11 < co <= 13 or 240 < no2 <= 320 or 40 < so2 <= 365:
          print("\n\nA qualidade do ar está RUIM,\nou seja, toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta."
                    "Pessoas de grupo sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde\n\n")

     elif 50 < mp10 <= 100 or 25 < mp2 <= 50 or 100 < o3 <= 130 or 9 < co <= 11 or 200 < no2 <= 240 or 20 < so2 <= 40:
          print("\n\nA qualidade do ar está MODERADA,\nou seja, pessoas de grupos sensíveis (crianças, idosos e pessoas com doenás respiratórias e cardíacas) "
               "poem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.\n\n")
     else:
          print("\n\nA qualidade do ar está BOA,\nou seja, não afetará a saúde da população.\n\n")


def Excluir():
     connection.commit()

     #Print amostras do BD
     cursor.execute("SELECT * from parametros")
     result_0 = cursor.fetchall()
     for i in range(len(result_0)):
          res = result_0[i]
          print(f'Amostra ID {res[6]}: (mp10: {res[0]} mp2: {res[1]} o3: {res[2]} co: {res[3]} no2: {res[4]} so2: {res[5]})')

     #validando input
     while True:
          try:
               ID_Element = int(input('Digite o ID das amostras: '))
               ID = [ID_Element]
               cursor.execute('SELECT mp10, mp2, o3, co, no2, so2 FROM parametros WHERE ID = :1', ID)
               result = list(cursor.fetchone())
               break
          except ValueError:
               print('Voce digitou um valor invalido!')
          except TypeError:
               print('O ID digitado nao existe!')

     #exclusao da amostra
     print(f'Amostra selecionada: {result}')
     resposta = input("Você relemnte deseja excluir?(s/n): ").lower()

     #confirmacao da exclusao
     if resposta == 's':
          cursor.execute("DELETE FROM parametros WHERE ID = :1", ID)
          print("Amostra excluída com sucesso! ")
          connection.commit()
     elif resposta == 'n':
          print('A amostra nao sera excluida')
     else:
          print('Resposta nao reconhecida, operacao cancelada!')
     