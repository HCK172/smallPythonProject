import random 
''' 
count = 0
number = random.randint(1,20)
print("I'm thinking of a number between 1 and 20")

for i in range(20):
    guess = int(input("Take a guess"))
    count = count + 1 
    if guess == number:
        break
    elif guess > number: 
        print("The guess is too high")
        continue
    elif guess < number: 
        print("The guess is too low") 
        continue
print(f"Good job! You guessed my number in {count} guess.")'''


## import random, sys, os, math
### third party modules


'''
print("Let's play Rock, Paper, Scissors!")
win = 0 
loss = 0
tie = 0

while True: # the main game loop
    print(f"{win} Wins,{loss} Losses, {tie} Ties")

    # the playMove loop
    while True: 
        playerMove = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit \n").lower().rstrip()
        if playerMove == 'q':
            print("Thank you for playing!")
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove=='s':
            break
        print("Type one of r , p , s or q")

    # Display what the player chose
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's': 
        print('Scissors versus...')

    # display what the computer choose 
    random_num = random.randit(1,3)
    if random_num == 1: 
        computerMove = 'r'
        print('Rock')
    elif random_num == 2: 
        computerMove = 'p'
        print('Paper')
    elif random_num == 3: 
        computerMove = 's'
        print('Scissors')
  '''
  
### function 
def getAnswers(answerNumber):
        if answerNumber == 1:
                return 'It is certain'
        elif answerNumber == 2:
                return 'Yes'
        elif answerNumber == 3:
                return 'very doubtful'

r = random.randint(1,3)
fortune = getAnswers(r)
print(fortune)
    
####

import time, sys
indent = 0 
indentincreasing = True

try: 
    while True:
        print(' '* indent, end='')
        print('*******')
        time.sleep(0.1)
        
        if indentincreasing: 
           indent = indent + 1
           if indent == 20:
                  indentincreasing = False
        else:
           indent = indent - 1 
           if indent == 0:
                  indentincreasing = True

except KeyboardInterrupt:
    sys.exit()


###### 


def collatz(num) :

    count = 1 
    while (num != 1):
        count = count+1
        if num % 2 == 0:
            num = num//2
            print(num)
        else:
            num = 3*num+1
            print(num)

    print(f'{count} times')

num = int(input('Enter a number:\n'))
collatz(num)

######

message = '''I love you very very very much.'''

characterCount = {}
wordCount = {}
for character in message : 
     characterCount.setdefault(character,0)
     characterCount[character] = characterCount[character] + 1
## print(count)

message = message.split(' ')
totalWordCount = len(message)

for word in message: 
     wordCount.setdefault(word, 0)
     wordCount[Word] = wordCount[Word] + 1 