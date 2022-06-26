from AmazonLocation import AmazonLocation

class ItemWarehouse:

	def __init__(self, itemId: str, quantity: int = 0):
		self.__itemId = itemId
		self.__quantity = quantity

	def getID(self):
		return self.__itemId

	def getQuantity(self):
		return self.__quantity

	def addQuantity(self, number: int):
		self.__quantity += number

	def removeQuantity(self, number: int):
		self.__quantity -= number

class Warehouse:

	def __init__(self, location: AmazonLocation, items: list = []):
		self.__location = location
		self.__items = items

	def addItem (self, itemID: str, quantity: int = 1):
		index = self.findItem(itemID)
		if index == None:
			self.__items.append(ItemWarehouse(itemID))
			index = -1
		self.__items[index].addQuantity(quantity)
		
	def findItem(self, itemID: str):
		index = 0
		for item in self.__items:
			if item.getID() == itemID:
				return index
			index += 1
			return None

	def changeLocation(self, location: AmazonLocation):		
		self.__location = location

	def shipItem(self, itemID: str, quantity: int = 1) -> bool:
		'''Returns True if item was shipped, False if the Warehouse did not have the item'''
		index = self.findItem(itemID)
		if index != None and self.__items[index].getQuantity() >= quantity:
				self.__items[index].removeQuantity(quantity)
				return True
		print("Not enough items to ship to store")
		return False

	def getLocation(self) -> AmazonLocation:
		return self.__location



