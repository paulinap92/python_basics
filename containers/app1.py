# Write a function that takes a list of tuples. Each tuple contains two elements:
# a string and a list of integers.
# The function should return a dictionary where the key is the upper string (the first element of the tuple),
# and the value is a list containing the sum of the numbers
# and the maximum value in the list (the second element of the tuple).

"""
INPUT:
[
    ("a", [10, 20, 30]),
    ("b", [10, 50, 30]),
]

OUTPUT:
{
    "A": [60,30]
    "B": [90,50]
}
"""

from typing import Callable, Any

def convert(data: list[tuple[str,list[int]]]) -> dict:
    return dict([(pair[0], [sum(pair[1]), max(pair[1])]) for pair in data])

def convert_flex(data: list[tuple[str, list[int]]], key_action_fn: Callable[[str], Any], value_action_fn: Callable[[list[int]], Any]) -> dict:
    return dict([(key_action_fn(pair[0]), value_action_fn(pair[1])) for pair in data])

def my_value_function(value: list[int])->list[int]:
    return [sum(value), max(value)]

def main() -> None:
    data = [
        ("a", [10, 20, 30]),
        ("b", [10, 50, 30]),
    ]

    print(convert_flex(data, lambda key: key.upper(), lambda value: my_value_function(value)))


if __name__ == '__main__':
    main()
