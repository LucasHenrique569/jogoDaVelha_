
def printGame(listOfGame_):
    for line in listOfGame_:
        for item in line:
            print(' ', item, sep='|', end=' ')
        print('____________')
    
listOfGame = [['', '', ''], ['', '', ''], ['', '', '']]

inputLine = int(input('Informe o indice da linha: '))
inputColumn = int(input('Informe o indice da coluna: '))


listOfGame[inputLine][inputColumn] = 'X'
printGame(listOfGame)

