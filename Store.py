from Locker import Locker
from AmazonLocation import AmazonLocation
from datetime import datetime

class Store:

	def __init__(self, location: AmazonLocation, lockers: list):
		self.__location = location
		self.__lockers = lockers

	def isOpen(self, today: datetime = datetime.today()) -> bool:
		day = today.strftime('%A')
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

	def changeLocation(self, location: AmazonLocation):		
		self.__location = location
	
	def addLocker(self, locker: Locker):
		self.__lockers.append(locker)

	def findLocker(self, id: str) -> int:
		i = 0
		for locker in self.__lockers:
			if locker.getLockerID() == id:
				return i
			i += 1
		print("Locker not found")
		return None

##doesn't seem needed
	#def updateLocker(self, locker: Locker):
		#index: int = self.findLocker(locker.getLockerID())
		#if index != None:
		#	self.__lockers[index] = locker			

	def removeLocker(self, id: str):
		index: int = self.findLocker(id)
		if index != None:
			del self.__lockers[index]

	def getLockers(self) -> list:
		return self.__lockers

	def getLocation(self) -> AmazonLocation:
		return self.__location

	def findOpenLocker(self, size: str) -> Locker:
		for locker in self.__lockers:
			if locker.getLockerStatus() == 0 and locker.getLockerSize() == size:
				return locker


