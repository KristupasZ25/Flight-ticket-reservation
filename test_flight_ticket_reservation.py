import unittest
from flight_ticket_reservation import User, Flight, Ticket, FlightFactory, generate_ticket_price, TICKET_CLASSES

class TestUser(unittest.TestCase):
    def test_login_valid_user(self):
        user = User("KristupasZ", "kursinis", "kristupaszazeckis@gmail.com")
        self.assertIsNotNone(user.login("KristupasZ", "kursinis"))

    def test_login_invalid_user(self):
        user = User("KristupasZ", "kursinis", "kristupaszazeckis@gmail.com")
        self.assertIsNone(user.login("invalid_username", "invalid_password"))

class TestFlightAndTicket(unittest.TestCase):
    def test_generate_ticket_price(self):
        flight = Flight("Vilnius", "London")
        self.assertEqual(flight.get_ticket_price(), 100)

    def test_ticket_calculate_price_economy(self):
        flight = Flight("Vilnius", "London")
        ticket = Ticket(flight, {"username": "KristupasZ"}, "economy", 1)
        self.assertEqual(ticket.calculate_ticket_price(), 100)

    def test_ticket_calculate_price_business(self):
        flight = Flight("Vilnius", "London")
        ticket = Ticket(flight, {"username": "KristupasZ"}, "business", 1)
        self.assertEqual(ticket.calculate_ticket_price(), 150)

    def test_ticket_calculate_price_first(self):
        flight = Flight("Vilnius", "London")
        ticket = Ticket(flight, {"username": "KristupasZ"}, "first", 1)
        self.assertEqual(ticket.calculate_ticket_price(), 200)

    def test_ticket_multiple_quantity(self):
        flight = Flight("Vilnius", "London")
        ticket = Ticket(flight, {"username": "KristupasZ"}, "first", 2)
        self.assertEqual(ticket.calculate_ticket_price(), 400)

class TestFlightFactory(unittest.TestCase):
    def test_create_flight(self):
        factory = FlightFactory()
        flight = factory.create_flight("Vilnius", "London", "economy")
        self.assertEqual(flight.get_flight_info(), "Vilnius to London")
        self.assertEqual(flight.get_ticket_price(), 100)

    def test_create_business_flight(self):
        factory = FlightFactory()
        flight = factory.create_flight("Vilnius", "London", "business")
        self.assertEqual(flight.get_flight_info(), "Vilnius to London")
        self.assertEqual(flight.get_ticket_price(), 150)

    def test_create_first_class_flight(self):
        factory = FlightFactory()
        flight = factory.create_flight("Vilnius", "London", "first")
        self.assertEqual(flight.get_flight_info(), "Vilnius to London")
        self.assertEqual(flight.get_ticket_price(), 200)

class TestGenerateTicketPrice(unittest.TestCase):
    def test_generate_ticket_price(self):
        self.assertEqual(generate_ticket_price("Vilnius", "London"), 100)
        self.assertEqual(generate_ticket_price("Vilnius", "Paris"), 100)
        self.assertEqual(generate_ticket_price("Kaunas", "London"), 100)
        self.assertEqual(generate_ticket_price("Kaunas", "Paris"), 100)

if __name__ == "__main__":
    unittest.main()
