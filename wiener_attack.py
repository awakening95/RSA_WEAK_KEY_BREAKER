from sympy import *


class WienerAttack:
    def convergents(self, e):
        n = []
        d = []

        for i in range(len(e)):
            if i == 0:
                ni = e[i]
                di = 1
            elif i == 1:
                ni = e[i] * e[i - 1] + 1
                di = e[i]
            else:
                ni = e[i] * n[i - 1] + n[i - 2]
                di = e[i] * d[i - 1] + d[i - 2]

            n.append(ni)
            d.append(di)
            yield (ni, di)


