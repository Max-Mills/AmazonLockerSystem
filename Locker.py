from LockerStatus import LockerStatus
from Sizes import Sizes

class Locker:

	def __init__(self, id: str, size: Sizes, status: LockerStatus, code: str):
		self.__id = id
		self.__size = size
		self.__status = status
		self.__code = code

	##Locker ID and Size will never change##

	def changeLockerStatus(self, status: LockerStatus):
		self.__status = status

	def changeLockerCode(self, code: str):
		self.__code = code

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