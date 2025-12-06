"""
Day 6 - Puzzle 2: [Puzzle Title]

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

    # Implement parsing logic
    my_input = []
    my_operands = []

    my_operations = re.sub(r'\s+', ' ', lines[-1]).split()
    lines.pop()

    max_columns = 0
    for line in lines:
        if len(line) > max_columns:
            max_columns = len(line)

    operation_inc = 0
    columns = []
    counter = 0
    my_operands.append([])

    for inc in range(0,max_columns):
        new_operand = ""
        for line in lines:
            if inc > len(line) - 1:
                new_operand += " "
            else:
                new_operand += line[inc]
        new_operand = re.sub(r'\s+', '', new_operand)

        if new_operand == "":
            counter += 1
            my_operands.append([])
        else:
            my_operands[counter].append(new_operand)

    return {"operands":my_operands, "operations":my_operations}


def solve(input_data: str):
    """
    Main solution function.

    Args:
        input_data: Raw input string from file

    Returns:
        The puzzle answer
    """
    data = parse_input(input_data)

#    print(data["operands"])
    result = 0

    for inc in range(0,len(data["operations"])):
        if data["operations"][inc] == "+":
            calculus = 0
            for operand in data["operands"][inc]:
                calculus += int(operand)
        else:
            calculus = 1
            for operand in data["operands"][inc]:
                calculus *= int(operand)

        result += calculus

    return result


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
