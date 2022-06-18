

def main():
    names = ["Bernard","Lionel","Samuel"]
    ages = [26,35,24]
    emails = ["bernmen2022@yahoo.com","messi@yahoo.com","sammy@gmail.com"]
    tab = {
        "Name":names,
        "Age":ages,
        "Email": emails
           }

    print(tab)
    print('After addig new element')
    skills = ['Programming','Playing football','Nursing']
    tab['skill'] = skills
    print(tab)
    del tab['skill']
    print(tab)
    mathsFxn()

def mathsFxn():
    s1 = {1,2,3,4,5,6,7,8,9}
    s2 = {1,3,5,7,9,11}

    print(s1.union(s2))

main()