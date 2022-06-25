# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

from Amazon import Amazon
from Customer import Customer

class AmazonLocker:

    def __init__(self):
        self.myAmazon = Amazon()

    # Clears the screen
    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def addCustomer(self):
        instructions = "Enter requested info or press ENTER to exit"
        while True:
            # Show Title
            print(instructions)

            name = input("Name: ")
            if name == '':
                break
            #! Need to change this part
            xGeoLocation = input("Location coordinate x: ")
            if xGeoLocation == '':
                break
            yGeoLocation = input("Location coordinate y: ")
            if yGeoLocation == '':
                break
            money = input("How much money do you have: $")
            if money == '':
                break
            
            id = self.myAmazon.getNumberOfCustomers()
            
            # Add client to the dictionary
            newCustomer = Customer(id, name, "test", money)
            self.myAmazon.addCustomer(id, newCustomer)
            #!Fix?
            print("\n Record added : [", id, "] = {Name:", name , ", $", money, "}\n")
            sleep(2)
            break
       

    def main_menu(self):
        # Main code
        while True:
            print("Menu\n")
            print("  1. Add a customer")
            print("  2. View customers")
            print("  9. Exit \n\n")
            selection = input("Enter selection: ")
            if selection == "1":
                self.addCustomer()
            #elif (selection == "2"):
                #self.addSubjects()
            elif (selection == "9"):
                exit()
            else:
                print("Invalid selection.")
                sleep(2)

def main():
    amazonTest = AmazonLocker()
    amazonTest.main_menu()


if __name__ == "__main__":
    main()