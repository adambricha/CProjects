#Adam Bricha U9233-5585
#This is the driver program for Bottles. It accepts user input and using the class definitions to display what the user
# has ordered, the total cost, the subtotal cost, and the price per bottle. The user can only get up to 3 of the same type of wine





import Bottles


def mainAB():
    DiffTypes = int(input("How many different types of wine will you order today? "))
    while DiffTypes < 1:
        DiffTypes = int(input("Number must be at least 1. How many different types of wine will you order today?"))
    wine = []

    for i in range(DiffTypes):
        print("Wine Type #", i +1 )
        name = input("Enter the wine name:")
        bottles = float(input("Enter number of bottles of this wine (limit 3):"))
        while bottles > 3:
            bottles = float(input("Enter number of bottles of this wine (limit 3):"))
        Wine = Bottles.WineAB(name,bottles)
        print("Wine:",Wine.getnameAB())
        print("Amount Ordered", bottles)
        print("Price Per Bottle", Wine.getPriceAB(name))
        print("Subtotal:", Wine.subtotalAB())
        print("---------------")
        wine.append(Wine)



    #for x in wine:
        #print(x)


    print(Wine) # should print the total cost using str method but my set price function is not working ;/
mainAB()
