"""
__author__ = Hagai Har-Gil
"""
import numpy as np
import attr


def validate_nonneg_int(instance, attribute, value):
    """ Validate that a number is a non-negative integer """
    if not isinstance(value, int) or value < 0:
        raise TypeError("n must be a non-negative number")


@attr.s
class CompareSeries:
    """ Compare Fibonacci series to prime numbers series """

    n = attr.ib(validator=validate_nonneg_int)

    def compare(self):
        """ Run the comparison of the series """
        if self.n == 0:
            return np.array([])
        fib_arr = self.gen_fib_arr()
        prime_arr = self.gen_prime_arr()
        return fib_arr - prime_arr

    def gen_fib_arr(self):
        """ Create a Fibonacci series up to some n """
        vals = (0, 1)
        result = [0, 1]
        for idx in range(self.n):
            vals = (vals[1], vals[0] + vals[1])
            result.append(vals[1])
        return np.array(result[:self.n])

    def gen_prime_arr(self):
        """
        Return a vector with the first n prime numbers
        """
        num = 3
        result = [2]
        primes_found = 0
        while primes_found < self.n-1:
            for divisor in range(num-1, 1, -1):
                if num % divisor == 0:
                    break
            else:
                primes_found += 1
                result.append(num)
            num += 1
        return np.array(result)

if __name__ == '__main__':
    print(CompareSeries(10).compare())