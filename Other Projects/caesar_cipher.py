def encryption(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 +97)
    return result

def decryption(text,s):
    result=""
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) - s-65) % 26 +65)
        else:
            result += chr((ord(char) - s-97) % 26 + 97)
    return result

plain = input("Enter Plain Text :- ")
s = int(input("Enter Shift Key :- "))
print("Plain Text :- " , plain)
print("Shift Key :-" , s)
a = encryption(plain,s)
print("Encrypted Text :- " , a)
b = decryption(a,s) ; print("Decrypted Text :- " , b)
