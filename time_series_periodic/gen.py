import math
import random


def gen_point(i3, i4, i5, i6, i7, t):
    sum_point = 0
    for i in range(3, 8):
        x = {
            3: i3,
            4: i4,
            5: i5,
            6: i6,
            7: i7
        }

        sum_point = sum_point + 1 / math.pow(2, i) * math.sin(2 * math.pi * t * (math.pow(2, 2 + i) + x[i]))
    return sum_point


def gen_data(count,width=1):
    i3 = random.random() * math.pow(2, 3)
    i4 = random.random() * math.pow(2, 4)
    i5 = random.random() * math.pow(2, 5)
    i6 = random.random() * math.pow(2, 6)
    i7 = random.random() * math.pow(2, 7)

    return [gen_point(i3, i4, i5, i6, i7, i / count / width) for i in range(count)]
