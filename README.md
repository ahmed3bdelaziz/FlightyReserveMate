# FlightyReserveMate ✈️ - Simple Flight Reservation Desktop App

## Overview

FlightyReserveMate is a user-friendly desktop application designed for managing flight reservations. Built with Python and Tkinter for the graphical interface, and SQLite for data storage, it allows users to easily book new flights, view existing reservations, and update or delete them.

This project aims to demonstrate fundamental desktop application development concepts, including GUI design, database interaction (CRUD operations), and application packaging.

## Features

-   **Friendly UI:** Clean and intuitive interface built with Tkinter's `ttk` widgets.
-   **Book New Flight:** A dedicated form to create new reservations with passenger details, flight number, route, date, and seat.
-   **View All Reservations:** Displays all reservations in a clear, tabular format using a `ttk.Treeview`.
-   **Edit Reservations:** Select an existing reservation and modify its details via a pre-filled form.
-   **Delete Reservations:** Easily remove unwanted reservations with a confirmation prompt.
-   **Persistent Data:** All reservation data is stored locally in an SQLite database (`flights.db`).

## Project Structure


/flight_reservation_app_v2
├── main.py                 # Main application entry point and navigation manager
├── database.py             # Handles all SQLite database operations (CRUD)
├── home.py                 # Defines the Home Page UI
├── booking.py              # Defines the Flight Booking Form UI
├── reservations.py         # Defines the Reservation List Page UI
├── edit_reservation.py     # Defines the Edit Reservation Form UI
├── flights.db              # SQLite database file (automatically created)
├── requirements.txt        # Lists required Python libraries (e.g., PyInstaller)
└── README.md               # Project documentation (this file)


## Setup and Installation

### Prerequisites

* **Python 3.x:** Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
* **pip:** Python's package installer, usually included with Python 3.x.

### Steps

1.  **Clone the Repository (or create files manually):**

    If you're getting this from a Git repository:
    ```bash
    git clone [https://github.com/yourusername/flight_reservation_app_v2.git](https://github.com/yourusername/flight_reservation_app_v2.git)
    cd flight_reservation_app_v2
    ```
    If you're creating the files manually, ensure they are all in the same directory as shown in the project structure above.

2.  **Install Dependencies:**

    Open your terminal or command prompt in the `flight_reservation_app_v2` directory and install the necessary libraries listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    (Note: `tkinter` and `sqlite3` are standard libraries included with Python, so they don't need separate installation.)

## How to Run the Application

1.  **Navigate to the Project Directory:**
    Open your terminal or command prompt and go to the `flight_reservation_app_v2` folder:
    ```bash
    cd flight_reservation_app_v2
    ```

2.  **Run the Main Script:**
    Execute the `main.py` file using Python:
    ```bash
    python main.py
    ```
    The application window should appear. The `flights.db` database file will be automatically created in the project directory if it doesn't already exist.

## Building an Executable (Optional)

You can create a standalone executable file for Windows using PyInstaller, so the app can be run without a Python installation.

1.  **Ensure PyInstaller is Installed:**
    It should have been installed via `requirements.txt`. If not:
    ```bash
    pip install pyinstaller
    ```

2.  **Build the Executable:**
    In your terminal, from the `flight_reservation_app_v2` directory, run:
    ```bash
    python -m PyInstaller --onefile main.py
    ```
    This command will generate a `dist` folder in your project directory. Inside, you'll find `main.exe` (or `main` if on Linux/macOS), which is your standalone application.

3.  **Test the Executable:**
    Navigate into the `dist` folder and double-click `main.exe` to run your application.
