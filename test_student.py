"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from models import Booking
from service import move_booking

# Add a unittest.TestCase class with your two test methods.
# See IA 3.2 for the cases and the expectation you must record before using AI.

class MoveStudentTests(unittest.TestCase):
    # Move a booking within the same room so its new interval overlaps its own old interval, with no other blocker.
    # Given: Booking 17 occupies Room 201 from 600 to 660 (no other bookings).
    # When: Move it within Room 201 to 630-690.
    # Expect: The move succeeds and returns the same updated booking object with no duplication.
    def test_same_room_overlapping_move_ignores_target(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]

        result = move_booking(bookings, 17, "Room 201", 630, 690)

        self.assertIs(result, target)
        self.assertEqual(target, Booking(17, "Room 201", 630, 690))
        self.assertIs(bookings[0], target)
        self.assertEqual(bookings, [target])

    # Request the booking's current room and times again.
    # Given: Booking 17 occupies Room 201 from 600 to 660.
    # When: Request Room 201 from 600 to 660 again.
    # Expect: The unchanged move succeeds and retains the same information (time, room, id, and number of bookings).
    def test_unchanged_move_succeeds(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]

        result = move_booking(bookings, 17, "Room 201", 600, 660)

        self.assertIs(result, target)
        self.assertEqual(target, Booking(17, "Room 201", 600, 660))
        self.assertIs(bookings[0], target)
        self.assertEqual(bookings, [target])

if __name__ == "__main__":
    unittest.main()
