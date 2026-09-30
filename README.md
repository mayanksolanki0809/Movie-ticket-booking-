# Movie Ticket Booking System

A Python-based **Movie Ticket Booking System** that runs in the command line. The project allows users to view movies, select show timings, check seat availability, book tickets, view bookings, cancel bookings, and display all active bookings.

## Project Structure

```text
movie_ticket_booking/
│
├── README.md
├── billing_and_payment.py
├── main.py
├── menu_data.py
├── menu_display.py
├── order_processing.py
├── requirements.txt
└── statement.md
```

## Features

- Display movies and ticket prices
- Display show timings
- Manage 48 seats per movie/show
- Check seat availability
- Book 1–8 tickets at a time
- Select individual seats
- Prevent duplicate seat selection
- Prevent booking already unavailable seats
- Calculate subtotal
- Apply 5% GST
- Generate a unique booking ID
- View booking details
- Cancel bookings
- Restore cancelled seats
- Display all active bookings
- Validate user input

## Movies

| No. | Movie | Ticket Price |
|---:|---|---:|
| 1 | Interstellar | Rs. 180 |
| 2 | The Martian | Rs. 150 |
| 3 | Inception | Rs. 170 |
| 4 | Avengers: End Game | Rs. 200 |
| 5 | Brahmastra | Rs. 120 |

## Show Timings

1. 10:00 AM  
2. 01:00 PM  
3. 04:00 PM  
4. 07:00 PM  
5. 10:00 PM

## Seat Layout

There are 6 rows with 8 seats per row:

```text
A1 A2 A3 A4 A5 A6 A7 A8
B1 B2 B3 B4 B5 B6 B7 B8
C1 C2 C3 C4 C5 C6 C7 C8
D1 D2 D3 D4 D5 D6 D7 D8
E1 E2 E3 E4 E5 E6 E7 E8
F1 F2 F3 F4 F5 F6 F7 F8
```

Total capacity per show:

```text
6 × 8 = 48 seats
```

## Billing

```text
Subtotal = Ticket Price × Number of Tickets
GST      = Subtotal × 5%
Total    = Subtotal + GST
```

## Example

For 2 Interstellar tickets:

```text
Ticket Price = Rs. 180
Quantity     = 2

Subtotal     = Rs. 360.00
GST (5%)     = Rs. 18.00
Total        = Rs. 378.00
```

## How to Run

Make sure all Python files are in the same folder.

Run:

```bash
python main.py
```

## Modules

### `main.py`
Runs the main menu and coordinates the application.

### `menu_data.py`
Stores movies, prices, timings, rows, seats, and GST information.

### `menu_display.py`
Displays movies/show timings and validates selections.

### `order_processing.py`
Handles customer information, seats, and bill calculation.

### `billing_and_payment.py`
Displays the final booking bill.

### `requirements.txt`
Documents the Python requirement. No third-party package is needed.

### `statement.md`
Contains the formal project statement.

## Limitations

- Bookings are stored only in memory.
- Data is lost when the program exits.
- No database is used.
- No graphical user interface is included.
- Payment processing is not included because this version focuses on ticket booking.

## Future Enhancements

- Add SQLite/MySQL database storage.
- Add a graphical interface using Tkinter.
- Add real payment integration.
- Add movie search and filtering.
- Add booking history.
- Add administrator login.
- Generate PDF tickets/receipts.
- Add multiple cinema screens.

## License

This project is intended for educational and academic use.
