"""
Day 11 - Puzzle 1: [Puzzle Title]

[Brief description of the puzzle]
"""

import re


def parse_input(input_data: str):
    """
    Parse the input data into a usable format.

    Args:
        input_data: Raw input string from file

    Returns:
        Parsed data structure (list, dict, etc.)
    """
    lines = input_data.strip().split('\n')

    server_rack = {}

    # Implement parsing logic
    for line in lines:
        #my_match = re.match(r'\[(.*)\](\s\([\d,]+\)]+)\s\{(.*)\}', line)
        my_match = re.match(r'(.*):\s(.*)', line)
        if my_match:
            server_rack[my_match.group(1)] = []
            for output in my_match.group(2).split(' '):
                server_rack[my_match.group(1)].append(output)

    return server_rack

def rec_count_path(my_device, my_server_rack):
    if my_device == "out":
        return 1
    else:
        nb_path = 0
        for next_device in my_server_rack[my_device]:
            nb_path += rec_count_path(next_device, my_server_rack)
        return nb_path

def solve(input_data: str):
    """
    Main solution function.

    Args:
        input_data: Raw input string from file

    Returns:
        The puzzle answer
    """
    data = parse_input(input_data)

    print(data)
    result = rec_count_path("you", data)

    return result


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None  # : Set expected result from puzzle

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
