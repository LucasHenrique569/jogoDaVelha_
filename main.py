
def printGame(listOfGame_):
    print('\n')
    for index, line in enumerate(listOfGame_):
        for index_, item in enumerate(line):
            if index_ == 1:
                print('| ', item, ' |', end='')
            else:
                print(' ', item, ' ', end='')
        
        if not index == 2:
            print('\n', '_'*15, '\n')
    print('\n')

def printInitialMenu():
    print('Olá, bem vindo ao jogo da velha !!! ')
    print('Menu de opções: ')
    print('     1: Iniciar novo jogo')
    print('     2: Sair')

def printRulesOfTheGame():
    print('Jogador 1 = "X"')
    print('Jogador 2 = "O"')

    print('Para posicionar o icone na posição desejada no quadro, informe o indice da linha e da coluna de acordo com a posição na matriz que você deseja inserir o icone, veja a ilustração abaixo: ')
    for line in range(0, 3):
        if line == 0:
            print('    ', 0, ' '*4, '1', ' '*4, '2', '  \n')

        for column in range(0, 3):
            if column == 1:
                print(line, '| ', ' ', ' |', end='')
            else:
                print(line, ' ', ' ', ' ', end='')
        
        if not line == 2:
            print('\n  ', '_'*17, '\n')


# mainUserInput = '0'

# while mainUserInput != '2':
#     printInitialMenu()
#     mainUserInput = input('\nDigite a opção desejada: ')

#     if mainUserInput == 1:
#         listOfGame = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

#         inputLine = int(input('Informe o indice da linha: '))
#         inputColumn = int(input('Informe o indice da coluna: '))

#         listOfGame[inputLine][inputColumn] = 'X'
#         printGame(listOfGame)

printRulesOfTheGame()