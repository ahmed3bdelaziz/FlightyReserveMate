import tkinter as tk
from tkinter import ttk # Import ttk for themed widgets
from database import create_table # Ensure database is set up on app start

# Import all page modules
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class FlightApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("FlightyReserveMate ✈️") # A more friendly title
        self.geometry("900x650") # Slightly larger window for better UI
        self.resizable(True, True) # Allow resizing

        # Apply a modern theme
        self.style = ttk.Style(self)
        self.style.theme_use('clam') # 'clam', 'alt', 'default', 'vista', 'xpnative'

        # Configure styles for better appearance
        self.style.configure('TFrame', background='#e0f2f7') # Light blue background
        self.style.configure('TLabel', background='#e0f2f7', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6)
        self.style.map('TButton', background=[('active', '#007bbd')]) # Darker blue on hover

        # Create a main container frame for all pages
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True, padx=10, pady=10) # Added padding
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        create_table() # Ensure the database table exists when the app starts

        self.frames = {}
        # Instantiate each page and store it in the frames dictionary
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # Place all frames on top of each other
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name, data=None):
        """
        Raises the requested page frame to the top, making it visible.
        Optionally passes data to the target frame (e.g., for editing a reservation).
        """
        frame = self.frames[page_name]
        if hasattr(frame, 'set_data') and data is not None:
            # If the frame has a set_data method, call it with the provided data
            frame.set_data(data)
        if hasattr(frame, 'on_show_page'):
            # Call a specific method if the page needs to refresh its content
            frame.on_show_page()
        frame.tkraise()

if __name__ == "__main__":
    app = FlightApp()
    app.mainloop()
