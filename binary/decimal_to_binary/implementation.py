from __future__ import annotations

MARK_BINARY = '0b'
EMPTY_BINARY = ''

def decimal_to_binary(decimal: int) -> str:
    binary = EMPTY_BINARY

    while(decimal):
        binary = push_left(decimal % 2, binary)
        decimal = decimal // 2

    return f'{MARK_BINARY}{binary}'


def push_left(left: int, right: str) -> str:
    return str(left) + right
