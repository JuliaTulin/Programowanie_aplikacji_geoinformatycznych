# Zadanie 1: Obsługa rezerwacji miejsc w kinie

class ReservationError(Exception):
    pass

class NoSeatsAvailableError(ReservationError):
    pass

class SeatAlreadyReservedError(ReservationError):
    pass

class UserAlreadyHasReservationError(ReservationError):
    pass

class InvalidCancellationDataError(ReservationError):
    pass

class CinemaHall:
    def __init__(self, rows, cols):
        self.seats = {(chr(65 + r) + str(c + 1)): None for r in range(rows) for c in range(cols)}
        self.user_reservations = {}

# funkcja odpowiadająca za rezerwację miejsc
    def reserve_seat(self, seat, user):
        if all(self.seats.values()):
            raise NoSeatsAvailableError("No seats available.")
        
        if self.seats[seat] is not None:
            raise SeatAlreadyReservedError(f"Seat {seat} is already reserved.")
        
        if user in self.user_reservations:
            raise UserAlreadyHasReservationError(f"You already have a reservation.")
        
        self.seats[seat] = user
        self.user_reservations[user] = seat
        print(f"Seat {seat} reserved for {user}.")

# funkcja odpowiadająca za anulowanie rezerwacji
    def cancel_reservation(self, seat, user):
        if self.seats[seat] != user:
            raise InvalidCancellationDataError("Seat and user information do not match.")
        
        self.seats[seat] = None
        del self.user_reservations[user]
        print(f"Reservation for seat {seat} by {user} has been cancelled.")

# funkcja odpowiadająca za wyświetlenie aktualnych rezerwacji
    def show_reservations(self):
        if not self.user_reservations:
            print("No current reservations.")
        else:
            for seat, user in self.seats.items():
                if user is not None:
                    print(f"Seat {seat} is reserved by {user}.")


cinema_hall = CinemaHall(5, 5)

# mozliwość rezerwacji anulacji i sprawdzenia wszystkich aktualnych rezerwacji
while True:
    action = input("Would you like to 'reserve' a seat, 'cancel' a reservation, or 'show' current reservations? (enter 'exit' to quit): ").strip().lower()
    if action == 'exit':
        break

    if action not in ['reserve', 'cancel', 'show']:
        print("Invalid action. Please enter 'reserve', 'cancel', or 'show'.")
        continue

    if action == 'show':
        cinema_hall.show_reservations()
        continue

    user = input("Enter your name: ").strip()
    seat = input("Enter seat (e.g., A1): ").strip().upper()

    try:
        if action == 'reserve':
            cinema_hall.reserve_seat(seat, user)
        elif action == 'cancel':
            cinema_hall.cancel_reservation(seat, user)
    except ReservationError as e:
        print(e)
