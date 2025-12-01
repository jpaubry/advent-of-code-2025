"""
Day 1 - Puzzle 2: [Puzzle Title]

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

    # TODO: Implement parsing logic
    # Example:
    # return [int(line) for line in lines]
    # return [[int(x) for x in line.split()] for line in lines]

    return lines

def rotate(position, direction, distance):
    click = 0

    while distance > 99:
        click += 1
        distance = distance - 100

    if direction == 'R':
        if position + distance > 99:
            return (click + 1, position + distance - 100)
        else:
            return (click, position + distance)
    else:
        if (position - distance == 0):
            return (click + 1, position - distance)
        elif (position - distance < 0):
            if position != 0:
                return (click + 1, position - distance + 100)
            else:
                return (click, position - distance + 100)
        else:
            return (click, position - distance)

def solve(input_data: str):
    """
    Main solution function.

    Args:
        input_data: Raw input string from file

    Returns:
        The puzzle answer
    """
    data = parse_input(input_data)

    # TODO: Implement solution logic
    rotations = []
    my_position = 50
    result = 0

    for l in data:
        l.rstrip('\n')
        action = rotate(my_position, l[0], int(l[1:]))
        result += action[0]
        my_position = action[1]
        #print(my_position, action[0])

    return result


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None  # TODO: Set expected result from puzzle

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
