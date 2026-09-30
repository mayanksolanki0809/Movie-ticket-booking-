from menu_data import MOVIES, SHOW_TIMES, ROWS, SEATS_PER_ROW


def create_show_key(movie_id, show_id):
    """Create a unique key for a movie and show."""
    return str(movie_id) + "-" + str(show_id)


def initialize_seats(movie_id, show_id, booked_seats):
    """Create seat information for a particular movie show."""
    key = create_show_key(movie_id, show_id)

    if key not in booked_seats:
        # This list contains currently AVAILABLE seats.
        booked_seats[key] = []

        for row in ROWS:
            for number in range(1, SEATS_PER_ROW + 1):
                booked_seats[key].append(row + str(number))


def display_seats(movie_id, show_id, booked_seats):
    """Display available and booked seats."""
    initialize_seats(movie_id, show_id, booked_seats)

    key = create_show_key(movie_id, show_id)
    available_seats = booked_seats[key]

    print("====================SEATS=====================")

    for row in ROWS:
        for number in range(1, SEATS_PER_ROW + 1):
            seat = row + str(number)

            if seat in available_seats:
                print(f"[{seat}]", end=" ")
            else:
                print("[XX]", end=" ")

        print()

    print("[XX] = Booked Seat")
    print("[A1] = Available Seat")


def select_seats(movie_id, show_id, quantity, booked_seats):
    """Allow customer to select available seats."""
    initialize_seats(movie_id, show_id, booked_seats)

    key = create_show_key(movie_id, show_id)
    selected_seats = []

    print("Select your seats.")
    display_seats(movie_id, show_id, booked_seats)

    valid_seats = []
    for row in ROWS:
        for number in range(1, SEATS_PER_ROW + 1):
            valid_seats.append(row + str(number))

    while len(selected_seats) < quantity:
        seat = input(
            f"Enter seat {len(selected_seats) + 1}: "
        ).upper().strip()

        if seat not in valid_seats:
            print("Invalid seat number!")
            continue

        if seat not in booked_seats[key]:
            print("This seat is already booked!")
            continue

        if seat in selected_seats:
            print("You already selected this seat!")
            continue

        selected_seats.append(seat)
        print(f"Seat {seat} selected successfully.")

    return selected_seats


def get_customer_details():
    """Collect customer information."""
    print("====================CUSTOMER DETAILS====================")

    while True:
        name = input("Enter customer name: ").strip()

        if name:
            break

        print("Name cannot be empty.")

    while True:
        phone = input("Enter mobile number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            break

        print("Please enter a valid 10-digit mobile number.")

    return name, phone


def calculate_bill(price, quantity):
    """Calculate ticket bill."""
    subtotal = price * quantity
    gst = subtotal * 0.05
    total = subtotal + gst
    return subtotal, gst, total


def add_booking(booking, bookings):
    """Store a booking using its booking ID."""
    bookings[booking["booking_id"]] = booking
