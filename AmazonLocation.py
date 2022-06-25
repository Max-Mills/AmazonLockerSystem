from GeoLocation import GeoLocation
from LocationTiming import LocationTiming

class AmazonLocation:

	def __init__(self, locationID: str, geoLocation: GeoLocation, locationTiming: LocationTiming):
		self.__locationID = locationID
		self.__geoLocation = geoLocation
		self.__locationTiming = locationTiming

	def setLocationID(self, id: str): 
		self.__locationID = id
	
	def setGeolocation(self, gLocation: GeoLocation):
		self.__geoLocation = gLocation
	
	def setLocationTiming(self, lTiming: LocationTiming):
		self.__locationTiming = lTiming

	def getLocationID(self) -> str:
		return self.__locationID

	def getGeoLocation(self) -> GeoLocation:
		return self.__geoLocation

	def getLocationTiming(self) -> LocationTiming:
		return self.__locationTiming