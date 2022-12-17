from typing import Dict, Tuple
from collections import Counter
from pprint import pprint


__all__ = ('print_content', 'print_sum')


INDENT_SIZE = 75


def print_content(data: Tuple[str, str, Dict]) -> None:
    print(f'{"=":=^{INDENT_SIZE}}\n{data[0]:^{INDENT_SIZE}}\n{"=":=^{INDENT_SIZE}}')
    print('# Structure:')
    print(data[1], end='')
    print('# Basic components quantity:')
    pprint(data[2])


def print_sum(*args) -> None:
    result = Counter()
    for el in args:
        result.update(el[2])
    # print(f'{"SUM":-^{len(str(dict(result)))}}\n{dict(result)}')
    print(f'{"SUM":-^{INDENT_SIZE}}')
    pprint(dict(result))
