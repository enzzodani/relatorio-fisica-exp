import csv

with open('/home/marinho/Documents/fisica-exp/Exp04_Aceleracao_da_gravidade_local.csv', newline='') as csvfile:

    linereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    del linereader[0:5]
    for index, row in enumerate(linereader):
        print(index)
        print(row)
        