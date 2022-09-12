#Driver(50%) - Adam Bricha (U9233-5585)
#Navigator(50%) - Juliana El Rayes (U0355-9866)

#This program reads a text file from the user. The program then takes each character and encypts the file and saves
#it as a .txt. The user has the choice to read the new file and display it to the console.







Encrypt_Code = {'A': ')', 'a': '0', 'B': '(', 'b': '9', 'C': '*', 'c': '8', \
                'D': '&', 'd': '7', 'E': '^', 'e': '6', 'F': '%', 'f': '5', \
                'G': '$', 'g': '4', 'H': '#', 'h': '3', 'I': '@', 'i': '2', \
                'J': '!', 'j': '1', 'K': 'Z', 'k': 'z', 'L': 'Y', 'l': 'y', \
                'M': 'X', 'm': 'x', 'N': 'W', 'n': 'w', 'O': 'V', 'o': 'v', \
                'P': 'U', 'p': 'u', 'Q': 'T', 'q': 't', 'R': 'S', 'r': 's', \
                'S': 'R', 's': 'r', 'T': 'Q', 't': 'q', 'U': 'P', 'u': 'p', \
                'V': 'O', 'v': 'o', 'W': 'N', 'w': 'n', 'X': 'M', 'x': 'm', \
                'Y': 'L', 'y': 'l', 'Z': 'K', 'z': 'k', '!': 'J', '1': 'j', \
                '@': 'I', '2': 'i', '#': 'H', '3': 'h', '$': 'G', '4': 'g', \
                '%': 'F', '5': 'f', '^': 'E', '6': 'e', '&': 'D', '7': 'd', \
                '*': 'C', '8': 'c', '(': 'B', '9': 'b', ')': 'A', '0': 'a', \
                ':': ',', ',': ':', '?': '.', '.': '?', '<': '>', '>': '<', \
                "'": '"', '"': "'", '+': '-', '-': '+', '=': ';', ';': '=', \
                '{': '[', '[': '{', '}': ']', ']': '}'}

def main():
    inputfile = str(input('What would you like to encrypt? (enter as .txt): '))
    notyetencryptedtext = open(inputfile, 'r')
    notyetencryptedtext = notyetencryptedtext.readlines()


    encryptText(notyetencryptedtext)

def encryptText(notyetencryptedtext):
    outputfile = str(input('What would you like to save your encrypted file as (enter as .txt): '))
    encryptedtext = open(outputfile, 'w')

    for y in notyetencryptedtext:

        for i in y:
            encrypted = (Encrypt_Code.get(i, i))
            encryptedtext.write(encrypted)

    encryptedtext.close()

main()
op1= input("would you like to read your encyrpted file? ")
while op1 != 'no':
    x = input("enter the name as .txt to open it:")
    with open(x,'r') as file:
        print(file.read())
else:
    quit()