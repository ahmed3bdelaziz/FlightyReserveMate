import sqlite3
from tkinter import messagebox

DATABASE_NAME = "flights.db"

def create_table():
    """
    Creates the 'reservations' table if it doesn't already exist.
    This ensures the database structure is ready on application startup.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                flight_number TEXT NOT NULL,
                departure TEXT NOT NULL,
                destination TEXT NOT NULL,
                date TEXT NOT NULL,
                seat_number TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to create table: {e}")
    finally:
        if conn:
            conn.close()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    """
    Inserts a new reservation record into the database.

    Args:
        name (str): Passenger's name.
        flight_number (str): Flight number.
        departure (str): Departure location.
        destination (str): Destination location.
        date (str): Date of the flight.
        seat_number (str): Seat number.

    Returns:
        bool: True if reservation added successfully, False otherwise.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, flight_number, departure, destination, date, seat_number))
        conn.commit()
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to add reservation: {e}")
        return False
    finally:
        if conn:
            conn.close()

def get_all_reservations():
    """
    Retrieves all reservation records from the database.

    Returns:
        list: A list of tuples, where each tuple represents a reservation.
              Returns an empty list if an error occurs.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reservations')
        reservations = cursor.fetchall()
        return reservations
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to retrieve reservations: {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_reservation_by_id(reservation_id):
    """
    Retrieves a single reservation record by its ID.

    Args:
        reservation_id (int): The ID of the reservation to retrieve.

    Returns:
        tuple: A tuple representing the reservation, or None if not found or an error occurs.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reservations WHERE id = ?', (reservation_id,))
        reservation = cursor.fetchone()
        return reservation
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to get reservation: {e}")
        return None
    finally:
        if conn:
            conn.close()


def update_reservation(reservation_id, name, flight_number, departure, destination, date, seat_number):
    """
    Updates an existing reservation record in the database.

    Args:
        reservation_id (int): The ID of the reservation to update.
        name (str): New passenger name.
        flight_number (str): New flight number.
        departure (str): New departure location.
        destination (str): New destination location.
        date (str): New flight date.
        seat_number (str): New seat number.

    Returns:
        bool: True if reservation updated successfully, False otherwise.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE reservations
            SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
            WHERE id = ?
        ''', (name, flight_number, departure, destination, date, seat_number, reservation_id))
        conn.commit()
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to update reservation: {e}")
        return False
    finally:
        if conn:
            conn.close()

def delete_reservation(reservation_id):
    """
    Deletes a reservation record from the database by its ID.

    Args:
        reservation_id (int): The ID of the reservation to delete.

    Returns:
        bool: True if reservation deleted successfully, False otherwise.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Failed to delete reservation: {e}")
        return False
    finally:
        if conn:
            conn.close()

# This ensures the database table is created when the script is imported or run directly.
create_table()