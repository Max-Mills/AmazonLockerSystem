from LockerStatus import LockerStatus

class Locker:

	def setLockerID(self, id):
		self.__id = id

	def setLockerSize(self, size):
		self.__lockerSize = size

	def setLockerStatus(self, status):
		self.__lockerStatus = status

	def setLockerCode(self, code):
		self.__code = code

	def getLockerID(self):
		return self.__id
	
	def getLockerSize(self):
		return self.__lockerSize
	
	def getLockerStatus(self) -> LockerStatus:
		return self.__lockerStatus

	def getLockerCode(self):
		return self.__code
	
	def isCodeValid(self, code):
		if self.__code == code:
			print("match")
		else:
			print("not match")