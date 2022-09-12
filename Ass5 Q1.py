#Driver - Adam Bricha (U9233-5585) (50%)
#Navigator - Amro  (U44065831) (50%)



#This program is based off a magic 8 ball. There are 20 random answers that can be given to a question the user asks
# The program will ask the user if they want to ask another question. If the user answers no it will terminate, else
# It will keep asking the user to ask another question until the user enters
#no


import random
import sys
x = random.randint(0,20)
Positive = ["It is certain",'It is decidedly so','Without a doubt','Yes-definetly','You may rely on it','As I see it yes',
            "Most likely","Outlook good","Yes.","Signs point to yes."]
Neutral = ["Reply Hazy,try again.","Ask again later","Better not tell you now.","Cannot predict now","Concentrate and ask again"]

negative = ["Don't count on it", "my reply is no", "my sources say no","outlook not so good","very doubtful"]

combined = ["It is certain",'It is decidedly so','Without a doubt','Yes-definetly','You may rely on it','As I see it yes',
            "Most likely","Outlook good","Yes.","Signs point to yes.","Reply Hazy,try again.",
            "Ask again later","Better not tell you now.","Cannot predict now","Concentrate and ask again",
            "Don't count on it", "my reply is no", "my sources say no","outlook not so good","very doubtful"]



Question = input("Ask the Magic 8 ball a question: ")
while len(Question) ==0:
    Question = input("Ask a real quesition please: ")
else:
    print(combined[x])
x = random.randint(0,20)
anotherq = input("Would you like to ask another question? ")
if anotherq == "no".casefold():
    sys.exit()
else:
    x = random.randint(0,20)
    anotherq = input("What is your question?: ")
    print(combined[x])

    anotherq = input("Would you like to ask another question? ")
while anotherq != 'no':
    x = random.randint(0,20)
    anotherq = input("What is your question?: ")
    print(combined[x])
    anotherq = input("Would you like to ask another question? ")
