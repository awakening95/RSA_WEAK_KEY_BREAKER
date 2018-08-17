from sympy import *
import fermat_factorization
import hastad_broadcast_attack
import near_prime_factorization
import wiener_attack


def con_fraction(n, d):  # get continued fraction of n/d
    e = []
    q = n // d
    r = n % d
    e.append(q)

    while r != 0:
        n, d = d, r
        q = n // d
        r = n % d
        e.append(q)

    return e


while True:
    print("┌──────────────────────────────────────────────────┐")
    print("│                                     RSA WEAK KEY BREAKER                                     │")
    print("├──────────────────────────────────────────────────┤")
    print("│                                                                                              │")
    print("│1. Near prime factorization                                                                   │")
    print("│                                                                                              │")
    print("│2. Fermat factorization                                                                       │")
    print("│                                                                                              │")
    print("│3. Hastad broadcast attack                                                                    │")
    print("│                                                                                              │")
    print("│4. Wiener's attack                                                                            │")
    print("│                                                                                              │")
    print("│5. exit                                                                                       │")
    print("│                                                                                              │")
    print("└──────────────────────────────────────────────────┘")

    number = int(input("Please input number :"))

    if number == 1:
        n = int(input("Input N :"))
        x = near_prime_factorization.NearPrimeFactorization(n)
        x.start()

    elif number == 2:
        n = int(input("Input N :"))
        # cypher = input("Input cypher text :")

        a = int(n ** (1 / 2)) + 1
        b2 = (a * a) - n

        x = fermat_factorization.FermatFactorization(n)

        while True:
            if x.is_square(b2):
                break
            a = a + 1
            b2 = (a * a) - n

        b = b2 ** (1 / 2)

        p = int(a + b)
        q = int(a - b)
        n = p * q

        print("p :", p, "q :", q)

    elif number == 3:
        e = int(input("Input e :"))

        list_n = []
        list_cipher_text = []

        for i in range(e):
            n = int(input("Input N :"))
            list_n.append(n)
            cipher_text = int(input("Input cipher text :"))
            list_cipher_text.append(cipher_text)

        x = hastad_broadcast_attack.HastadBroadcastAttack()

        c = x.crt_list(list_n, list_cipher_text)

        text = int(round(c ** (1 / e)))

        print("text :", text)

    elif number == 4:
        n = int(input("Input N:"))
        e = int(input("Input e:"))

        cf_expansion = con_fraction(e, n)

        x = wiener_attack.WienerAttack()

        conv = x.convergents(cf_expansion)

        for pk, pd in conv:
            if pk == 0:
                continue

            possible_phi = (e * pd - 1) // pk
            p = Symbol('p', integer=True)
            roots = solve(p ** 2 + (possible_phi - n - 1) * p + n, p)

            if len(roots) == 2:
                if roots[0] * roots[1] == n:
                    print("p :", roots[0], "q :", roots[1])

    elif number == 5:
        break



