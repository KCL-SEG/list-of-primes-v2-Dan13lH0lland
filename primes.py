"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    else:
        list = [2]
        counter = 3
        baseCounter = 1
        isPrime = False
        if number_of_primes == 1:
            return list
        else:
            while baseCounter != number_of_primes:
                isPrime = False
                for x in range(2, counter):
                    if (counter % x) == 0:
                        isPrime = False
                        break
                    else:
                        isPrime = True
                if isPrime:
                    list.append(counter)
                    baseCounter += 1
                counter += 1
            return list
