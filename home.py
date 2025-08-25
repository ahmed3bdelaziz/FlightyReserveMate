import tkinter as tk
from tkinter import ttk

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Welcome message
        welcome_label = ttk.Label(self, text="Welcome to FlightyReserveMate!", font=("Helvetica", 28, "bold"), foreground="#00567a")
        welcome_label.pack(pady=80)

        subtitle_label = ttk.Label(self, text="Your simple solution for flight reservations.", font=("Helvetica", 14), foreground="#333")
        subtitle_label.pack(pady=10)

        # Frame for buttons to center them better
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=50)

        # Book Flight Button
        book_btn = ttk.Button(button_frame, text="✈️ Book New Flight", command=lambda: controller.show_frame("BookingPage"), style='Accent.TButton')
        book_btn.pack(pady=15, ipadx=20, ipady=10) # Added internal padding

        # View Reservations Button
        view_btn = ttk.Button(button_frame, text="📄 View All Reservations", command=lambda: controller.show_frame("ReservationsPage"), style='TButton')
        view_btn.pack(pady=15, ipadx=20, ipady=10)

        # Custom button style for accent
        self.controller.style.configure('Accent.TButton', background='#007bbd', foreground='white', font=('Helvetica', 12, 'bold'))
        self.controller.style.map('Accent.TButton', background=[('active', '#00567a')])
