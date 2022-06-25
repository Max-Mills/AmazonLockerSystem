class Customer:
    
    # Init method that will construct objects (also known as the construtor method)
    def __init__(self, id, name, geoLocation, money):
        self.customerID = id      #instance variable
        self.__name = name
        self.__geoLocation = geoLocation 
        self.__orders = {}
        self.__money = money

    def setName(self, name):
        self.__name = name
    
    def setGeoLocation(self, geoLocation):
        self.__geoLocation = geoLocation
    

    def getGeoLocation(self):
        return self.__geoLocation
	
    #def addOrders(self, newOrder):
        #self.__orders.append(newOrder) 
    
    #def getAllOrders(self):
        #return self.__orders

    def setOrders(self, newOrder):
        self.__orders.append(newOrder) 
        
    def setMoney(self, money):
        self.__money = money 
    
    def getName(self):
        return self.__name

    def getGeoLocation(self):
        return self.__geoLocation

    def getOrders(self):
        return self.__orders

    def getMoney(self):
        return self.__money  