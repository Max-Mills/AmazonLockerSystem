class LocationTiming:
	def __init__(self, mondayTimes: list, tuesdayTimes: list, wednesdayTimes: list, thursdayTimes: list, fridayTimes: list, saturdayTimes: list, sundayTimes: list, datesClosed: list):
		self.__mondayTimes = mondayTimes
		self.__tuesdayTimes = tuesdayTimes
		self.__wedensdayTimes = wednesdayTimes
		self.__thursdayTimes = thursdayTimes
		self.__fridayTimes = fridayTimes
		self.__saturdayTimes = saturdayTimes
		self.__sundayTimes = sundayTimes
		self.__datesClosed = datesClosed

	def setMondayTimes(self, mTimes: list):
		self.__mondayTimes = mTimes

	def setTuesdayTimes(self, tuTimes: list):
		self.__mondayTimes = tuTimes

	def setWednesdayTimes(self, wTimes: list):
		self.__wedensdayTimes = wTimes

	def setThursdayTimes(self, thTimes: list):
		self.__thursdayTimes = thTimes

	def setFridayTimes(self, fTimes: list):
		self.__fridayTimes = fTimes
	
	def setSaturdayTimes(self, saTimes: list):
		self.__saturdayTimes = saTimes

	def setSundayTimes(self, suTimes: list):
		self.__sundayTimes = suTimes
	
	def setDatesClosed(self, dClosed: list):
		self.__datesClosed = dClosed

	def getOpenTimes(self) -> dict:
		return {"Monday": self.__mondayTimes, "Tuesday": self.__tuesdayTimes, "Wednesday": self.__wedensdayTimes, "Thursday": self.__thursdayTimes, "Friday": self.__fridayTimes, "Saturday": self.__saturdayTimes, "Sunday": self.__sundayTimes, "Dates Closed": self.__datesClosed}