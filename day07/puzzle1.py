"""
Day 7 - Puzzle 1: [Puzzle Title]

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
    my_manifold = {}

    # Implement parsing logic
    my_line_nb = 0
    for line in lines:
        for inc in range(0, len(line)):
            if line[inc] == 'S':
                my_start = (my_line_nb, inc)
            my_manifold[(my_line_nb, inc)] = line[inc]
        my_line_nb += 1

    return {"start": my_start, "manifold": my_manifold, "exit":my_line_nb}


def solve(input_data: str):
    """
    Main solution function.

    Args:
        input_data: Raw input string from file

    Returns:
        The puzzle answer
    """
    data = parse_input(input_data)

#    print(data)

    # Implement solution logic

    result = 0
    my_beams = set()
    my_beams.add(data["start"])
    my_depth = data["start"][0]
    my_manifold = data["manifold"]

    while my_depth < data["exit"]-1:
#        print("---------------------------")
#        print(my_depth)
#        print(my_beams)
        my_new_beams = set()
        my_depth += 1
        for beam in my_beams:
            if my_manifold[(my_depth,beam[1])] == '.':
                my_new_beams.add((my_depth,beam[1]))
            else:
                my_new_beams.add((my_depth,beam[1]-1))
                my_new_beams.add((my_depth,beam[1]+1))
                result += 1
        my_beams = my_new_beams

    return result


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None  # Set expected result from puzzle

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
