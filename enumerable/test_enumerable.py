import unittest
from expects import *


class TestEnumerableFilter(unittest.TestCase):
    def setUp(self):
        self.test_data = [1, 2, 3, 4, 5]
        return super().setUp()

    def test_it_should_return_an_enumerable_object(self):
        """
        When called it should always return an enumerable object.
        """
        from enumerable.iterators import Enumerable

        def even_numbers(x):
            return x % 2 == 0

        result = Enumerable(self.test_data).filter(even_numbers)
        expect(result).to(be_a(Enumerable))

    def test_it_should_filter_items_based_on_provided_function(self):
        """
        When called it should filter out items based on the provided function.
        """
        from enumerable.iterators import Enumerable

        def even_numbers(x):
            # Returns true if x is evenly divisible by two
            return x % 2 == 0

        result = Enumerable(self.test_data).filter(even_numbers).to(tuple)
        expect(result).to(equal((2,4)))

    def test_it_should_pass_additional_paramaters_to_provided_function(self):
        """
        When called with additional arguments, those arguments should
        be passed to the provided function.
        """
        from enumerable.iterators import Enumerable

        def divisible_by(x, div):
            # Returns true if x is evenly divisible by div
            return x % div == 0

        result = Enumerable(self.test_data).filter(divisible_by, 2).to(tuple)
        expect(result).to(equal((2,4)))


class TestEnumerableMap(unittest.TestCase):
    def setUp(self):
        self.test_data = [1, 2, 3, 4, 5]
        return super().setUp()

    def test_it_should_return_an_enumerable_object(self):
        """
        When called it should return an Enumerable object.
        """
        from enumerable.iterators import Enumerable

        def square_number(x):
            # Returns x^2
            return x * x

        result = Enumerable(self.test_data).map(square_number)
        expect(result).to(be_a(Enumerable))

    def test_it_should_return_the_results_of_each_item_passed_to_the_provided_function(self):
        """
        When called, it should return the results of each item in the iterable
        passed to the function.
        """
        from enumerable.iterators import Enumerable

        def square_number(x):
            # Returns x^2
            return x*x

        result = Enumerable(self.test_data).map(square_number).to(tuple)
        expect(result).to(equal((1, 4, 9, 16, 25)))

    def test_it_should_pass_additiona_parameters_to_the_provided_function(self):
        """
        When called it should pass any additional paramaters to the provided
        function.
        """
        from enumerable.iterators import Enumerable

        def multiply_by(x, mul):
            return x * mul

        results = Enumerable(self.test_data).map(multiply_by, 2).to(tuple)
        expect(results).to(equal((2, 4, 6, 8, 10)))


class TestEnumerableReduce(unittest.TestCase):
    def setUp(self):
        self.test_data = [1, 2, 3, 4, 5]
        return super().setUp()

    def test_it_should_reduce_the_iterable_down_to_a_single_value(self):
        """
        When called it should reduce the iterable down to a single value.
        """
        from enumerable.iterators import Enumerable

        def sum(accumulator, value):
            return accumulator + value

        result = Enumerable(self.test_data).reduce(sum)
        expect(result).to(equal(15))

    def test_the_accumulator_should_start_at_the_initializer_value(self):
        """
        When provided an initializer value, the accumulator should start at
        this value.
        """
        from enumerable.iterators import Enumerable

        def sum(accumulator, value):
            return accumulator + value

        result = Enumerable(self.test_data).reduce(sum, 10)
        expect(result).to(equal(25))

    def test_it_should_pass_additional_paramaters_to_the_provided_function(self):
        """
        When provided with additional paramaters it should pass them to the
        provided function.
        """
        from enumerable.iterators import Enumerable

        def sum_plus(accumulator, value, padding):
            return accumulator + value + padding

        result = Enumerable(self.test_data).reduce(sum_plus, 0, 1)
        expect(result).to(equal(20))


class TestEnumerableTo(unittest.TestCase):
    def test_it_should_cast_the_internal_iterator_to_the_provided_container_type(self):
        """
        When called it should return the internal iterator cast as the provided type.
        """
        from enumerable.iterators import Enumerable

        test_data = [1, 2, 3, 4, 5]
        results = Enumerable(test_data).to(list)
        expect(results).to(equal(test_data))

if __name__ == '__main__':
    unittest.main()
