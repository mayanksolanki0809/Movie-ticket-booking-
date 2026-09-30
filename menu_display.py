from menu_data import MOVIES, SHOW_TIMES


def display_movies():
    """Display all available movies."""
    print("====================MOVIES====================")

    for movie_id, movie_data in MOVIES.items():
        name = movie_data[0]
        price = movie_data[1]
        print(f"{movie_id}. {name:<25} Ticket Price: Rs. {price}")


def display_show_times():
    """Display all available show timings."""
    print("=====================SHOW TIMINGS=====================")

    for show_id, time in SHOW_TIMES.items():
        print(f"{show_id}. {time}")


def get_movie_choice():
    """Take valid movie choice from user."""
    while True:
        display_movies()

        try:
            choice = int(input("Enter movie number: "))

            if choice in MOVIES:
                return choice

            print("Invalid movie number!")

        except ValueError:
            print("Please enter a valid number.")


def get_show_choice():
    """Take valid show timing choice."""
    while True:
        display_show_times()

        try:
            choice = int(input("Enter show number: "))

            if choice in SHOW_TIMES:
                return choice

            print("Invalid show number!")

        except ValueError:
            print("Please enter a valid number.")
