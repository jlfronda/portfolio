letter=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

t = input("Enter text: ")
k = int(input("Enter key: "))
choice=input("E for Encrypt, D for Decrypt: ")

def encryption(b, key):
    C=""
    for i in b:
        if i.isalpha():
            s=letter.index(i)
            if i.isupper():
                E = letter[((s+ key) %  26)]
            else:
                E = letter[((s+ key) %  26)+26]
            C=C+E
        else:
            C=C+i
    print(C)
def decryption(b, key):
    C=""
    for i in b:
        if i.isalpha():
            s=letter.index(i)
            if i.isupper():
                E = letter[((s- key) %  26)]
            else:
                E = letter[((s- key) %  26)+26]
            C=C+E
        else:
            C=C+i
    print(C)

if choice=='E' or choice=='e':
    encryption(t,k)
elif choice=='D' or choice=='d':
    decryption(t,k)

