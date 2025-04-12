
from os import system
from copy import deepcopy
from msvcrt import getch

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
    print('     2: Ver regras do jogo')
    print('     3: Sair\n')


# testado
def printRulesOfTheGame():
    print('\nPara posicionar o icone na posição desejada no quadro, informe o indice da linha e da coluna de acordo com a posição na matriz que você deseja inserir o icone, veja a ilustração abaixo: \n')
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
    print('\n')


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
    
    
# ainda precisa ser testada
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


# testado
def printWhichPlayerWonTheGame(matrixOfTheGame__):
    
    # não tem vencedor
    if matrixOfTheGame__ == []:
        return ' '
    elif matrixOfTheGame__.count('X') == 3: 
        return '\033[1;32mJogador 1 venceu !!! \033[0m'
    else:
        return '\033[1;32mJogador 2 venceu !!! \033[0m'

# ainda precisa ser testado
def handleUsersTurn(matrixOfTheGame, whichPlayerSTurnIsIt, playerIcon):
    validPosition = False

    while not validPosition:
        print(f'\nÉ a vez do jogador {whichPlayerSTurnIsIt}, por favor digite uma posição válida')
        userOneInputLine = input('Informe o indice da linha: ')
        userOneInputColumn = input('Informe o indice da coluna: ')

        validPosition = validateUsersInputPosition(matrixOfTheGame, userOneInputLine, userOneInputColumn)

    matrixOfTheGame[int(userOneInputLine)][int(userOneInputColumn)] = playerIcon
    printGame(matrixOfTheGame)

# testado
def cleanScreen():
    print('\nPressione qualquer tecla para continuar ...')
    getch()
    system('cls')


mainUserInput = '0'

while mainUserInput != '3':
    printInitialMenu()
    mainUserInput = input('Digite a opção desejada: ')

    match mainUserInput:
        case '1':
            matrixOfTheGame = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

            print('\nJogador 1 = "X" ')
            print('Jogador 2 = "O" ')

            userWantToContinue = 'S'

            while userWantToContinue == 'S' or userWantToContinue == 's':

                # É a vez do jogador 1
                controlsWhichPlayerSTurnItIs = 1
                handleUsersTurn(matrixOfTheGame, controlsWhichPlayerSTurnItIs, 'X')

                possibleWinner = printWhichPlayerWonTheGame(checkIfThereIsAWinner(matrixOfTheGame))
                print('\n', possibleWinner)

                cleanScreen()

                # Sai do loop caso tenha um vencedor
                if possibleWinner != ' ':
                    break
                    
                # É a vez do jogador 2
                controlsWhichPlayerSTurnItIs = 2
                handleUsersTurn(matrixOfTheGame, controlsWhichPlayerSTurnItIs, 'O')

                possibleWinner = printWhichPlayerWonTheGame(checkIfThereIsAWinner(matrixOfTheGame))
                print('\n', possibleWinner)

                cleanScreen()

                # Sai do loop caso tenha um vencedor
                if possibleWinner != ' ':
                    break

                # lidar melhor com a resposta do usuário depois
                userWantToContinue = input('Deseja continuar jogando ou voltar ao menu principal ? (s) para sim e qualquer outra tecla para não: ')
        case '2':
            printRulesOfTheGame()
        case '3':
            print('\nThank you for playing with us. See you next time.')
        case _:
            print('\nPlease, write a suitable input.')

    cleanScreen()

