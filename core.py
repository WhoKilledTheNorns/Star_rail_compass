import numpy as np
import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


max_state = [0, 6, 3, 2, 3, 6]


def main():
    A0, B0, C0 = 4, 4, 4
    A_step, B_step, C_step = 4, 2, 1
    # m0 = (A_step + At) + (C_step + Ct)
    # m1 = (B_step + Bt) + (C_step + Ct)
    # m2 = (B_step + Bt) + (A_step + At)
    for i in range(0, lcm(max_state[A_step], max_state[C_step])):
        for j in range(0, lcm(max_state[B_step], max_state[C_step])):
            for k in range(0, lcm(max_state[B_step], max_state[A_step])):
                At, Bt, Ct = (i + k) * A_step + A0, (j + k) * B_step + B0, (i + j) * C_step + C0
                if not (At % 6 or Bt % 6 or Ct % 6):
                    print(f'x={i}; y={j}; z={k}')


if __name__ == "__main__":
    main()