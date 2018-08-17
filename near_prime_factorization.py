from random import *
import prime


class NearPrimeFactorization:
    def __init__(self, n):
        self.n = n
        self.root_n = int(self.n ** (1/2))
        self.p = self.root_n
        self.q = self.root_n

    def start(self):
        if self.root_n % 2 == 0:
            self.root_n = self.root_n - 1

        for self.p in range(self.root_n, int(self.root_n * 3 / 4), -2):
            if prime.is_prime(self.p) == 1:
                if self.n % self.p == 0:
                    self.q = int(self.n / self.p)
                    break

        print("p :", self.p, "q", self.q)

# cypher = input("Input cypher text :")