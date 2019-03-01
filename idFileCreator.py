#Alexander Swann
#Friday, February 22, 2019
#CS Applications

#idFileCreator

def makeID(infoList):
    for i in range(len(infoList)):
        idfile = open(infoList[i][0] + infoList[i][1] + 'ID.txt', 'w')
        idfile.write('Name: ' + infoList[i][1] + ', ' + infoList[i][0]+'\nAge: ' + infoList[i][2]+ '\nOccupation: ' + infoList[i][3])
        idfile.close()

makeID([['Alexander','Swann', '15', 'Student'], ['Jahseh', 'Onfroy', '20', 'rapper'], ['Timothy', 'Hornor', 'unknown', 'Army'], ['Gekyume','Onfroy','3 weeks', 'religious figure']])
