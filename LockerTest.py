###This is for testing the Code###

from Locker import Locker
from Store import Store
from Item import Item
from LockerStatus import LockerStatus
from Sizes import Sizes

size = Sizes
item = Item("a","toy",20.00, size.m)
lockerStatus = LockerStatus
locker1 = Locker("1", size.s,lockerStatus.Available, "1112")
locker2 = Locker("2", size.m,lockerStatus.Open, "1112")
locker3 = Locker("3", size.m,lockerStatus.Available, "1112")
lockers = []

lockers.append(locker1)
lockers.append(locker2)

store = Store(lockers)
store.addLocker(locker3)
store.findOpenLocker(item)
store.removeLocker("3")
store.findOpenLocker(item)
locker2.changeLockerStatus(lockerStatus.Available)
store.findOpenLocker(item)

