
from os import system
from time import sleep
from copy import deepcopy

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
def checkIfThereIsAWinner(matrixOfTheGame_):
    possibilities = {
        'lineZero': deepcopy(matrixOfTheGame_[0]),
        'lineOne': deepcopy(matrixOfTheGame_[1]),
        'lineTwo': deepcopy(matrixOfTheGame_[2]),
        'columnZero': list(),
        'columnOne': list(),
        'columnTwo': list(),
        'mainDiagonal': list(),
        'secondaryDiagonal': list(),
    }

    for numberOfTheLine in range(0, 3):
        for numberOfTheColumn in range(0, 3):
            if numberOfTheLine == numberOfTheColumn:
                possibilities['mainDiagonal'].append(matrixOfTheGame_[numberOfTheLine][numberOfTheColumn])

            if numberOfTheColumn == (3 - numberOfTheLine - 1):
                possibilities['secondaryDiagonal'].append(matrixOfTheGame_[numberOfTheLine][numberOfTheColumn])

            if numberOfTheColumn == 0:
                possibilities['columnZero'].append(matrixOfTheGame_[numberOfTheLine][numberOfTheColumn])

            if numberOfTheColumn == 1:
                possibilities['columnOne'].append(matrixOfTheGame_[numberOfTheLine][numberOfTheColumn])

            if numberOfTheColumn == 2:
                possibilities['columnTwo'].append(matrixOfTheGame_[numberOfTheLine][numberOfTheColumn])
            
    # Checar se tem alguma lista com simbolos iguais
    if possibilities['lineZero'].count('X') == 3 or possibilities['lineZero'].count('O') == 3:
        return possibilities['lineZero']
    elif possibilities['lineOne'].count('X') == 3 or possibilities['lineOne'].count('O') == 3:
        return possibilities['lineOne']
    elif possibilities['lineTwo'].count('X') == 3 or possibilities['lineTwo'].count('O') == 3:
        return possibilities['lineTwo']
    elif possibilities['columnZero'].count('X') == 3 or possibilities['columnZero'].count('O') == 3:
        return possibilities['columnZero']
    elif possibilities['columnOne'].count('X') == 3 or possibilities['columnOne'].count('O') == 3:
        return possibilities['columnOne']
    elif possibilities['columnTwo'].count('X') == 3 or possibilities['columnTwo'].count('O') == 3:
        return possibilities['columnTwo']
    elif possibilities['mainDiagonal'].count('X') == 3 or possibilities['mainDiagonal'].count('O') == 3:
        return possibilities['mainDiagonal'] 
    elif possibilities['secondaryDiagonal'].count('X') == 3 or possibilities['secondaryDiagonal'].count('O') == 3:
        return possibilities['secondaryDiagonal']
    else:
        return []


mainUserInput = '0'

while mainUserInput != '2':
    printInitialMenu()
    mainUserInput = input('Digite a opção desejada: ')

    if mainUserInput == '1':
        matrixOfTheGame = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        print('\nJogador 1 = "X" ')
        print('Jogador 2 = "O" ')

        userWantToContinue = 'S'

        while userWantToContinue == 'S' or userWantToContinue == 's':
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

            userWantToContinue = input('Deseja continuar jogando ou voltar ao menu principal ? (s) para sim e (n) para não: ')


# printRulesOfTheGame()
# print('\n')


