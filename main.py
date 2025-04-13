
from os import system
from copy import deepcopy
from msvcrt import getch

# testado
def printGame(matrixOfTheGame):
    print('\n')
    for index, line in enumerate(matrixOfTheGame):
        for index_, item in enumerate(line):
            # consertar essa porqueira depois
            if index_ == 1:
                print(f'\033[1;36m|\033[0m ', f'\033[1;37m{item}\033[0m', f' \033[1;36m|\033[0m', end='')
            elif index_ == 2:
                print(' ', f'\033[1;37m{item}\033[0m', end='')
            else:
                print('  ', f'\033[1;37m{item}\033[0m', ' ', end='')
        
        if not index == 2:
            print('\n', f'\033[1;36m_\033[0m'*17, '\n')
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
    print('\nPara posicionar o icone na posição desejada na matriz, informe o indice da linha e da coluna de acordo com a ilustração abaixo: \n')
    for line in range(0, 3):
        if line == 0:
            print('    ', f'\033[1;35m0\033[0m', ' '*3, f'\033[1;35m1\033[0m', ' '*3, f'\033[1;35m2\033[0m', '  \n')

        print(f'\033[1;33m{line}\033[0m', '  ', end='')
        for column in range(0, 3):
            
            if column == 1:
                print('|     |', end='')
            else:
                print('    ',end='')
        
        if not line == 2:
            print('\n  ', '_'*17, '\n')

    print('\n\n\n\033[1;32mHAVERÁ UM \033[1;37mVENCEDOR\033[0m NOS SEGUINTES CASOS: \033[0m')
    print('\033[1;32m- ICONES IGUAIS EM TODAS AS POSIÇÕES DE UMA LINHA\033[0m')
    print('\033[1;32m- ICONES IGUAIS EM TODAS AS POSIÇÕES DE UMA COLUNA\033[0m')
    print('\033[1;32m- ICONES IGUAIS NA DIAGONAL PRINCIPAL\033[0m')
    print('\033[1;32m- ICONES IGUAIS NA DIAGONAL SECUNDÁRIA\033[0m')
    print('\n\033[1;32mO JOGO TERMINARÁ \033[1;37mEMPATADO\033[0m CASO NENHUM DOS CASOS ACIMA ACONTECER E A MATRIZ NÃO ACEITAR MAIS ICONES\033[0m')


# testado
def validateUsersInputPosition(matrixOfTheGame, line, column):
    convertedLine = line
    convertedColumn = column

    try:
        convertedLine = int(line)
        convertedColumn = int(column)
    except ValueError:
        print('Por favor, tente novamente, você informou algo inválido.')
        return False

    thereIsANegativeNumber = True if convertedLine < 0 or convertedColumn < 0 else False
    thereIsANumberBiggerThan3 = True if convertedLine > 2 or convertedColumn > 2 else False

    if thereIsANegativeNumber or thereIsANumberBiggerThan3:
        print('Por favor, tente novamente, você informou as coordenadas de uma posição inválida.')
        return False
    
    positionIsEmpty = True if matrixOfTheGame[convertedLine][convertedColumn] == ' ' else False

    if positionIsEmpty:
        return True

    print('Por favor, tente novamente, você informou as coordenadas de uma posição inválida.')
    return False
    
    
# testado
def checkIfThereIsAWinner(matrixOfTheGame):
    possibilities = {
        'lineZero': deepcopy(matrixOfTheGame[0]),
        'lineOne': deepcopy(matrixOfTheGame[1]),
        'lineTwo': deepcopy(matrixOfTheGame[2]),
        'columnZero': list(),
        'columnOne': list(),
        'columnTwo': list(),
        'mainDiagonal': list(),
        'secondaryDiagonal': list(),
    }

    for numberOfTheLine in range(0, 3):
        for numberOfTheColumn in range(0, 3):
            if numberOfTheLine == numberOfTheColumn:
                possibilities['mainDiagonal'].append(matrixOfTheGame[numberOfTheLine][numberOfTheColumn])

            if numberOfTheColumn == (3 - numberOfTheLine - 1):
                possibilities['secondaryDiagonal'].append(matrixOfTheGame[numberOfTheLine][numberOfTheColumn])

            if numberOfTheColumn == 0:
                possibilities['columnZero'].append(matrixOfTheGame[numberOfTheLine][numberOfTheColumn])

            if numberOfTheColumn == 1:
                possibilities['columnOne'].append(matrixOfTheGame[numberOfTheLine][numberOfTheColumn])

            if numberOfTheColumn == 2:
                possibilities['columnTwo'].append(matrixOfTheGame[numberOfTheLine][numberOfTheColumn])
            
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
def printWhichPlayerWonTheGame(matrixOfTheGame):
    
    # não tem vencedor
    if matrixOfTheGame == []:
        return ' '
    elif matrixOfTheGame.count('X') == 3: 
        return '\033[1;32m      JOGADOR 1 VENCEU !!! \033[0m'
    else:
        return '\033[1;32m      JOGADOR 2 VENCEU !!! \033[0m'

# testado
def handleUsersTurn(matrixOfTheGame, whichPlayerSTurnIsIt, playerIcon):
    validPosition = False

    while not validPosition:
        print(f'\nÉ a vez do jogador {whichPlayerSTurnIsIt}, por favor digite uma posição válida')
        userInputLine = input('Informe o indice da linha: ')
        userInputColumn = input('Informe o indice da coluna: ')

        validPosition = validateUsersInputPosition(matrixOfTheGame, userInputLine, userInputColumn)

    matrixOfTheGame[int(userInputLine)][int(userInputColumn)] = playerIcon
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
            verifyIfTheGameTied = 0

            print('\n\033[1;32mJogador 1 = "X" \033[0m')
            print('\033[1;32mJogador 2 = "O" \033[0m')

            seeIfUserWantToContinue = 'S'

            while seeIfUserWantToContinue == 'S' or seeIfUserWantToContinue == 's':

                # É a vez do jogador 1
                controlsWhichPlayerSTurnItIs = 1
                handleUsersTurn(matrixOfTheGame, controlsWhichPlayerSTurnItIs, 'X')

                possibleWinner = printWhichPlayerWonTheGame(checkIfThereIsAWinner(matrixOfTheGame))
                print('\n', possibleWinner)

                # Sai do loop caso tenha um vencedor
                if possibleWinner != ' ':
                    break
                    
                verifyIfTheGameTied += 1
                
                if verifyIfTheGameTied == 9:
                    print('\033[1;32m     DEU VELHA !!! \033[0m')
                    break
                
                cleanScreen()

                # É a vez do jogador 2
                controlsWhichPlayerSTurnItIs = 2
                handleUsersTurn(matrixOfTheGame, controlsWhichPlayerSTurnItIs, 'O')

                possibleWinner = printWhichPlayerWonTheGame(checkIfThereIsAWinner(matrixOfTheGame))
                print('\n', possibleWinner)

                cleanScreen()

                # Sai do loop caso tenha um vencedor
                if possibleWinner != ' ':
                    break
                
                verifyIfTheGameTied += 1

                # lidar melhor com a resposta do usuário depois
                seeIfUserWantToContinue = input('Deseja continuar jogando ou voltar ao menu principal ? (s) para sim e qualquer outra tecla para não: ')
        case '2':
            printRulesOfTheGame()
        case '3':
            print('\nObrigado, até mais.')
        case _:
            print('\nOpção inválida, por favor, tente novamente.')

    cleanScreen()
