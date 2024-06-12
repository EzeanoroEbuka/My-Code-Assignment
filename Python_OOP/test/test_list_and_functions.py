import unittest

from Python_OOP.pythonWeekendAssignment.list_and_function_assessment import *


class MyTestCase(unittest.TestCase):
    def test_that_list_elements_is_static(self):
        self.assertEqual(create_a_list_of_ten_numbers(), [37, 3, 28, 31, 37, 1, 14, 30, 32, 18])  # add assertion here
        self.assertEqual(create_a_list_of_ten_numbers(), [37, 3, 28, 31, 37, 1, 14, 30, 32, 18])  # add assertion here

    def test_that_length_of_list_is_10(self):
        self.assertEqual(get_length_of_list(create_a_list_of_ten_numbers()), 10)  # add assertion here

    def test_sum_of_element_in_even_index_of_list(self):
        self.assertEqual(sum_of_even_index([9, 7, 2, 1, 6, 8, 11, 5]), 28)

    def test_sum_of_element_in_odd_index_of_list(self):
        self.assertEqual(sum_of_odd_index([9, 7, 2, 1, 6, 8, 11, 5]), 21)

    def test_product_of_element_in_every_third_index_of_list(self):
        self.assertEqual(product_of_every_third_positions([9, 7, 2, 1, 6, 8, 11, 5, 12, 9, 6]), 99)

    def test_average_of_a_list(self):
        self.assertEqual(average_of_element_in_collection([2, 7, 2, 1, 6, 8, 1, 5]), 4)

    def test_to_get_the_largest_element_of_a_list(self):
        self.assertEqual(largest_of_the_list([2, 7, 2, 1, 6, 8, 1, 5]), 8)

    def test_to_get_the_smallest_element_of_a_list(self):
        self.assertEqual(smallest_of_the_list([2, 7, 2, 1, 6, 8, 1, 5]), 1)

    def test_to_get_the_string_at_the_beginning_and_end_of_a_list(self):
        self.assertEqual(count_strings(["king", "gymnastic", "sisters", "popcorn"]), "sisters")

    def test_that_function_returns_a_duplicate_of_sequence_between_1_and_15(self):
        self.assertEqual(duplicate_of_sequential_list_one_to_fifteen(),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                          14, 15])

    def test_that_function_returns_no_duplicate_of_sequence_between_1_and_15(self):
        self.assertEqual(eliminate_duplicated_element(), {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15})

    def test_that_function_returns_sum_of_third_element_in_list(self):
        self.assertEqual(add_third_element_in_a_designated_list([2, 7, 2, 1, 6, 8, 1, 5, 4]), 14)

    def test_that_function_returns_sum_of_first_middle_and_third_element_in_list(self):
        self.assertEqual(add_first_middle_and_last_element([2, 7, 2, 1, 6, 8, 1, 5, 4]), 12)
        self.assertEqual(add_first_middle_and_last_element([2, 7, 2, 1, 6, 1, 5, 4]), 9.5)

    def test_that_no_element_is_repeated_in_set(self):
        self.assertEqual(collect_and_store_without_duplicates([2, 5, 3, 5, 3, 6, 2, 1]), {2, 5, 3, 6, 1})

    def test_function_returns_the_sum_of_elements_in_collection(self):
        self.assertEqual(sum_of_element_in_collection([2, 5, 3, 2, 1]), 13)

    def test_that_the_specified_item_was_what_function_removed_from_collection(self):
        self.assertEqual(remove_item({2, 4, 7, 9, 1, 0}, 9), 9)

    def test_that_function_return_none_when_specified_element_not_found(self):
        self.assertEqual(remove_item({2, 4, 7, 9, 1, 0}, 12), None)

    def test_that_function_return_the_interception_of_two_sets(self):
        self.assertEqual((find_intersection({4, 9, 2, 7, 1}, {9, 0, 4, 1, 2, 12})), {4, 9, 2, 1})

    def test_that_function_return_the_union_of_two_sets(self):
        self.assertEqual((create_union({4, 9, 2, 7, 1}, {9, 0, 4, 1, 2, 12})), {4, 9, 2, 7, 1, 0, 12})

    def test_that_first_set_is_a_subset_of_second_set(self):
        self.assertEqual((check_for_subset({4, 9, 2, 7, 1}, {9, 7, 4, 1, 2, 12})), True)

    def test_that_function_removes_all_elements_in_set(self):
        self.assertEqual(remove_element_in_set({2, 4, 7, 9, 1, 0}), set())

    def test_that_function_returns_minimum_and_maximum_elements_of_set(self):
        self.assertEqual(maximum_and_minimum({2, 4, 7, 9, 1, 0}), (9, 0))

    def test_that_function_returns_the_length_of_set(self):
        self.assertEqual(length_of_set({2, 4, 7, 9, 1, 0}), 6)

    def test_that_an_empty_tuple_is_created(self):
        self.assertEqual(create_empty_tuple(), tuple())

    def test_that_the_sum_of_element_in_odd_index_of_tuple_is_returned(self):
        self.assertEqual(sum_of_odd_index_of_tuple((2, 4, 7, 9, 1, 0)), 13)

    def test_that_the_sum_of_element_in_even_index_of_tuple_is_returned(self):
        self.assertEqual(sum_of_even_index_of_tuple((2, 4, 7, 9, 1, 0)), 10)

    def test_that_function_adds_smallest_and_largest_number_in_tuple(self):
        self.assertEqual(sum_up_smallest_and_largest((2, 4, 7, 9, 1, 0)), 9)

    def test_that_the_first_five_elements_of_tuple_was_unpacked(self):
        self.assertEqual(unpack_first_five_element_of_tuple((2, 5, 7, 9, 8, 3, 5, 8)), (2, 5, 7, 9, 8))

    def test_that_dictionary_contain_10_student_items(self):
        self.assertEqual(populate_dictionary((2, 5, 7, 9, 8, 3, 5, 8), (2, 5, 7, 9, 8))


if __name__ == '__main__':
    unittest.main()
