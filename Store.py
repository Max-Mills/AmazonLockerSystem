from Item import Item
from Locker import Locker

class Store:

	def __init__(self, lockers: list):
		self.__lockers = lockers

	def addLocker(self, locker: Locker):
		self.__lockers.append(locker)

	def removeLocker(self, id: str):
		i = 0
		for locker in self.__lockers:
			if locker.getLockerID() == id:
				self.__lockers.remove(locker)
				return
			i += i

	def getLockers(self) -> list:
		return self.__lockers

	def findOpenLocker(self, item: Item):
		for locker in self.__lockers:
			if locker.getLockerStatus() == 0 and locker.getLockerSize() == item.getItemSize():
				print("Locker " + locker.getLockerID() + " is available for the item")
				break



