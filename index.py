from abc import ABC

class Abstract_Bus(ABC):
    def __init__(self, coach, driver, arrival, departure, from_des, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seats = ['Empty' for i in range(20)]


class Bus(Abstract_Bus):
    pass

class BusCompany:
    def __init__(self):
        self.buses = {} # shokol bus er details thakbe {'coach':bus er object}

    def install_bus(self, bus):
        print(f'Bus {bus.coach} Added successfully!!')
        self.buses[bus.coach] = bus

    def display_available_bus(self):
        if not self.buses:
            print("Bus is not available!!")
        else:
            print(f'Coach\tDiver\tArrival\tDeparture\tFrom_des\tTo')
            for coach, bus in self.buses.items():
                print(f'{coach}\t{bus.driver}\t{bus.arrival}\t{bus.departure}\t{bus.from_des}\t{bus.to}')
    
    def book_ticket(self, coach, seat):
        if coach in self.buses:
            if 1<=seat<=20:
                if self.buses[coach].seats[seat-1] == 'Empty':
                    print("Seat booked Successfully")
                    self.buses[coach].seats[seat-1] = 'booked'
                else:
                    print('Seat already Booked!!')
            else:
                print("Invalid seat Number!!")
        else:
            print("Invalid Coach number!!")

    def display_seat_status(self, coach):
        if coach in self.buses:
            print(self.buses[coach].seats)

ena = BusCompany()

while True:
    print('Welcome to Bus Ticket Booking System')
    print('\t1. Install Bus')
    print('\t2. View Available Buses')
    print('\t3. Book Ticked')
    print('\t4. Check seats status')
    print('\t5. Exit')
    choice = int(input("Enter Your choice : "))

    if choice == 1:
        coach = int(input("\tEnter Bus Number : "))
        driver = input("\tEnter Bus Driver Name : ")
        arrival = input("\tEnter Arrival Time : ")
        departure = input("\tEnter Departure Time : ")
        from_des = input("\tEnter From Destination : ")
        to = input("\tEnter To Destination : ")

        bus = Bus(coach, driver, arrival, departure, from_des, to)
        ena.install_bus(bus)
    elif choice == 2:
        ena.display_available_bus()
    elif choice == 3:
        coach = int(input("\tEnter Bus number : "))
        seat = int(input("\tEnter Seat number : "))

        ena.book_ticket(coach, seat)
    elif choice == 4:
        coach = int(input("\tEnter Bus number : "))
        ena.display_seat_status(coach)
    elif choice == 5:
        break
    else:
        print("Invalid Number!!")