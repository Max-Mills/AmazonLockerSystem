from Customer import Customer

class Amazon:
    def __init__(self):
        self.__customers = {}
        self.__catalogItems = None
        self.__stores = None
        self.__werehouse = None

    def getNumberOfCustomers(self):
        return len(self.__customers)

    def addCustomer(self, id, customer):
        self.__customers[id] = customer
    
    def getCustomer(self, id):
        pass
        #! I need to return another object
       #print(self.__customers)

    def getAllCustomers(self):
        return self.__customers
    
    def addCatalogItem(self, item):
        self.__catalogItems.append(item) 
    
    def getAllCatalogItems(self):
        return self.__catalogItems
    
    def addStore(self, store):
        self.__stores.append(store) 
    
    def getAllStores(self):
        return self.__stores

    def addWarehouse(self, warehouse):
        self.__stores.append(warehouse) 
    
    def getAllWarehouses(self):
        return self.__warehouses