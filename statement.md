# Project Statement

## Project Title
**Movie Ticket Booking System**

## Problem Statement

Booking movie tickets manually can make seat management, billing, and booking records difficult to handle. This project provides a simple Python-based command-line system for managing movie ticket bookings.

## Objectives

- Display available movies and ticket prices.
- Display available show timings.
- Manage 48 seats for every movie/show combination.
- Allow customers to select multiple seats.
- Prevent duplicate or already booked seat selection.
- Calculate ticket price and 5% GST.
- Generate a unique booking ID.
- View existing booking details.
- Cancel a booking and restore its seats.
- Display all active bookings.

## Main Modules

### `main.py`
Contains the main application flow, booking, cancellation, booking lookup, seat availability, and main menu.

### `menu_data.py`
Stores movie names, ticket prices, show timings, seat rows, and GST configuration.

### `menu_display.py`
Handles movie/show display and validates movie/show choices.

### `order_processing.py`
Handles customer details, seat creation, seat selection, seat display, and bill calculation.

### `billing_and_payment.py`
Formats and displays the booking bill.

## Data Structures

- Dictionaries for movies, show timings, seats, and bookings.
- Lists for rows, seats, and selected seats.
- Tuples for movie name and price.
- Strings for booking IDs, names, phone numbers, and seat numbers.

## Billing

```text
Subtotal = Ticket Price × Number of Tickets
GST      = Subtotal × 5%
Total    = Subtotal + GST
```

## Seat Capacity

There are 6 rows:

`A, B, C, D, E, F`

Each row contains 8 seats.

```text
6 × 8 = 48 seats per show
```

## Conclusion

The project demonstrates practical use of Python functions, dictionaries, lists, loops, validation, conditional statements, and modular programming to build a movie ticket booking application.
