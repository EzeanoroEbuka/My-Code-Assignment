import unittest

from pythonSecondProject.airconditoner import AirCondition


class MyACCase(unittest.TestCase):

    def test_that_air_conditioner_is_on(self):
        self.ac = AirCondition()
        self.ac.turn_on()
        self.assertTrue(self.ac.check_on_or_off(), "Bike is ON lets Ride")

    def test_that_air_conditioner_is_off(self):
        self.ac = AirCondition()
        self.ac.turn_off()
        self.assertFalse(self.ac.check_on_or_off(), "Bike is OFF lets Ride")  # add assertion here

    def test_to_get_the_default_temperature_of_ac(self):
        self.ac = AirCondition()
        self.ac.turn_on()
        self.assertEqual(self.ac.check_temperature(), 20)

    def test_to_check_increase_in_temperature_of_ac(self):
        self.ac = AirCondition()
        self.ac.turn_on()
        self.assertEqual(self.ac.check_temperature(), 20)
        self.ac.increase_temperature()
        self.assertEqual(self.ac.check_temperature(), 21)
        self.ac.increase_temperature()
        self.ac.increase_temperature()
        self.assertEqual(self.ac.check_temperature(), 23)

    def test_to_check_decrease_in_temperature_of_ac(self):
        self.ac = AirCondition()
        self.ac.turn_on()
        self.assertEqual(self.ac.check_temperature(), 20)
        self.ac.decrease_temperature()
        self.assertEqual(self.ac.check_temperature(), 19)
        self.ac.decrease_temperature()
        self.ac.decrease_temperature()
        self.assertEqual(self.ac.check_temperature(), 17)

    def test_to_check_that_temperature_is_not_increased_above_30(self):
        self.ac = AirCondition()
        self.ac.turn_on()
        self.assertEqual(self.ac.check_temperature(), 20)
        for index in range(10):
            self.ac.increase_temperature()
        self.assertEqual(self.ac.check_temperature(), 30)
        self.ac.increase_temperature()
        self.ac.increase_temperature()
        self.assertEqual(self.ac.check_temperature(), 30)

    def test_to_check_that_temperature_is_not_decreased_above_30(self):
        self.ac = AirCondition()
        self.ac.turn_on()
        self.assertEqual(self.ac.check_temperature(), 20)
        for index in range(4):
            self.ac.decrease_temperature()
        self.assertEqual(self.ac.check_temperature(), 16)
        self.ac.decrease_temperature()
        self.ac.decrease_temperature()
        self.assertEqual(self.ac.check_temperature(), 16)


if __name__ == '__main__':
    unittest.main()
