from Sizes import Sizes

class Item:

	def __init__(self, id: str, name: str, price: int, size: Sizes):
		self.__id = id
		self.__name = name
		self.__price = price
		self.__size = size

	##Item ID should never change###

	def setItemName(self, name: str):
		self.__name = name

	def setItemPrice(self, price: int):
		self.__price == price

	def setItemSize(self, size: Sizes):
		self.__size = size

	def getItemId(self) -> str:
		return self.__id

	def getItemName(self) -> str:
		return self.__name

	def getItemPrice(self) -> int:
		return self.__price

	def getItemSize(self) -> Sizes:
		return self.__size