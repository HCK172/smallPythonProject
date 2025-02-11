allGuests = {'Jenny':{'apples':5, 'pretzels':6},
             'Philip':{'Soju':8, 'apples':2},
             'Linda':{'cupcake': 11, 'cups':4}}

def totalBought(guests, item):
    numBought = 0 
    for k, v in guests.items():
        numBought = numBought + v.get(item, 0)
    return numBought

print('Number of things being bought:')
print(' - Apples ' + str(totalBought(allGuests,'apples')))
print(' - Soju   ' + str(totalBought(allGuests, 'Soju')))
