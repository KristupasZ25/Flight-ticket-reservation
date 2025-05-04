import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

users_db = [
    {"username": "KristupasZ", "password": "kursinis", "email": "kristupaszazeckis@gmail.com"},
    {"username": "ChrisZ", "password": "work", "email": "chriz@gmail.com"}
]

TICKET_CLASSES = {
    "economy": {"price_addition": 0, "label": "Economy Class"},
    "business": {"price_addition": 50, "label": "Business Class"},
    "first": {"price_addition": 100, "label": "First Class"}
}

def generate_ticket_price(departure_city, destination_city):
    base_price = 100 
    return base_price

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def login(self, entered_username, entered_password):
        for user in users_db:
            if user['username'] == entered_username and user['password'] == entered_password:
                return user
        return None

class Flight:
    def __init__(self, departure_city, destination_city):
        self.departure_city = departure_city
        self.destination_city = destination_city

    def get_flight_info(self):
        return f"{self.departure_city} to {self.destination_city}"

    def get_ticket_price(self):
        return generate_ticket_price(self.departure_city, self.destination_city)

class EconomyFlight(Flight):
    def get_ticket_price(self):
        return generate_ticket_price(self.departure_city, self.destination_city)

class BusinessFlight(Flight):
    def get_ticket_price(self):
        return generate_ticket_price(self.departure_city, self.destination_city) + 50

class FirstClassFlight(Flight):
    def get_ticket_price(self):
        return generate_ticket_price(self.departure_city, self.destination_city) + 100

class FlightFactory:
    def create_flight(self, departure_city, destination_city, ticket_type):
        if ticket_type == "economy":
            return EconomyFlight(departure_city, destination_city)
        elif ticket_type == "business":
            return BusinessFlight(departure_city, destination_city)
        elif ticket_type == "first":
            return FirstClassFlight(departure_city, destination_city)
        else:
            return Flight(departure_city, destination_city)

class Ticket:
    def __init__(self, flight, passenger, ticket_type, quantity):
        self.flight = flight
        self.passenger = passenger
        self.ticket_type = ticket_type
        self.quantity = int(quantity)
        self.ticket_price = self.calculate_ticket_price()

    def calculate_ticket_price(self):
        price_per_ticket = self.flight.get_ticket_price()
        ticket_info = TICKET_CLASSES.get(self.ticket_type, {"price_addition": 0, "label": "Unknown Class"})
        
        final_price = price_per_ticket + ticket_info["price_addition"]
        final_price *= self.quantity
        return final_price

    def get_ticket_info(self):
        ticket_info = TICKET_CLASSES.get(self.ticket_type, {"label": "Unknown Class"})
        return f"Ticket for {self.passenger['username']} on flight: {self.flight.get_flight_info()} ({ticket_info['label']})\n" \
               f"Quantity: {self.quantity}\nTotal Price: €{self.ticket_price}"

    def get_ticket_price(self):
        return self.ticket_price

class FlightBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EuropeAir - Flight Booking System")
        self.root.geometry("500x350")
        self.center_window(root, 500, 350)

        self.current_user = None
        self.create_login_screen()
        self.is_booking_completed = False

    def center_window(self, root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
        root.geometry(f'{width}x{height}+{position_right}+{position_top}')

    def create_login_screen(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)

        self.username_label = ttk.Label(self.login_frame, text="Username:", font=("Arial", 12))
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.password_label = ttk.Label(self.login_frame, text="Password:", font=("Arial", 12))
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.username_entry = ttk.Entry(self.login_frame, font=("Arial", 12))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_entry = ttk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        user = User(entered_username, entered_password, "")
        logged_in_user = user.login(entered_username, entered_password)
        if logged_in_user:
            self.current_user = logged_in_user
            messagebox.showinfo("Login Successful", f"Welcome back, {self.current_user['username']}!")
            self.show_flight_search_screen()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password!")

    def show_flight_search_screen(self):
        self.login_frame.pack_forget()

        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(padx=20, pady=20)

        departure_cities = ["Vilnius", "Kaunas"]
        destination_cities = ["London", "Paris", "Berlin", "Rome", "Madrid", "Athens", "Istanbul"]
        destination_cities_with_prices = [f"{city} - €{generate_ticket_price('Vilnius', city)}" for city in destination_cities]

        self.departure_label = ttk.Label(self.search_frame, text="Departure City:", font=("Arial", 12))
        self.departure_label.grid(row=0, column=0, padx=10, pady=5)

        self.destination_label = ttk.Label(self.search_frame, text="Destination City:", font=("Arial", 12))
        self.destination_label.grid(row=1, column=0, padx=10, pady=5)

        self.departure_combobox = ttk.Combobox(self.search_frame, values=departure_cities, font=("Arial", 12))
        self.departure_combobox.grid(row=0, column=1, padx=10, pady=5)

        self.destination_combobox = ttk.Combobox(self.search_frame, values=destination_cities_with_prices, font=("Arial", 12))
        self.destination_combobox.grid(row=1, column=1, padx=10, pady=5)

        departure_dates = ["2025-05-02", "2025-05-03", "2025-05-04", "2025-05-05", "2025-05-06", "2025-05-07"]
        return_dates = ["2025-06-07", "2025-06-08", "2025-06-09", "2025-06-10", "2025-06-11", "2025-06-12"]

        self.departure_date_label = ttk.Label(self.search_frame, text="Departure Date:", font=("Arial", 12))
        self.departure_date_label.grid(row=2, column=0, padx=10, pady=5)

        self.return_date_label = ttk.Label(self.search_frame, text="Return Date:", font=("Arial", 12))
        self.return_date_label.grid(row=3, column=0, padx=10, pady=5)

        self.departure_date_combobox = ttk.Combobox(self.search_frame, values=departure_dates, font=("Arial", 12))
        self.departure_date_combobox.grid(row=2, column=1, padx=10, pady=5)

        self.return_date_combobox = ttk.Combobox(self.search_frame, values=return_dates, font=("Arial", 12))
        self.return_date_combobox.grid(row=3, column=1, padx=10, pady=5)

        self.one_way_var = tk.BooleanVar()
        self.one_way_label = ttk.Label(self.search_frame, text="One-Way:", font=("Arial", 12))
        self.one_way_label.grid(row=4, column=0, padx=10, pady=5)

        self.one_way_checkbox = ttk.Checkbutton(self.search_frame, variable=self.one_way_var, command=self.toggle_return_date)
        self.one_way_checkbox.grid(row=4, column=1, padx=10, pady=5)

        self.ticket_type_label = ttk.Label(self.search_frame, text="Ticket Type:", font=("Arial", 12))
        self.ticket_type_label.grid(row=5, column=0, padx=10, pady=5)

        self.ticket_type_combobox = ttk.Combobox(self.search_frame, values=["economy", "business", "first"], font=("Arial", 12))
        self.ticket_type_combobox.grid(row=5, column=1, padx=10, pady=5)

        self.quantity_label = ttk.Label(self.search_frame, text="Number of Tickets:", font=("Arial", 12))
        self.quantity_label.grid(row=6, column=0, padx=10, pady=5)

        self.quantity_entry = ttk.Entry(self.search_frame, font=("Arial", 12))
        self.quantity_entry.grid(row=6, column=1, padx=10, pady=5)

        self.search_button = ttk.Button(self.search_frame, text="Search Flights", command=self.search_flights)
        self.search_button.grid(row=7, columnspan=2, pady=10)

    def toggle_return_date(self):
        if self.one_way_var.get():
            self.return_date_combobox.config(state="disabled")
            self.return_date_combobox.set("N/A")
        else:
            self.return_date_combobox.config(state="normal")

    def search_flights(self):
        departure_city = self.departure_combobox.get()
        destination_city = self.destination_combobox.get()
        departure_date = self.departure_date_combobox.get()
        return_date = self.return_date_combobox.get() if not self.one_way_var.get() else "N/A"
        ticket_type = self.ticket_type_combobox.get()
        quantity = self.quantity_entry.get()

        if int(quantity) > 2:
            messagebox.showerror("Input Error", "You can only book a maximum of 2 tickets.")
            return

        if not departure_city or not destination_city or not departure_date or not ticket_type or not quantity:
            messagebox.showerror("Input Error", "Please select all fields.")
            return

        factory = FlightFactory()
        flight = factory.create_flight(departure_city, destination_city, ticket_type)

        ticket_info = TICKET_CLASSES.get(ticket_type, {"price_addition": 0, "label": "Unknown Class"})
        final_price = flight.get_ticket_price() * int(quantity)

        ticket_type_label = ticket_info["label"]

        messagebox.showinfo("Flight Found", f"Searching flights from {departure_city} to {destination_city}...\nTicket Type: {ticket_type_label}\nTotal Price: €{final_price}")
        self.show_ticket_screen(departure_city, destination_city, departure_date, ticket_type_label, final_price, return_date)

    def show_ticket_screen(self, departure_city, destination_city, departure_date, ticket_type, total_price, return_date):
        self.search_frame.pack_forget()

        self.ticket_frame = tk.Frame(self.root)
        self.ticket_frame.pack(padx=20, pady=20)

        self.ticket_info_label = ttk.Label(self.ticket_frame, text=f"Your flight from {departure_city} to {destination_city} has been found!\n\n"
                                                                 f"Reservation information:\n"
                                                                 f"Ticket Type: {ticket_type}\nDeparture Date: {departure_date}\nReturn Date: {return_date}\nPrice: €{total_price}\n\n"
                                                                 f"Do you want to proceed with your order?", font=("Arial", 12), anchor='w')
        self.ticket_info_label.grid(row=0, columnspan=2)

        self.confirm_button = ttk.Button(self.ticket_frame, text="Confirm", command=self.confirm_reservation)
        self.confirm_button.grid(row=1, columnspan=2, pady=10)

        self.logout_button = ttk.Button(self.ticket_frame, text="Logout", command=self.logout)
        self.logout_button.grid(row=2, columnspan=2, pady=5)

    def confirm_reservation(self):
        departure_city = self.departure_combobox.get()
        destination_city = self.destination_combobox.get()
        departure_date = self.departure_date_combobox.get()
        ticket_type = self.ticket_type_combobox.get()
        return_date = self.return_date_combobox.get() if not self.one_way_var.get() else "N/A"
        quantity = self.quantity_entry.get()

        flight = Flight(departure_city, destination_city)
        ticket = Ticket(flight, self.current_user, ticket_type, quantity)
        total_price = ticket.get_ticket_price()

        with open("reservations.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.current_user['username'], 
                             "Flight123",
                             departure_city, 
                             destination_city, 
                             generate_ticket_price(departure_city, destination_city),
                             departure_date, 
                             return_date,
                             ticket_type, 
                             quantity,
                             total_price])

        messagebox.showinfo("Successfully Booked", f"Your flight has been successfully booked!\nReservation receipt has been sent to {self.current_user['email']}.")
        self.is_booking_completed = True
        self.show_logout_button()

    def show_logout_button(self):
        if self.is_booking_completed:
            self.logout_button.config(state="normal")

    def logout(self):
        self.root.quit()
        messagebox.showinfo("Logged out", "You have been logged out of your account.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingApp(root)
    root.mainloop()
