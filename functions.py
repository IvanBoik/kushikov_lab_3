import logging

logger = logging.getLogger('uvicorn.error')


def pend(x, t, faks, xm):
    S = lambda: fx(t, faks[0])
    F = lambda: fx(t, faks[1])
    G = lambda: fx(t, faks[2])
    T = lambda: fx(t, faks[3])
    A = lambda: fx(t, faks[4])
    D = lambda: fx(t, faks[5])
    I = lambda: fx(t, faks[6])
    P = faks[7][3]
    C = faks[8][3]
    logger.info(x, t, faks, xm)
    dkdt = [
        # 0
        (
                (1 / xm[0]) * f1s(S()) * f1x8(x)
        ),

        # 1
        (
                (1 / xm[1]) * F() * G() * f2s(S()) * f2x8(x) - f2x1(x) * f2x7(x)
        ),

        # 2
        (
                (1 / xm[2]) * f3x8(x) * f3x1(x)
        ),

        # 3
        (
                (1 / xm[3]) * F() * G() * T() * f4x8(x) * f4x7(x) * f4x1(x)
        ),

        # 4
        (
                (1 / xm[4]) * A() * f5s(S()) - f5x1(x) * f5x7(x)
        ),

        # 5
        (
                (1 / xm[5]) * f6s(S()) * f6x8(x)
        ),

        # 6
        (
                (1 / xm[6]) * f7x1(x)
        ),

        # 7
        (
                (1 / xm[7]) * D() * f8s(S()) - f8x4(x)
        ),

        # 8
        (
                (1 / xm[8]) * I() * f9s(S()) - f9x1(x) * f9x7(x)
        ),

        # 9
        (
                (1 / xm[9]) * F() * G() * T() * f10s(S()) * f10x1(x) * f10x7(x)
        ),

        # 10
        (
                (1 / xm[10]) * P * C * F() * G() * D() * f11s(S()) * f11x6(x)
        ),

        # 11
        (
                (1 * xm[11]) * f12x11(x)
        )
    ]
    return dkdt


def fx(x, params):
    return params[0] * x ** 3 + params[1] * x ** 2 + params[2] * x + params[3]


def f1s(s):
    return 0.001 * s ** 3 - 0.04 * s ** 2 + 0.6 * s - 2.1


def f1x8(t):
    x = x8(t)
    return 54 * x ** 4 - 137 * x ** 3 + 103.4 * x ** 2 - 20.7 * x + 1.9


def f2s(s):
    return -0.02 * s ** 3 + 0.64 * s ** 2 - 6.4 * s + 21


def f2x8(t):
    x = x8(t)
    return -14.5 * x ** 2 + 22.5 * x - 3.3


def f2x1(t):
    x = x1(t)
    return 0.573 * x ** 2 + 0.276 * x + 0.046


def f2x7(t):
    x = x7(t)
    return -3.335 * x ** 2 + 5.6 * x - 0.126


def f3x8(t):
    x = x8(t)
    return 3.276 * x ** 2 - 23.31 * x + 12.3


def f3x1(t):
    x = x1(t)
    return -1.257 * x ** 2 + 10.1 * x - 17.8


def f3x7(t):
    x = x7(t)
    return -0.328 * x ** 2 + 2.2 * x - 0.26


def f4x8(t):
    x = x8(t)
    return -1.3 * x ** 4 + 1.92 * x ** 3 - 0.95 * x ** 2 + 0.3 * x + 0.7


def f4x7(t):
    x = x7(t)
    return -0.42 * x ** 4 - 7.2 * x ** 3 + 19.34 * x ** 2 - 15.1 * x + 4.435


def f4x1(t):
    x = x1(t)
    return x ** 3 - x ** 2 + 1.5 * x + 0.02


def f5s(s):
    return 0.01 * s ** 2 - 0.1 * s + 0.5


def f5x1(t):
    x = x1(t)
    return 0.217 * x ** 2 - 0.505 * x + 0.31


def f5x7(t):
    x = x7(t)
    return -0.304 * x ** 2 + 1.1 * x + 0.26


def f6s(s):
    return 0.002 * s ** 2 + 0.056 * s + 0.48


def f6x8(t):
    x = x8(t)
    return -0.05 * x ** 3 + 0.9 * x ** 2 - 0.02 * x + 0.23


def f7x1(t):
    x = x1(t)
    return 3.5 * x ** 3 - 5.3 * x ** 2 + 3.27 * x + 0.0003


def f8s(s):
    return 0.18 * s ** 3 - 0.06 * s ** 2 + 0.77 * s - 1.77


def f8x4(t):
    x = x4(t)
    return 2.17 * x ** 2 - 0.0024 * x + 0.16


def f9s(s):
    return 0.002 * s ** 2 + 0.07 * s + 0.5


def f9x1(t):
    x = x1(t)
    return 0.43 * x ** 3 - 2.3 * x ** 2 + 3.2 * x - 0.07


def f9x7(t):
    x = x7(t)
    return 1.15 * x ** 3 - 1.78 * x ** 2 + 0.93 * x - 0.024


def f10s(s):
    return -0.0007 * s ** 4 + 0.03 * s ** 3 - 0.46 * s ** 2 + 2 * s - 0.4


def f10x1(t):
    x = x1(t)
    return 0.25 * x ** 3 - 1.24 * x ** 2 + 0.04 * x - 0.049


def f10x7(t):
    x = x7(t)
    return 10.9 * x ** 3 - 26.57 * x ** 2 + 16.7 * x - 0.515


def f11s(s):
    return -0.0005 * s ** 3 + 0.02 * s ** 2 - 0.01 * s + 0.4


def f11x6(t):
    x = x6(t)
    return -3.5 * x ** 3 + 7.8 * x ** 2 - 2.7 * x + 0.25


def f12x11(t):
    x = x11(t)
    return -45.3 * x ** 4 + 111.95 * x ** 3 - 84.07 * x ** 2 + 20.04


def x1(t):
    return fx1(t[0])


def x2(t):
    return fx2(t[1])


def x3(t):
    return fx3(t[2])


def x4(t):
    return fx4(t[3])


def x5(t):
    return fx5(t[4])


def x6(t):
    return fx6(t[5])


def x7(t):
    return fx7(t[6])


def x8(t):
    return fx8(t[7])


def x9(t):
    return fx9(t[8])


def x10(t):
    return fx10(t[9])


def x11(t):
    return fx11(t[10])


def x12(t):
    return fx12(t[11])


def fx1(t):
    return 0.001 * t ** 3 + 0.0665 * t ** 2 - 0.0345 * t - 0.008


def fx2(t):
    return -0.0536 * t ** 3 + 0.4455 * t ** 2 - 0.786 * t + 0.447


def fx3(t):
    return -0.011 * t ** 3 + 0.151 * t ** 2 - 0.14 * t + 0.25


def fx4(t):
    return 0.0923 * t ** 3 - 0.859 * t ** 2 + 2.6156 * t - 1.849


def fx5(t):
    return -0.04 * t ** 3 + 0.288 * t ** 2 - 0.187 * t + 0.239


def fx6(t):
    return -0.0063 * t ** 3 + 0.104 * t ** 2 + 0.107 * t + 0.045


def fx7(t):
    return 0.03 * t ** 3 - 0.032 * t ** 2 + 0.01 * t + 0.023


def fx8(t):
    return 0.0132 * t ** 3 - 0.0245 * t ** 2 + 0.245 * t - 0.067


def fx9(t):
    return -0.009 * t ** 3 + 0.1115 * t ** 2 - 0.06 * t - 0.038


def fx10(t):
    return 0.16 * t ** 3 - 1.5 * t ** 2 + 4.57 * t - 3.23


def fx11(t):
    return 0.004 * t ** 3 + 0.01 * t ** 2 + 0.21 * t - 0.22


def fx12(t):
    return 0.034 * t ** 3 - 0.127 * t ** 2 + 0.24 * t - 0.145
