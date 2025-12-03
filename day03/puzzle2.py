"""
Day 3 - Puzzle 2: [Puzzle Title]

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
    # Example:
    # return [int(line) for line in lines]
    # return [[int(x) for x in line.split()] for line in lines]

    return lines


def solve(input_data: str):
    """
    Main solution function.

    Args:
        input_data: Raw input string from file

    Returns:
        The puzzle answer
    """
    data = parse_input(input_data)

    # Implement solution logic
    result = 0
    run_power = 12

    for line in data:
        line.rstrip('\n')
        my_batteries = list(line)
        bank_joltage = 0

        my_power = run_power
#        print("###################")
#        print(my_batteries)

        while my_power > 0:
            my_power = my_power - 1
            if my_power > 0:
                my_batteries_set = my_batteries[:-my_power]
            else:
                my_batteries_set = my_batteries
 #           print(my_batteries_set)

            my_nb = 9
            nb_not_found = True

            while nb_not_found:
                if (str(my_nb) in my_batteries_set):
                    nb_not_found = False
                else:
                    my_nb = my_nb - 1
            my_batteries = my_batteries[my_batteries.index(str(my_nb))+1:]
            bank_joltage = bank_joltage + my_nb * (10 ** my_power)

        print(bank_joltage)

        result += bank_joltage

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
