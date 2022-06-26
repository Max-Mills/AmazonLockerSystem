from LockerStatus import LockerStatus
from Sizes import Sizes
from Item import Item

class Locker:

	def __init__(self, id: str, size: Sizes, status: LockerStatus, code: str, item: Item = None):
		self.__id = id
		self.__size = size
		self.__status = status
		self.__code = code
		self.__item = item

	##Locker ID and Size will never change##

	def addItem(self, item: Item) -> bool:
		'''Returns true if added, returns false if locker was already in use'''
		if self.__item == None:
			self.__item = item
			return True
		return False

	def removeItem(self) -> bool:
		'''Returns true if remove, false if locker was already empty'''
		if self.__item != None:
			self.__item = None
			return True
		return False

	def changeLockerStatus(self, status: LockerStatus):
		self.__status = status

	def changeLockerCode(self, code: str):
		self.__code = code

	def getItem(self) -> Item:
		return self.__item

	def getLockerID(self) -> str:
		return self.__id
	
	def getLockerSize(self) -> Sizes:
		return self.__size
	
	def getLockerStatus(self) -> LockerStatus:
		return self.__status.value

	def getLockerCode(self):
		return self.__code
	
	def isCodeValid(self, code: str):
		if self.__code == code:
			print("match")
		else:
			print("not match")