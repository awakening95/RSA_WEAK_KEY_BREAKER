# 소수 p * q = N이고
# N = a^2 - b^2이 성립될 때
# N = (a + b) * (a - b)이고
# a + b = p, a - b = q가 성립

# a^2 - N = b^2 > 0


class FermatFactorization:
    def __init__(self, n):
        self.n = n
        self.a = int(self.n ** (1 / 2)) + 1
        self.b2 = (self.a * self.a) - self.n

    def is_square(self, old_x2):
        root_x = int(old_x2 ** (1/2))
        new_x2 = root_x * root_x
        if new_x2 == old_x2:
            return True
        return False
