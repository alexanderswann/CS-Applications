#Alexander Swann
#Friday, February 22, 2019
#CS Applications

#StringBuildingAndParsingLists

def numberString(num):
    numlist = ""
    for i in range(int(num)):
        numlist+=(str(i+1))
    return numlist
print(numberString(9))

def hill(n):
    numlist = ""
    for i in range(int(n+1)):
        numlist+=(str(i)*i)+('\n')
    return numlist
print(hill(9))

def valley(n):
    numlist = ""
    for i in range(int(n+1)):
        numlist+=((str(i)*i)+(str(' '*((2*n)-(2*i))))+(str(i)*i)+('\n'))
    return (numlist)
print(valley(9))


def endsZero(aList):
    numzero = 0
    for i in aList:
        if i % 10 == 0:
            numzero+=1
    return numzero
print(endsZero([3000,90,324,234,2,4]))


def countLengths(litsOfLists):
    numlist = []
    for i in range(len(litsOfLists)):
        numlist.append(len(litsOfLists[i]))
    return numlist
print(countLengths([[3,4,2],[],[90,23,234,True]]))


def findAverages(numLists):
    numlist = []
    for i in range(len(numLists)):
        avg = 0
        for ii in numLists[i]:
            avg += ii
        numlist.append(avg/len(numLists[i]))
    return numlist
print(findAverages([[3,4,2],[3,3],[9]]))
