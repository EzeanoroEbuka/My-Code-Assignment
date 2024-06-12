import unittest

from pythonSecondProject.play_code import MyStonyStack


class StonyTestCase(unittest.TestCase):

    def set_up(self):
        self.stack = MyStonyStack()
        self.stack.adding_to_stony("king")
        self.stack.adding_to_stony("erratum")
        self.stack.adding_to_stony("limited")

    def test_that_stack_added_successfully(self):
        self.set_up()
        self.assertEqual(len(self.stack.stony), 3)  # add assertion here

    def test_that_the_last_element_of_stony_of_stack_has_been_remove(self):
        self.set_up()
        self.stack.pop()
        self.assertEqual(self.stack.stony[-1], "erratum")

    def set_up_two(self):
        self.stack = MyStonyStack()
        self.stack.adding_to_queue("fish")
        self.stack.adding_to_queue("credible")
        self.stack.adding_to_queue("limited")

    def test_that_elements_was_added_successfully_in_queue(self):
        self.set_up_two()
        self.assertEqual(len(self.stack.queue), 3)

    def test_that_first_element_was_removed_from_queue(self):
        self.set_up_two()
        self.stack.remove()
        self.assertEqual(self.stack.queue[0], "credible")

if __name__ == '__main__':
    unittest.main()
