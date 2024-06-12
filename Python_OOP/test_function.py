import unittest

from Python_OOP.pythonSecondProject.functions import calculate_the_length_of_a_collection


class MyTestCase(unittest.TestCase):

    def test_function_return_the_correct_length_of_a_single_character(self):
        self.assertEqual(1, calculate_the_length_of_a_collection("9"))

    def test_function_return_the_correct_length_of_many_characters(self):
        self.assertEqual(11, calculate_the_length_of_a_collection("hipopotamus"))  # add assertion here

    def test_function_return_0_an_empty_collection(self):
        self.assertEqual(0, calculate_the_length_of_a_collection(""))

    def test_function_return_the_correct_length_for_an_list(self):
        self.assertEqual(6, calculate_the_length_of_a_collection([3, 3, 4, 5, 6, 7]))  # add
