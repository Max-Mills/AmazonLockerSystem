from Locker import Locker
from AmazonLocation import AmazonLocation
from datetime import datetime

class Store:

	def __init__(self, location: AmazonLocation, lockers: list):
		self.__location = location
		self.__lockers = lockers

	def isOpen(self, day = datetime.today().strftime('%A')) -> bool:
		today = datetime.today()
		date = str(today.date())
		hour = today.hour
		times = self.__location.getLocationTiming().getOpenTimes()
		for closedDate in times["Dates Closed"]:
			if closedDate == date:
				return False
		for timeRanges in times[day]:
			if hour in range(timeRanges[0],timeRanges[1],1):
				return True
		return False

	def changeLocation(self, location: AmazonLocation):		self.__location = location
	
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

	def getLocation(self) -> AmazonLocation:
		return self.__location

	def findOpenLocker(self, size: str):
		for locker in self.__lockers:
			if locker.getLockerStatus() == 0 and locker.getLockerSize() == size:
				print("Locker " + locker.getLockerID() + " is available for the item")
				break



