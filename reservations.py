import tkinter as tk
from tkinter import ttk, messagebox
from database import get_all_reservations, delete_reservation, get_reservation_by_id

class ReservationsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        ttk.Label(self, text="All Flight Reservations", font=("Helvetica", 20, "bold"), foreground="#00567a").pack(pady=30)
        
        # Frame for the Treeview and its scrollbar
        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Scrollbar for the Treeview
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side="right", fill="y")

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"),
                                 show="headings", yscrollcommand=tree_scroll.set, selectmode="extended") # Added selectmode="extended"
        
        # Configure scrollbar
        tree_scroll.config(command=self.tree.yview)

        # Define column headings and widths
        self.tree.heading("ID", text="ID", anchor="center")
        self.tree.heading("Name", text="Passenger Name", anchor="w")
        self.tree.heading("Flight", text="Flight No.", anchor="center")
        self.tree.heading("Departure", text="Departure", anchor="w")
        self.tree.heading("Destination", text="Destination", anchor="w")
        self.tree.heading("Date", text="Date", anchor="center")
        self.tree.heading("Seat", text="Seat No.", anchor="center")

        self.tree.column("ID", width=40, anchor="center")
        self.tree.column("Name", width=150, anchor="w")
        self.tree.column("Flight", width=80, anchor="center")
        self.tree.column("Departure", width=120, anchor="w")
        self.tree.column("Destination", width=120, anchor="w")
        self.tree.column("Date", width=100, anchor="center")
        self.tree.column("Seat", width=70, anchor="center")

        self.tree.pack(fill="both", expand=True)
        
        # Bind double-click to edit reservation (only first selected)
        self.tree.bind("<Double-1>", self.on_double_click)
        
        # Frame for action buttons (Edit, Delete, Home)
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="✏️ Edit Selected", command=self.edit_selected_reservation).pack(side="left", padx=10, ipadx=10, ipady=5)
        ttk.Button(button_frame, text="🗑️ Delete Selected", command=self.delete_selected_reservation, style='Danger.TButton').pack(side="left", padx=10, ipadx=10, ipady=5)
        ttk.Button(button_frame, text="🏠 Go Home", command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=10, ipadx=10, ipady=5)
        
        # Custom button style for danger action
        self.controller.style.configure('Danger.TButton', background='#dc3545', foreground='white', font=('Helvetica', 12, 'bold'))
        self.controller.style.map('Danger.TButton', background=[('active', '#c82333')])

        # Populate table initially
        self.populate_table()

    def on_show_page(self, event=None):
        """
        This method is called by the controller when this page is brought to the front.
        It ensures the reservation list is always up-to-date.
        """
        self.populate_table()

    def populate_table(self):
        """
        Clears existing entries in the Treeview and populates it with fresh data
        from the database.
        """
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get all reservations from the database
        reservations = get_all_reservations()
        
        # Insert each reservation into the Treeview
        if reservations:
            for res in reservations:
                self.tree.insert('', 'end', values=res)
        else:
            # Display a message if no reservations are found
            self.tree.insert('', 'end', values=["", "No reservations found.", "", "", "", "", ""], tags=('no_data',))
            self.tree.tag_configure('no_data', foreground='gray', font=('Helvetica', 10, 'italic'))


    def on_double_click(self, event):
        """Handles double-click event on a reservation row to initiate editing."""
        self.edit_selected_reservation()

    def edit_selected_reservation(self):
        """
        Retrieves the selected reservation's data and passes it to the
        EditReservationPage for modification. If multiple items are selected,
        only the first one will be considered for editing.
        """
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("No Selection", "Please select a reservation from the list to edit.")
            return

        # For editing, we typically only allow one item at a time
        if len(selected_items) > 1:
            messagebox.showwarning("Multiple Selection", "Please select only one reservation to edit.")
            return

        selected_item = selected_items[0]
        reservation_data = self.tree.item(selected_item, "values")
        
        if "No reservations found." in reservation_data: # Prevent editing the "no data" message
            return

        # Navigate to the EditReservationPage, passing the reservation data
        self.controller.show_frame("EditReservationPage", data=reservation_data)

    def delete_selected_reservation(self):
        """
        Deletes the selected reservation(s) from the database after user confirmation.
        Refreshes the table upon successful deletion.
        """
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("No Selection", "Please select at least one reservation from the list to delete.")
            return

        # Filter out the "No reservations found." message if it's somehow selected
        items_to_delete = []
        for item_id in selected_items:
            data = self.tree.item(item_id, "values")
            if "No reservations found." not in data:
                items_to_delete.append((item_id, data[0])) # Store Treeview item ID and DB reservation ID

        if not items_to_delete:
            messagebox.showwarning("No Valid Selection", "No valid reservations selected for deletion.")
            return

        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {len(items_to_delete)} reservation(s)?")
        if confirm:
            deleted_count = 0
            for tree_item_id, reservation_id in items_to_delete:
                if delete_reservation(reservation_id):
                    deleted_count += 1
                else:
                    # Optionally log which item failed to delete
                    print(f"Failed to delete reservation ID: {reservation_id}")

            if deleted_count > 0:
                messagebox.showinfo("Success", f"{deleted_count} reservation(s) deleted successfully! ✅")
                self.populate_table() # Refresh the table after all deletions
            else:
                messagebox.showerror("Error", "No reservations were deleted. Please check for database errors.")