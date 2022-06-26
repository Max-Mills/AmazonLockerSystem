###This is for testing the Code###
from Locker import Locker
from Store import Store
from Item import Item
from LockerStatus import LockerStatus
from Sizes import Sizes
from GeoLocation import GeoLocation
from AmazonLocation import AmazonLocation
from LocationTiming import LocationTiming
from Warehouse import Warehouse

size = Sizes
item = Item("a","toy",20.00, size.m)
lockerStatus = LockerStatus
geoLocation = GeoLocation(2,4)
locationTiming = LocationTiming([[7,12]], [[7,18]], [[6,12]], [[5,7]], [], [[15,18]], [], ["2022-06-26"])
amazonLocation = AmazonLocation("asildnn", geoLocation, locationTiming)
warehouse = Warehouse(amazonLocation)
warehouse.addItem(item.getItemId())

locker1 = Locker("1", size.s,lockerStatus.Available, "1112")
locker2 = Locker("2", size.m,lockerStatus.Open, "1112")
locker3 = Locker("3", size.m,lockerStatus.Available, "1112")
lockers = []

lockers.append(locker1)
lockers.append(locker2)

store = Store(amazonLocation, lockers)
store.addLocker(locker3)
store.findOpenLocker(item.getItemSize())
store.removeLocker("3")
store.findOpenLocker(item.getItemSize())
locker2.changeLockerStatus(lockerStatus.Available)
locker = store.findOpenLocker(item.getItemSize())
warehouse.shipItem(item.getItemId())
locker.addItem(item)
warehouse.shipItem(item.getItemId())

