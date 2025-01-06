class Phone():
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.charging = False
        self.out_of_battery = True
        self.broken = False

    def battery(self,charging):
        if charging == "y":
            self.out_of_battery = True
        else:
            self.out_of_battery = False
    def charge(self,charging):
        if charging == "y":
            self.charging = True
        else:
            self.charging = False
    def brk(self, brk):
        if brk == "y":
            self.broken = True
        else:
            self.broken = False
    
    def display(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.out_of_battery)
        print(self.broken)
        print(self.charging)


def main():
    tel = Phone("samsung", "A54", "2024")
    tel.brk("n")
    tel.charge("y")
    tel.battery("n")
    tel.display()


main()