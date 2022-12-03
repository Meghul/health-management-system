import datetime


def gettime():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food\n"))
        if c==1:
            value=input("Type here\n")
            with open("Madhur-exercise.txt","a") as op:
                op.write(str([str(gettime())])+":"+value)
                print("Data saved successfully ")
        elif c==2:
            value=input("Type here\n")
            with open("Madhur-food.txt","a") as op:
                op.write(str([str(gettime())])+":",value)
                print("Data saved successfully")
    elif k==2:
        c=int(input("Enter 1 for exercise and 2 for food\n" ))
        if c==1:
            value=input("Type here\n")
            with open("Vishwas-exercise.txt","a") as op:
                op.write(str([str(gettime())])+":"+value)
                print("Data saved successfully")
        elif c==2:
            value=input("Type here\n")
            with open("Vishwas-food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value)
                print("Data saved successfully")

    elif k==3:
        c=int(input("Enter 1 for exercise and 2 for food\n"))
        if c==1:
            value=input("Type here\n")
            with open("Meghul-exercise.txt","a") as op:
                op.write(str([str(gettime())])+":"+value)
                print("Data saved successfully")
        elif c==2:
            value=(input("Type here\n"))
            with open("Meghul-food.txt","a") as op:
                op.write(str([str(gettime())]) + ":"+value)
                print("Data saved successfully")
    else:
        print("Please enter  valid value: 1-Madhur, 2-Vishwas, 3-Meghul")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food\n"))
        if c==1:
            with open("Madhur-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("Madhur-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        c=int(input("Enter 1 for exercise and 2 for food\n"))
        if c==1:
            with open("Vishwas-exercise.txt") as op:
                for i in op:
                    print(i,end="")

        elif c == 2:
            with open("Vishwas-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==3:
        c=int(input("Enter 1 for exercise and 2 for food\n"))
        if c==1:
            with open("Meghul-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        if c==2:
            with open("Meghul-food.txt") as op:
                for i in op:
                    print(i,end="")
    else:
        print("Please enter valid value: 1-Madhur, 2-Vishwas, 3-Meghul")
print("Health Management System: ")
a=int(input("Press 1 for log the value and 2 for retrieve\n"))

if a==1:
    b=int(input("Press 1 for Madhur, 2 for Vishwas and 3 for Meghul"))
    take(b)
elif a==2:
    b=int(input("press 1 for Madhur, 2 for Vishwas and 3 for Meghul"))
    retrieve(b)









