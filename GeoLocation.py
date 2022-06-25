class GeoLocation:

	def __init__(self, x:int, y:int):
		self.__x = x
		self.__y = y

	def setXandY(self, xGeolocation: int, yGeolocation: int):
		self.__x = xGeolocation
		self.__y = yGeolocation

	def getXandY(self) -> int:
		return self.__x,self.__y
	

