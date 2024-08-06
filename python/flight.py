class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if self.open_seats() == 0:
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Niladri", "Sagor", "Sazid", "Jubaer", "Nijhum"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to the flight successfully")
    else:
        print(f"No available seats for {person}")
