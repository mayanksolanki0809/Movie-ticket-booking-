from order_processing import calculate_bill


def print_bill(booking):
    """Print the final booking bill."""
    print("====================BOOKING SUCCESSFUL====================")

    print(f"Booking ID : {booking['booking_id']}")
    print(f"Customer   : {booking['name']}")
    print(f"Mobile     : {booking['phone']}")
    print(f"Movie      : {booking['movie']}")
    print(f"Show Time  : {booking['show']}")
    print(f"Seats      : {', '.join(booking['seats'])}")
    print(f"Tickets    : {booking['quantity']}")
    print(f"Subtotal   : Rs. {booking['subtotal']:.2f}")
    print(f"GST (5%)   : Rs. {booking['gst']:.2f}")
    print(f"Total      : Rs. {booking['total']:.2f}")

    print("=" * 70)


def get_bill(price, quantity):
    """Return subtotal, GST and total."""
    return calculate_bill(price, quantity)
