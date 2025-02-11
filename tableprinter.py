tableData = [['apples','oranges','cherries','bananas'],
             ['Alice','Bob','Taylor','David','Carol'],
             ['dog','cat','duck', 'moose']]

colWidth = [0] * len(tableData)



for i in range(len(tableData)): 
    length = []
    for x in tableData[i]: 
        length.append(len(x))
        colWidth[i] = max(length)

print(colWidth)

for i in range(len(colWidth)):
    for x in range(len(tableData[i])): 
        new = tableData[i][x].rjust(colWidth[i],'$')


print(new)