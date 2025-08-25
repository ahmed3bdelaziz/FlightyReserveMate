import tkinter as tk
from tkinter import ttk, messagebox
from database import update_reservation, get_reservation_by_id

class EditReservationPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.reservation_id = None # To store the ID of the reservation being edited
        
        ttk.Label(self, text="Edit Reservation", font=("Helvetica", 20, "bold"), foreground="#00567a").pack(pady=30)
        
        # Frame for the input fields
        form_frame = ttk.Frame(self, padding="20 20 20 20")
        form_frame.pack(fill="both", expand=False, padx=50, pady=20)
        form_frame.columnconfigure(1, weight=1)

        fields = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
        self.entries = {} # Dictionary to hold Tkinter Entry widgets

        for i, field in enumerate(fields):
            ttk.Label(form_frame, text=f"{field}:", font=("Helvetica", 12)).grid(row=i, column=0, sticky="w", pady=10, padx=5)
            entry = ttk.Entry(form_frame, width=40, font=('Helvetica', 11))
            entry.grid(row=i, column=1, sticky="ew", pady=10, padx=5)
            self.entries[field] = entry

        # Frame for buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=30)

        # Update Button
        update_btn = ttk.Button(button_frame, text="Update Reservation", command=self.update_reservation, style='Accent.TButton')
        update_btn.pack(side="left", padx=10, ipadx=10, ipady=5)

        # Go Back Button
        back_btn = ttk.Button(button_frame, text="↩️ Go Back", command=lambda: controller.show_frame("ReservationsPage"))
        back_btn.pack(side="left", padx=10, ipadx=10, ipady=5)
    
    def set_data(self, data):
        """
        Receives reservation data from the controller and pre-fills the form fields.
        This method is called when navigating to this page with specific reservation data.
        """
        if data:
            self.reservation_id = data[0] # Store the ID for updating
            fields = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
            
            # Clear and insert data into entry fields
            for i, field_name in enumerate(fields):
                entry_widget = self.entries[field_name]
                entry_widget.delete(0, tk.END)
                # Data indices: 0=id, 1=name, 2=flight_number, 3=departure, 4=destination, 5=date, 6=seat_number
                entry_widget.insert(0, data[i+1]) # +1 because data[0] is ID

    def update_reservation(self):
        """
        Collects updated data from the form fields and calls the database function
        to modify the reservation. Provides user feedback.
        """
        if self.reservation_id is None:
            messagebox.showerror("Error", "No reservation selected for editing.")
            return

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
        
        # Simple date format validation
        if not (len(date) == 10 and date[4] == '-' and date[7] == '-'):
             messagebox.showerror("Input Error", "Please use YYYY-MM-DD format for the date.")
             return

        # Call database update function
        if update_reservation(self.reservation_id, name, flight_number, departure, destination, date, seat_number):
            messagebox.showinfo("Success", f"Reservation ID {self.reservation_id} updated successfully! ✨")
            self.controller.show_frame("ReservationsPage") # Go back to reservation list
        else:
            messagebox.showerror("Error", "Failed to update reservation. Please try again.")

    def on_show_page(self):
        # This page doesn't need to refresh its data automatically, as data is passed via set_data
        pass
