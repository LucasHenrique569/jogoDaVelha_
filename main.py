
from os import system
from time import sleep

# testado
def printGame(listOfGame_):
    print('\n')
    for index, line in enumerate(listOfGame_):
        for index_, item in enumerate(line):
            # consertar essa porqueira depois
            if index_ == 1:
                print('| ', item, ' |', end='')
            elif index_ == 2:
                print(' ', item, end='')
            else:
                print('  ', item, ' ', end='')
        
        if not index == 2:
            print('\n', '_'*17, '\n')
    print('\n')


# testado
def printInitialMenu():
    print('Olá, bem vindo ao jogo da velha !!! ')
    print('Menu de opções: ')
    print('     1: Iniciar novo jogo')
    print('     2: Sair\n')


# testado
def printRulesOfTheGame():
    print('Para posicionar o icone na posição desejada no quadro, informe o indice da linha e da coluna de acordo com a posição na matriz que você deseja inserir o icone, veja a ilustração abaixo: \n')
    for line in range(0, 3):
        if line == 0:
            print('    ', 0, ' '*3, '1', ' '*3, '2', '  \n')

        print(line, '  ', end='')
        for column in range(0, 3):
            
            if column == 1:
                print('|     |', end='')
            else:
                print('    ',end='')
        
        if not line == 2:
            print('\n  ', '_'*17, '\n')


# testado
def validateUsersInputPosition(matrixOfTheGame_, line, column):
    convertedLine = line
    convertedColumn = column

    try:
        convertedLine = int(line)
        convertedColumn = int(column)
    except ValueError:
        print('Por favor, tente novamente, você informou algo inválido.')
        return False
    finally:
        positionIsEmpty = True if matrixOfTheGame_[convertedLine][convertedColumn] == ' ' else False

        if positionIsEmpty:
            return True
        else:
            print('Por favor, tente novamente, você informou as coordenadas de uma posição inválida.')
            return False
    
    
# continuar a partir daqui
def checkIfThereIsAWinner():
    for numberOfTheLine in range(0, 3):
        for numberOfTheColumn in range(0, 3):
            ...

mainUserInput = '0'
matrixOfTheGame = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]

while mainUserInput != '2':
    printInitialMenu()
    mainUserInput = input('Digite a opção desejada: ')

    if mainUserInput == '1':
        print('\nJogador 1 = "X" ')
        print('Jogador 2 = "O" ')

        validPosition = False

        while not validPosition:
            print('É a vez do jogador 1, por favor digite uma posição válida')
            userOneInputLine = input('Informe o indice da linha: ')
            userOneInputColumn = input('Informe o indice da coluna: ')

            validPosition = validateUsersInputPosition(matrixOfTheGame, userOneInputLine, userOneInputColumn)
            sleep(1)
            system('cls')

        matrixOfTheGame[int(userOneInputLine)][int(userOneInputColumn)] = 'X'
        printGame(matrixOfTheGame)

        validPosition = False

        while not validPosition:
            print('É a vez do jogador 2, por favor digite uma posição válida')
            userOneInputLine = input('Informe o indice da linha: ')
            userOneInputColumn = input('Informe o indice da coluna: ')

            validPosition = validateUsersInputPosition(matrixOfTheGame, userOneInputLine, userOneInputColumn)
            sleep(1)
            system('cls')

        matrixOfTheGame[int(userOneInputLine)][int(userOneInputColumn)] = 'O'
        printGame(matrixOfTheGame)

# printRulesOfTheGame()
# print('\n')
