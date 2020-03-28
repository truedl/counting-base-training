from __future__ import annotations
import math

EMPTY_DECIMAL = 0

def binary_to_decimal(binary: str) -> int:
    decimal = EMPTY_DECIMAL

    for index, num in enumerate([int(x) for x in binary][::-1]):
        decimal += num * math.pow(2, index)

    return decimal
