from enum import Enum

class LockerStatus(Enum):
	Open = -1
	Available = 0
	Reserved = 1
	OccupiedFirstDay = 2
	OccupiedSecondDay = 3
	OccupiedThirdDay = 4

