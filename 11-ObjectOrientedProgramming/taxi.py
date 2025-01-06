class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(self.distance)
        print(self.rate_per_km)
        print(self.fare)


def main():
    # your program
    taxi1 = TaxiRide(rate_per_km=2)
    taxi1.calculate_fare(distance=50)
    taxi1.print_receipt()


    taxi2 = TaxiRide(rate_per_km=2)
    taxi2.calculate_fare(distance=60)
    taxi2.print_receipt()

if __name__ == "__main__":
    main()
