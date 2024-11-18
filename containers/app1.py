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

from typing import Callable, Any, List, Tuple, Dict

def convert(data: List[Tuple[str, List[int]]]) -> Dict[str, List[int]]:
    """Converts a list of tuples into a dictionary.

    Each tuple contains a string and a list of integers. The function
    returns a dictionary where:
        - The key is the string converted to uppercase.
        - The value is a list containing:
            1. The sum of the integers.
            2. The maximum value from the list of integers.

    Args:
        data (List[Tuple[str, List[int]]]):
            A list of tuples. Each tuple consists of:
                - A string (key).
                - A list of integers.

    Returns:
        Dict[str, List[int]]:
            A dictionary where keys are uppercase strings and values
            are lists containing the sum and the maximum of the integers.
    """
    return dict([(pair[0].upper(), [sum(pair[1]), max(pair[1])]) for pair in data])


def convert_flex(
    data: List[Tuple[str, List[int]]],
    key_action_fn: Callable[[str], Any],
    value_action_fn: Callable[[List[int]], Any]
) -> Dict[Any, Any]:
    """A flexible function to transform a list of tuples into a dictionary.

    Allows customization of how keys and values are processed through
    user-provided functions.

    Args:
        data (List[Tuple[str, List[int]]]):
            A list of tuples. Each tuple consists of:
                - A string (key).
                - A list of integers (value).
        key_action_fn (Callable[[str], Any]):
            A function to process the string key.
        value_action_fn (Callable[[List[int]], Any]):
            A function to process the list of integers.

    Returns:
        Dict[Any, Any]:
            A dictionary where keys and values are transformed according
            to `key_action_fn` and `value_action_fn`.
    """
    return dict([(key_action_fn(pair[0]), value_action_fn(pair[1])) for pair in data])


def my_value_function(value: List[int]) -> List[int]:
    """Processes a list of integers.

    Returns a list containing:
        1. The sum of the integers.
        2. The maximum value.

    Args:
        value (List[int]):
            A list of integers.

    Returns:
        List[int]:
            A list containing the sum and the maximum of the integers.
    """
    return [sum(value), max(value)]


def main() -> None:
    """Main function to demonstrate usage of `convert_flex`."""
    data = [
        ("a", [10, 20, 30]),
        ("b", [10, 50, 30]),
    ]

    print(convert_flex(data, lambda key: key.upper(), lambda value: my_value_function(value)))


if __name__ == '__main__':
    main()
