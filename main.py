from menu_data import MOVIES, SHOW_TIMES, ROWS, SEATS_PER_ROW
from menu_display import display_movies, display_show_times, get_movie_choice, get_show_choice
from order_processing import (
    create_show_key,
    initialize_seats,
    display_seats,
    select_seats,
    get_customer_details,
    calculate_bill,
)
from billing_and_payment import print_bill


# Available seats for every movie/show.
# The original project used the name booked_seats, but it actually stores
# the seats that are still available.
booked_seats = {}

# All booking records.
bookings = {}

booking_counter = 1000


def book_ticket():
    """Book a movie ticket."""
    global booking_counter

    print("==================BOOK TICKET=====================")

    name, phone = get_customer_details()
    movie_id = get_movie_choice()
    show_id = get_show_choice()

    movie_name = MOVIES[movie_id][0]
    price = MOVIES[movie_id][1]
    show_time = SHOW_TIMES[show_id]

    while True:
        try:
            quantity = int(input("\nEnter number of tickets (1-8): "))

            if 1 <= quantity <= 8:
                break

            print("Please select between 1 and 8 tickets.")

        except ValueError:
            print("Please enter a valid number.")

    initialize_seats(movie_id, show_id, booked_seats)

    # Prevent a request larger than the number of remaining seats.
    key = create_show_key(movie_id, show_id)
    if quantity > len(booked_seats[key]):
        print("Not enough seats are available for this show.")
        return

    selected_seats = select_seats(
        movie_id,
        show_id,
        quantity,
        booked_seats
    )

    subtotal, gst, total = calculate_bill(price, quantity)

    booking_counter += 1
    booking_id = "BK" + str(booking_counter)

    # Remove selected seats from the available-seat list.
    for seat in selected_seats:
        booked_seats[key].remove(seat)

    booking = {
        "booking_id": booking_id,
        "name": name,
        "phone": phone,
        "movie": movie_name,
        "movie_id": movie_id,
        "show": show_time,
        "show_id": show_id,
        "seats": selected_seats,
        "quantity": quantity,
        "price": price,
        "subtotal": subtotal,
        "gst": gst,
        "total": total
    }

    bookings[booking_id] = booking
    print_bill(booking)


def view_booking():
    """View a booking by booking ID."""
    print("VIEW BOOKING")

    if not bookings:
        print("No bookings found.")
        return

    booking_id = input("Enter Booking ID: ").upper().strip()

    if booking_id not in bookings:
        print("Booking ID not found.")
        return

    booking = bookings[booking_id]

    print("\n" + "-" * 70)
    print(f"Booking ID : {booking_id}")
    print(f"Customer   : {booking['name']}")
    print(f"Mobile     : {booking['phone']}")
    print(f"Movie      : {booking['movie']}")
    print(f"Show Time  : {booking['show']}")
    print(f"Seats      : {', '.join(booking['seats'])}")
    print(f"Tickets    : {booking['quantity']}")
    print(f"Total      : Rs. {booking['total']:.2f}")
    print("-" * 70)


def cancel_booking():
    """Cancel a booking and return its seats to availability."""
    print("====================CANCEL BOOKING====================")

    if not bookings:
        print("No bookings available.")
        return

    booking_id = input(
        "Enter Booking ID to cancel: "
    ).upper().strip()

    if booking_id not in bookings:
        print("Booking ID not found.")
        return

    booking = bookings[booking_id]

    print("\nBooking Details:")
    print(f"Customer : {booking['name']}")
    print(f"Movie    : {booking['movie']}")
    print(f"Show     : {booking['show']}")
    print(f"Seats    : {', '.join(booking['seats'])}")
    print(f"Amount   : Rs. {booking['total']:.2f}")

    confirm = input(
        "Are you sure you want to cancel? (Y/N): "
    ).upper().strip()

    if confirm == "Y":
        key = create_show_key(
            booking["movie_id"],
            booking["show_id"]
        )

        for seat in booking["seats"]:
            if seat not in booked_seats[key]:
                booked_seats[key].append(seat)

        del bookings[booking_id]

        print("\nBooking cancelled successfully.")
        print("Your seats are now available again.")

    else:
        print("\nCancellation stopped.")


def display_all_bookings():
    """Display every active booking."""
    print("====================ALL BOOKINGS====================")

    if not bookings:
        print("No bookings available.")
        return

    for booking_id, booking in bookings.items():
        print("\n" + "-" * 70)
        print(f"Booking ID : {booking_id}")
        print(f"Customer   : {booking['name']}")
        print(f"Movie      : {booking['movie']}")
        print(f"Show       : {booking['show']}")
        print(f"Seats      : {', '.join(booking['seats'])}")
        print(f"Tickets    : {booking['quantity']}")
        print(f"Amount     : Rs. {booking['total']:.2f}")

    print("-" * 70)


def check_seat_availability():
    """Display seat counts and the seat map."""
    print("====================SEAT AVAILABILITY====================")

    movie_id = get_movie_choice()
    show_id = get_show_choice()

    initialize_seats(movie_id, show_id, booked_seats)

    key = create_show_key(movie_id, show_id)

    available = len(booked_seats[key])
    total_seats = len(ROWS) * SEATS_PER_ROW
    booked = total_seats - available

    print("Movie:", MOVIES[movie_id][0])
    print("Show :", SHOW_TIMES[show_id])

    print(f"Total Seats     : {total_seats}")
    print(f"Booked Seats    : {booked}")
    print(f"Available Seats : {available}")

    display_seats(movie_id, show_id, booked_seats)


def main_menu():
    """Run the main application menu."""
    while True:
        print("====================MAIN MENU====================")
        print("1. Display Movies")
        print("2. Display Show Timings")
        print("3. Check Seat Availability")
        print("4. Book Movie Ticket")
        print("5. View Booking")
        print("6. Cancel Booking")
        print("7. Display All Bookings")
        print("8. Exit")
        print("=" * 70)

        choice = input(
            "Enter your choice (1-8): "
        ).strip()

        if choice == "1":
            display_movies()

        elif choice == "2":
            display_show_times()

        elif choice == "3":
            check_seat_availability()

        elif choice == "4":
            book_ticket()

        elif choice == "5":
            view_booking()

        elif choice == "6":
            cancel_booking()

        elif choice == "7":
            display_all_bookings()

        elif choice == "8":
            print("THANK YOU FOR USING MOVIE TICKET BOOKING SYSTEM")
            break

        else:
            print("Invalid choice!")
            print("Please select a number between 1 and 8.")


if __name__ == "__main__":
    main_menu()
