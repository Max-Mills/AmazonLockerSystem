class Store:

	def setLockers(self, lockers):
		self.__lockers = lockers

	def getLockers(self):
		return self.__lockers

	def findOpenLocker(self, item):
		for locker in self.__lockers:
			if locker.getLockerStatus() == 0 and locker.getLockerSize() == item.getItemSize():
				print("Locker " + locker.getLockerID() + " is available for the item")
				break



