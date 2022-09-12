#Navigator(50%) - Adam Bricha (U9233-5585)
#Driver(50%) - Juliana El Rayes (U0355-9866)


#This program accepts and reads a file, translates it to Pig Latin and writes the output to another text file.
# It first removes the first letter, place it at the end of the word, and then add the string 'ay' at the end.

def translator():
    originalFile = input("Enter the name of file you want to translate (include .txt at the end): ")
    TranslatedFile = input("Enter the name of file you want to save your translated text (include .txt at the end): ")

    p = open(originalFile, "r")
    r = p.read()
    l = r.lower()
    s = l.split("\n")
    PigLatinWords = []
    for i in s:
        PigLatinWords.append(i.split(" "))
    print(PigLatinWords)

    pigLatinLines = []
    for line in PigLatinWords:
        pigLatinLine = []
        for word in line:
            if len(word) < 1:
                pigLatinWord = word + "ay"
            elif word[-1] == ";":
                pigLatinWord = word[1:-1] + word[0] + "ay;"
            elif word[-1] == ",":
                pigLatinWord = word[1:-1] + word[0] + "ay,"
            elif word[-1] == ".":
                pigLatinWord = word[1:-1] + word[0] + "ay."
            elif word[-1] == ":":
                pigLatinWord = word[1:-1] + word[0] + "ay:"
            else:
                pigLatinWord = word[1:] + word[0] + "ay"
            pigLatinLine.append(pigLatinWord)
        pigLatinLines.append(pigLatinLine)
    print(pigLatinLines)

    x = open(TranslatedFile, "w")
    for pigLatinLine in pigLatinLines:
        for pigLatinWord in pigLatinLine:
            x.write(pigLatinWord + " ")
        x.write("\n")


translator()
