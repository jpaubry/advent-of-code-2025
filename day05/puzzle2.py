"""
Day 5 - Puzzle 2: [Puzzle Title]

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

def check_if_overlap(my_range, my_ranges):
    if len(my_ranges) == 0:
        return -1
    my_index = 0
    for range in my_ranges:
        if my_range[0] >= range[0] and my_range[0] <= range[1]:
            return my_index
        if my_range[1] >= range[0] and my_range[1] <= range[1]:
            return my_index
        if my_range[0] <= range[0] and my_range[1] >= range[1]:
            return my_index
        my_index += 1
    return -1

def remove_overlap(my_range, my_ranges, my_index):
    if my_range[0] < my_ranges[my_index][0]:
        my_ranges[my_index][0] = my_range[0]
    if my_range[1] > my_ranges[my_index][1]:
        my_ranges[my_index][1] = my_range[1]

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

    ranges_without_overlap = []

    for range in data['ranges']:
        my_index = check_if_overlap(range, ranges_without_overlap)
        while my_index > -1:
            remove_overlap(range, ranges_without_overlap, my_index)
            range[0] = ranges_without_overlap[my_index][0]
            range[1] = ranges_without_overlap[my_index][1]
            ranges_without_overlap.pop(my_index)
            my_index = check_if_overlap(range, ranges_without_overlap)

        ranges_without_overlap.append(range)

    print(ranges_without_overlap)

    for range in ranges_without_overlap:
        result += (range[1] - range[0] + 1)
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
