# FlightyReserveMate

A simple desktop application for flight reservation, built with Tkinter and SQLite.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

**FlightyReserveMate** is a desktop app that enables users to manage flight reservations through a user-friendly interface. The application uses Tkinter for the GUI and SQLite for data persistence, making it lightweight and easily deployable.

---

## Features

- Create, edit, and delete flight reservations
- Browse available flights
- Intuitive and responsive Tkinter interface
- Persistent data storage via SQLite
- Modular codebase for easy maintenance

---

## Repository Structure

```
FlightyReserveMate/
│
├── booking.py            # Handles booking logic and UI
├── database.py           # Database connection and queries
├── edit_reservation.py   # Editing existing reservations
├── home.py               # Home window and navigation
├── main.py               # Application entry point
├── reservations.py       # Reservations listing and management
│
├── requirements.txt      # Python dependencies
├── main.spec             # PyInstaller spec for building executable
├── .gitattributes        # Git configuration
│
├── build/                # Build artifacts (after packaging)
├── dist/                 # Distribution files (after packaging)
│
└── README.md             # Project documentation
```

---

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ahmed3bdelaziz/FlightyReserveMate.git
    cd FlightyReserveMate
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

Run the application using:
```bash
python main.py
```
*(If you package the app using PyInstaller, use the generated executable in the dist/ directory)*

---

## Contributing

Contributions are welcome! If you spot issues or want to add features, feel free to open an issue or submit a pull request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/feature-name`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request


---

## Contact

For questions or support, open an [issue](https://github.com/ahmed3bdelaziz/FlightyReserveMate/issues) or contact [@ahmed3bdelaziz](https://github.com/ahmed3bdelaziz).

---

*Happy flying and reserving!*
