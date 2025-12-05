"""
Day 5 - Puzzle 1: [Puzzle Title]

[Brief description of the puzzle]
"""

def parse_input(input_data: str):
    """
    Parse the input data into a usable format.

    Args:
        input_data: Raw input string from file

    Returns:
        Parsed data structure (list, dict, etc.)
    """
    lines = input_data.strip().split('\n')

    # Implement parsing logic

    my_ranges = []
    my_ingredients = []
    second_section = 0

    for line in lines:
        if line == '':
            second_section = 1
        elif second_section == 0:
            new_range = line.split('-')
            my_ranges.append([int(new_range[0]), int(new_range[1])])
        else:
            my_ingredients.append(int(line))

    return {'ranges': my_ranges, 'ingredients': my_ingredients}

def check_if_ranges(my_nb, my_ranges):
    for ranges in my_ranges:
        if my_nb >= ranges[0] and my_nb <= ranges[1]:
            return True
    return False

def solve(input_data: str):
    """
    Main solution function.

    Args:
        input_data: Raw input string from file

    Returns:
        The puzzle answer
    """
    data = parse_input(input_data)

    result = 0

    # Implement solution logic
#    print(data)
    for ingredient in data['ingredients']:
        if check_if_ranges(ingredient, data['ranges']):
            result += 1

    return result


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None  #Set expected result from puzzle

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
