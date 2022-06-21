from sympy import Order


class Customer:
    
    # Init method that will construct objects (also known as the construtor method)
    def __init__(self, name, geoLocation, orders, money):
        self.customerID = None      #instance variable
        self.__name = name
        self.__geoLocation = geoLocation 
        self.__orders = None
        self.__money = money

    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setGeoLocation(self, geoLocation):
        self.__geoLocation = geoLocation
    
    def getGeoLocation(self):
        return self.__geoLocation
	
    def setOrders(self, newOrder):
        self.__orders.append(newOrder) 
    
    def getOrders(self):
        return self.__orders

        
    def setMoney(self, money):
        self.__money = money 
    
    def getMoney(self):
        return self.__money  