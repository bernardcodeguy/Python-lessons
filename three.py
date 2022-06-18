# CH4



reply = input("Keep going?: ")

# While loop
while reply == 'y' or reply == 'Y' or reply == 'Yes':
    print("You are on the right track")
    reply = input("Keep going?: ")



i = 10

# For loop 1
for count in [1,2,3,4,5,6]:
    print('Hello',count)

# For loop
for count in range(10):
    print()
    print('Hello',count)


print()


# Descending
for count in range(10,0,-1):
    print('Hi',count)


for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)