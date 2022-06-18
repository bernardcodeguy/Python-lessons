# Functions CH3


def printMsg():
    print("Hello There")

def printMsg1(age1,age2):
    if age1 > age2:
        print('Player 1 is older Player 2')
    elif age2 > age1:
        print('Player 2 is older Player 1')
    else:
        print('Same age')



def sum(a,b):
    tot = a+b
    return tot


def logicalOp(ans1,ans2,ans3):
    if (ans1 == 'yes' and ans2 =='no'):
        print('You are bisexal')
    elif ans1 == 'no' or ans2 == 'no':
        print('You are Straight')
    elif not(ans3 == 'yes'):
        print('You are Straight ass')



def main():
    print('Welcome')
    printMsg()
    input('Press Enter to continue: ')
    printMsg1(30,30)
    logicalOp('yes','yes','no')
    booleanry = True
    print(booleanry)

main()
