import unittest
from flight_ticket_reservation import User, Flight, Ticket, FlightFactory, generate_ticket_price

class TestUser(unittest.TestCase):
    def test_login_valid_user(self):
        user = User("KristupasZ", "kursinis", "kristupaszazeckis@gmail.com")
        self.assertTrue(user.login("KristupasZ", "kursinis"))

    def test_login_invalid_user(self):
        user = User("KristupasZ", "kursinis", "kristupaszazeckis@gmail.com")
        self.assertFalse(user.login("invalid_username", "invalid_password"))

class TestFlightAndTicket(unittest.TestCase):
    def test_generate_ticket_price(self):
        flight = Flight("Vilnius", "London")
        self.assertEqual(flight.get_ticket_price(), 100)

    def test_ticket_calculate_price_economy(self):
        flight = Flight("Vilnius", "London")
        ticket = Ticket(flight, "KristupasZ", "economy", 1)
        self.assertEqual(ticket.calculate_ticket_price(), 100)

    def test_ticket_calculate_price_business(self):
        flight = Flight("Vilnius", "London")
        ticket = Ticket(flight, "KristupasZ", "business", 1)
        self.assertEqual(ticket.calculate_ticket_price(), 150)

    def test_ticket_calculate_price_first(self):
        flight = Flight("Vilnius", "London")
        ticket = Ticket(flight, "KristupasZ", "first", 1)
        self.assertEqual(ticket.calculate_ticket_price(), 200)

    def test_ticket_multiple_quantity(self):
        flight = Flight("Vilnius", "London")
        ticket = Ticket(flight, "KristupasZ", "first", 2)
        self.assertEqual(ticket.calculate_ticket_price(), 400)

class TestFlightFactory(unittest.TestCase):
    def test_create_flight(self):
        factory = FlightFactory()
        flight = factory.create_flight("Vilnius", "London")
        self.assertEqual(flight.get_flight_info(), "Vilnius to London")
        self.assertEqual(flight.get_ticket_price(), 100)

class TestGenerateTicketPrice(unittest.TestCase):
    def test_generate_ticket_price(self):
        self.assertEqual(generate_ticket_price("Vilnius", "London"), 100)
        self.assertEqual(generate_ticket_price("Vilnius", "Paris"), 100)
        self.assertEqual(generate_ticket_price("Kaunas", "London"), 100)
        self.assertEqual(generate_ticket_price("Kaunas", "Paris"), 100)

if __name__ == "__main__":
    unittest.main()