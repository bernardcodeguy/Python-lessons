#CH7


def main():
    #Writing to file
    fileOpen = open('hello.txt','w')


    fileOpen.write("Hi\n")
    fileOpen.write("Hello\n")
    fileOpen.close();

    print('Reading from the file')
    fileRead = open('hello.txt', 'r')
    readDataLine = fileRead.readline();
    #readData = fileRead.read();



    #print(readData)
    print("+++++++")
    print(readDataLine)


    #Appending
    try:
        fileOpen = open('hello.txt', 'a')
        fileOpen.write("Hell Yh")
    except Exception as err:
        print(err.__str__())

main()