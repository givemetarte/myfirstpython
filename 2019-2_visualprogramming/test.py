#hello.py
"""
작성자: 박하람
작성일: 2019-09-19
기능: 화면출력
"""

#실습2
print(1234567890 * 98765432109876543210)
print(0xAA + 55)

print(1/3 + 1/3 + 1/3)
print(0.1 + 0.1 + 0.1)

a = 1.2 * 3.4 * 5.6 * 7.8
b = int(1.2 * 3.4 * 5.6 * 7.8)
c = a - b
print(b)
print(c)
print(0.0000000001234 * 9876)

#실습3
print( ((1000 % 99) % 8) % 5)
print(4**4**4 + 3**3 + 2)

from fractions import Fraction
print(Fraction ( 3**4, 5**-2 ) )

print(137%7)

import math
print( math.pi * 1000) / 1000)
