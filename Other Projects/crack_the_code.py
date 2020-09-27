import random

print("===========Crack The Code==========")
print("====There Will Be 10 Tries To Crack The Code====")
print("====R Indicates All The Digits Are Correct====")
print("====Y Indicates Digits Are Correct But At Wrong Place====")
print("====W Indicates Digits Are Wrong====")

def code():
    digit = []
    for i in range(4):
        v = random.randint(0,9)
        digit.append(v)
    return digit

def input_fun():
    a = input("Code :- ")
    return a

def guess():
    a = code()
    i = 0
    while i < 10:
        result = ""
        icode = [int(c) for c in input_fun()]
        if len(icode) != 4:
            print("Enter 4 Digit No Only")
            continue
        if icode == a:
            print("Right !!" , a)
            break
        for element in icode:
            if element in a:
                if icode.index(element) == a.index(element):
                    result += "R"
                else:
                    result += "Y"
            else:
                result += "W"
        print(result)
        i += 1
    else:
        print("You Ran Out Of Trys !! ")
        print("Correct Code Was :- " , a)
guess()
