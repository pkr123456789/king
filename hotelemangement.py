class Hotel:
    def __init__(self, total_rooms):
        self.total_rooms = total_rooms
        self.rooms = [None] * total_rooms  # None means the room is empty

    def check_in(self, guest_name):
        for i in range(self.total_rooms):
            if self.rooms[i] is None:  # Room is empty
                self.rooms[i] = guest_name
                print(f"Checked in {guest_name} to room {i + 1}.")
                return
        print("No available rooms.")

    def check_out(self, room_number):
        if 1 <= room_number <= self.total_rooms and self.rooms[room_number - 1] is not None:
            guest_name = self.rooms[room_number - 1]
            self.rooms[room_number - 1] = None
            print(f"Checked out {guest_name} from room {room_number}.")
        else:
            print("Invalid room number or room is already empty.")

    def status(self):
        print("Current room status:")
        for i, guest in enumerate(self.rooms):
            if guest is None:
                print(f"Room {i + 1}: Empty")
            else:
                print(f"Room {i + 1}: Occupied by {guest}")

def main():
    hotel = Hotel(total_rooms=5)  # Initialize hotel with 5 rooms

    while True:
        print("\n1. Check In")
        print("2. Check Out")
        print("3. View Status")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter guest name: ")
            hotel.check_in(name)
        elif choice == '2':
            room_number = int(input("Enter room number to check out: "))
            hotel.check_out(room_number)
        elif choice == '3':
            hotel.status()
        elif choice == '4':
            print("Exiting the hotel management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
