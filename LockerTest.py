from Locker import Locker
from Store import Store
from Item import Item
from LockerStatus import LockerStatus

locker1 = Locker()
locker2 = Locker()
store = Store()
item = Item()
lockerStatus = LockerStatus
lockers = []

locker1.setLockerID("1234")
locker1.setLockerSize("Small")
locker1.setLockerStatus(lockerStatus.Open)

lockers.append(locker1)

locker2.setLockerID("4321")
locker2.setLockerSize("Small")
locker2.setLockerStatus(lockerStatus.Available)

item.setItemName("toy")
item.setItemSize("Small")

lockers.append(locker2)

store.setLockers(lockers)

store.findOpenLocker(item)

