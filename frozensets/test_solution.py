import time
import unittest
from solution import find_common_elements
import random
import string


class TestFrozensetFunctionality(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(find_common_elements(["prod123", "prod567"], ["prod567", "prod891"]), frozenset(["prod567"]))

    def test_no_common_elements(self):
        self.assertEqual(find_common_elements(["prod123", "prod567"], ["prod890", "prod891"]), frozenset())

    def test_multiple_common_elements(self):
        self.assertEqual(find_common_elements(["prod123", "prod567", "prod890"], ["prod567", "prod890", "prod654"]),
                         frozenset(["prod567", "prod890"]))

    def test_immutability(self):
        result = find_common_elements(["prod123", "prod567"], ["prod567", "prod891"])
        with self.assertRaises(AttributeError):
            result.add("prod999")

    def test_empty_lists(self):
        self.assertEqual(find_common_elements([], []), frozenset())

    def test_performance(self):
        initial_size = 10 ** 3  # starting with a list of size 1,000
        max_size = 10 ** 5  # we'll scale up to a list of size 100,000
        time_threshold = 1.0  # each iteration should complete in less than 1 second

        current_size = initial_size
        while current_size <= max_size:
            list1 = [''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) for _ in range(current_size)]
            list2 = list1[-current_size // 2:] + [''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
                                                  for _ in range(current_size // 2)]

            start_time = time.time()
            find_common_elements(list1, list2)
            elapsed_time = time.time() - start_time

            self.assertLess(elapsed_time, time_threshold,
                            f"Size {current_size} took {elapsed_time:.2f} seconds, exceeding the threshold!")

            current_size *= 2  # double the size for the next iteration

    def test_alphanumeric_product_ids(self):
        self.assertEqual(find_common_elements(["prod123A", "prod56B"], ["prod56B", "prod891C"]), frozenset(["prod56B"]))

    def test_order_irrelevance(self):
        self.assertEqual(find_common_elements(["prod123", "prod567", "prod890"], ["prod890", "prod654", "prod567"]),
                         frozenset(["prod567", "prod890"]))
