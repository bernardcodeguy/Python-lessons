#CH8


# Lists
def main():
    nameList = [1,2,3,4,5,6,7,8,9,10]
    for i in nameList:
        print(i,end=' ')
    nameList.append(11)
    print()
    for i in nameList:
        print(i,end=' ')

    print()
    mulList = nameList * 2
    print(mulList)

    # Built-in list creation
    numbers = list(range(1,10,2))
    print()
    print(numbers)

    #Slicing
    numbre = [1,2,3,4,5,6,7,8]
    print()
    print(numbre[0:5])


def main1():
    nameList = (1,2,3,4,5,6,7,8,9,10)
    for i in range(len(nameList)):
        print(nameList[i],end=" ")

    convertToList = list(nameList)
    print(convertToList)


main1()