q1 = ["I want list", "i want data of all students", "i want complete data"]
pairr = {}
def val(name, age, add, gender):
    newlist1=[]
    newlist1.append(name)
    newlist1.append(age)
    newlist1.append(add)
    newlist1.append(gender)
    return newlist1

def std(idd):
    return idd

chk = True

def insst():
    aa = input("Please enter Student ID: ")
    bb = input("Please enter Student Name: ")
    cc = int(input("Please enter Student Age: "))
    dd = input("Please enter Student Address: ")
    ee = input("Please enter Student Gender: ")
    pairr[std(aa)]=val(bb,cc,dd,ee)
    print("New Student " + bb + " Added")
    return pairr

    #print("New Student " + bb + " Added")

def ins():
    b = input("Do you want to add Student? ")
    if b == 'yes':
        insst()
    else:
        print("Ok as you wish.\n Quitting....")
        chk = False

# program starts from here

anchk = True
while chk:

    f=input("What is your purpose here? ")
    if q1.__contains__(f):
        print(pairr)
        ins()
        while anchk:
            again = input("Do you want to add another student? ")
            if again=='yes':
                insst()
            else:
                print("This is ur list of students \n"+ str(pairr))
                anchk=False
                break

        #chk = False
    else:
        print("I dont get it.")
        a=input("Do you want to try again? ")
        if a== 'yes':
            ins()
        else:
            print("quitting...")
            break

