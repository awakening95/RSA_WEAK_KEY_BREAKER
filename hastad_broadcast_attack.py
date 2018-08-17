class HastadBroadcastAttack:
    def crt_list(self, mod, values):
        # m = mod[1] * mod[2] * ... * mod[i]
        # n[i] = m / mod[i]
        # ((s[i] * n[i]) % mod[i]) == 1 (s[i]는 정수)
        # x = value[1] * n[1] * s[1] + ... + value[i] * n[i] * s[i]
        # x = x % m (실제 해)

        m = 1
        n = []
        s = []
        x = 0

        num = len(mod)  # 합동식의 개수

        for i in range(num):  # m
            m = m * mod[i]

        for i in range(num):  # n[i], s[i]
            n.append(int(m / mod[i]))
            s.append(int(1))
            while ((s[i] * n[i]) % mod[i]) != 1:
                s[i] = s[i] + 1

        for i in range(num):  # x
            x = x + (values[i] * n[i] * s[i])

        x = x % m  # 실제 해

        return x  # 결과 값 반환



