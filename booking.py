import tkinter as tk
from tkinter import ttk, messagebox
from database import add_reservation

class BookingPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Title for the booking page
        ttk.Label(self, text="Book a New Flight", font=("Helvetica", 20, "bold"), foreground="#00567a").pack(pady=30)

        # Frame to hold the input fields, for better organization
        form_frame = ttk.Frame(self, padding="20 20 20 20")
        form_frame.pack(fill="both", expand=False, padx=50, pady=20) # Center the form
        form_frame.columnconfigure(1, weight=1) # Make the entry column expandable

        fields = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
        self.entries = {}
        
        for i, field in enumerate(fields):
            ttk.Label(form_frame, text=f"{field}:", font=("Helvetica", 12)).grid(row=i, column=0, sticky="w", pady=10, padx=5)
            entry = ttk.Entry(form_frame, width=40, font=('Helvetica', 11))
            entry.grid(row=i, column=1, sticky="ew", pady=10, padx=5)
            self.entries[field] = entry
        
        # Frame for buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=30)

        # Submit Button
        submit_btn = ttk.Button(button_frame, text="Submit Reservation", command=self.submit, style='Accent.TButton')
        submit_btn.pack(side="left", padx=10, ipadx=10, ipady=5)

        # Go Home Button
        home_btn = ttk.Button(button_frame, text="Go Home", command=lambda: controller.show_frame("HomePage"))
        home_btn.pack(side="left", padx=10, ipadx=10, ipady=5)

    def submit(self):
        """
        Collects data from input fields, validates it, and adds a new reservation to the database.
        Provides user feedback via messagebox.
        """
        name = self.entries["Name"].get().strip()
        flight_number = self.entries["Flight Number"].get().strip()
        departure = self.entries["Departure"].get().strip()
        destination = self.entries["Destination"].get().strip()
        date = self.entries["Date (YYYY-MM-DD)"].get().strip()
        seat_number = self.entries["Seat Number"].get().strip()

        # Basic input validation
        if not all([name, flight_number, departure, destination, date, seat_number]):
            messagebox.showerror("Input Error", "All fields are required! Please fill out all the information.")
            return

        # Simple date format validation (can be improved with regex or a date picker)
        if not (len(date) == 10 and date[4] == '-' and date[7] == '-'):
             messagebox.showerror("Input Error", "Please use YYYY-MM-DD format for the date.")
             return

        # Add reservation to the database
        if add_reservation(name, flight_number, departure, destination, date, seat_number):
            messagebox.showinfo("Success", "Reservation booked successfully! 🎉")
            # Clear input fields after successful booking
            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.controller.show_frame("HomePage") # Navigate back to home page
        else:
            messagebox.showerror("Error", "Failed to book reservation. Please try again.")

    def set_data(self, data=None):
        # This page doesn't receive data, but the method is here for consistency
        # when called by controller.show_frame
        pass
