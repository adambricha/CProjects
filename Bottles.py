# Adam Bricha U9233-5585
#Programming exam 3

#This program defines class wine and gives it different methods that can be used in the driver program
#The methods set the price of the wine bottles, calculate the subtotals,  and calculates the total cost of the purchases
#There is also getter methods which retrive the price, number of bottles, abd name of the wine



class WineAB:
    __totalCost = 0.0
    def __init__(self,name,numBottles):
        self.__name = name
        self.__numBottles = numBottles
        self.__pricePerBottle = 0
        self.__setPriceAB(name)


    def getnameAB(self):
        return self.__name


    def getbottlesAB(self):
        return self.__numBottles


    def __setPriceAB(self,name):
        name = self.__name.lower()
        if name == "DLM Grand Cru":
            self.__pricePerBottle = 39605.00
        elif name == "HJC Parantoux":
            self.__pricePerBottle = 18364.00
        elif name == "EMS Riesling":
            self.__pricePerBottle = 16776.00
        elif name == "HJE Grand Cru":
            self.__pricePerBottle = 9120.00
        elif name == "JS Terrantez":
            self.__pricePerBottle = 7514.00
        elif name == "Screaming Eagle Sauvignon Blanc":
            self.__pricePerBottle = 6373.00
        elif name == "JJPW Riesling":
            self.__pricePerBottle = 5280.00
        elif name == "HMB 'T' Vintage":
            self.__pricePerBottle = 4900.00
        elif name == "Screaming Eagle Cabernet Sauvignon":
            self.__pricePerBottle = 4518.00
        else:
            self.__pricePerBottle = 0

    def getPriceAB(self,name):
        return self.__pricePerBottle

    def CalcCostAB(self):
        cost = self.__pricePerBottle * self.__numBottles
        WineAB.__totalCost += cost
        return cost

    def getTotalCostAB(self):
        return WineAB.__totalCost

    def subtotalAB(self):
        subtotal = self.__pricePerBottle * self.__numBottles
        return subtotal


    def __str__(self):
        return "The total cost of all your purchases is".format(self.getTotalCostAB())


    dictionaryAB = {"DLM Grand Cru":39605.00,"HJC Parantoux":18364.00,"EMS Riesling": 16776.00,"HJE Grand Cru": 9120.00,"JS Terrantez":7514.00,"Screaming Eagle Sauvignon Blanc":6373.00,"JJPW Riesling":5280.00,"HMB 'T' Vintage":4900.00,"Screaming Eagle Cabernet Sauvignon":4518.00}




