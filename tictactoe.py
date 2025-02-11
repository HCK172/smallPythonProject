import pprint

theBroad = {'top-L':' ', 'top-M': ' ', 'top-R': ' ', 
            'mid-L':' ', 'mid-M': ' ', 'mid-R':' ',
            'low-L':' ', 'low-M': ' ', 'low-R':' '} 

pprint.pprint(theBroad)


## building out the board 
def printBroad(broad):
    print(broad['top-L'] +'|' + broad['top-M']+'|'+broad['top-R'])
    print('-+-+-')
    print(broad['mid-L'] +'|' + broad['mid-M']+'|'+broad['mid-R'])
    print('-+-+-')
    print(broad['low-L'] +'|' + broad['low-M']+'|'+broad['low-R'])

#### if the user input is not one of the keys in the dic??
### finish the game and claim a winner



turn = 'X'
for i in range(9):
    printBroad(theBroad)
    print('Turn for ' + turn + ' . Move on which space?')
    move = input()
    theBroad[move] = turn
    if turn == 'X':
        turn = 'O'
    else: 
        turn = 'X'

printBroad(theBroad)