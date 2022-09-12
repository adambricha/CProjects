#Driver - Adam Bricha (U9233-5585) (50%)
#Navigator - Amro  (U44065831) (50%)



#This program is quiz based off the capitals of the USA states.
# The program will ask the user to the capital of a random state. The program will keep track of the users score
# If the user answers q it will terminate, else
# It will keep asking the user to answer the question



import random

def game():
    Dict = {'Alabama': 'Montgomery',
                 'Alaska': 'Juneau',
                 'Arizona': 'Phoenix',
                 'Arkansas': 'Little Rock',
                 'California': 'Sacramento',
                 'Colorado': 'Denver',
                 'Connecticut': 'Hartford',
                 'Delaware': 'Dover',
                 'Florida': 'Tallahassee',
                 'Georgia': 'Atlanta',
                 'Hawaii': 'Honolulu',
                 'Idaho': 'Boise',
                 'Illinois': 'Springfield',
                 'Indiana': 'Indianapolis',
                 'Iowa': 'Des Moines',
                 'Kansas': 'Topeka',
                 'Kentucky': 'Frankfort',
                 'Louisiana': 'Baton Rouge',
                 'Maine': 'Augusta',
                 'Maryland': 'Annapolis',
                 'Massachusetts': 'Boston',
                 'Michigan': 'Lansing',
                 'Minnesota': 'Saint Paul',
                 'Mississippi': 'Jackson',
                 'Missouri': 'Jefferson City',
                 'Montana': 'Helena',
                 'Nebraska': 'Lincoln',
                 'Nevada': 'Carson City',
                 'New Hampshire': 'Concord',
                 'New Jersey': 'Trenton',
                 'New Mexico': 'Santa Fe',
                 'New York': 'Albany',
                 'North Carolina': 'Raleigh',
                 'North Dakota': 'Bismarck',
                 'Ohio': 'Columbus',
                 'Oklahoma': 'Oklahoma City',
                 'Oregon': 'Salem',
                 'Pennsylvania': 'Harrisburg',
                 'Rhode Island': 'Providence',
                 'South Carolina': 'Columbia',
                 'South Dakota': 'Pierre',
                 'Tennessee': 'Nashville',
                 'Texas': 'Austin',
                 'Utah': 'Salt Lake City',
                 'Vermont': 'Montpelier',
                 'Virginia': 'Richmond',
                 'Washington': 'Olympia',
                 'West Virginia': 'Charleston',
                 'Wisconsin': 'Madison',
                 'Wyoming': 'Cheyenne'}

    statesList = list(Dict)

    correct = 0
    incorrect = 0


    while True:
        x = random.randint(0, 49)
        state = statesList[x]
        answer = input("What is the capital of {} ?(or enter q to quit) ".format(state))
        if (answer == Dict[state]):
            correct += 1
            print("That is correct")
        elif answer != Dict[state] and answer != 'q':
            incorrect += 1
            print("That is Incorrect")
        if answer == 'q':
            print("You had", correct, "correct answers and", incorrect, "incorrect answers")
            quit()



game()