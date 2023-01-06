
class package:
    def __init__(self, name):
        self.name = name
    def dropOff(self, driver):
        print(f"Dilivered {self.name} by {driver} with number")

class AmazonTruck:
    packages = []
    driver = "nobody"

    def load(self, package):
        self.packages.append(package)   # add the package to the truck

    def deliver(self):
        for package in self.packages:
            package.dropOff(self.driver)

xbox = package("xbox")
tshirt = package("tshirt")
blades = package("rollerblades")

truck= AmazonTruck()
truck.driver = "Joe"
truck.load(xbox)
truck.load(tshirt)
truck.load(blades)

truck.deliver()
