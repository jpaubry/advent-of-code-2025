"""
Day 4 - Puzzle 1: [Puzzle Title]

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

    my_matrix = {}
    my_nb_lines = 0
    my_nb_columns = 0

    for line in lines:
        line.rstrip('\n')
        my_nb_columns = len(line)
        counter = 0
        for character in list(line):
            my_matrix[(my_nb_lines, counter)] = character
            counter += 1
        my_nb_lines += 1

    resp = {
        "nb_lines": my_nb_lines,
        "nb_columns": my_nb_columns,
        "matrix": my_matrix
    }

    return resp

    # Implement parsing logic
    # Example:
    # return [int(line) for line in lines]
    # return [[int(x) for x in line.split()] for line in lines]

    return lines

#  1    2    3
#  4   x,y   5
#  6    7    8

def check1(x, y, d):
    if x == 0:
        return 0
    if y == 0:
        return 0
    if d["matrix"][(x-1, y-1)] == '.':
        return 0
    return 1

def check2(x, y, d):
    if x == 0:
        return 0
    if d["matrix"][(x-1, y)] == '.':
        return 0
    return 1

def check3(x, y, d):
    if x == 0:
        return 0
    if y == d["nb_columns"] - 1:
        return 0
    if d["matrix"][(x-1, y+1)] == '.':
        return 0
    return 1

def check4(x, y, d):
    if y == 0:
        return 0
    if d["matrix"][(x, y-1)] == '.':
        return 0
    return 1

def check5(x, y, d):
    if y == d["nb_columns"] - 1:
        return 0
    if d["matrix"][(x, y+1)] == '.':
        return 0
    return 1

def check6(x, y, d):
    if x == d["nb_lines"] - 1:
        return 0
    if y == 0:
        return 0
    if d["matrix"][(x+1, y-1)] == '.':
        return 0
    return 1

def check7(x, y, d):
    if x == d["nb_lines"] - 1:
        return 0
    if d["matrix"][(x+1, y)] == '.':
        return 0
    return 1

def check8(x, y, d):
    if x == d["nb_lines"] - 1:
        return 0
    if y == d["nb_columns"] - 1:
        return 0
    if d["matrix"][(x+1, y+1)] == '.':
        return 0
    return 1

def checkAll(x,y,d):
    return check1(x, y, d) + check2(x, y, d) + check3(x, y, d) + \
        check4(x, y, d) + check5(x, y, d) + check6(x, y, d) + \
        check7(x, y, d) + check8(x, y, d)

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

    check_mat = ""
    #print(data)

    # Implement solution logic
    for i in range(0, data["nb_lines"]):
        for j in range(0, data["nb_columns"]):
            check_mat += data["matrix"][(i, j)]
            if data["matrix"][(i, j)] == '@':
                if checkAll(i, j, data) < 4:
                    check_mat = check_mat[:-1]
                    check_mat += "x"
                    result += 1
        #check_mat += "\n"

    print(check_mat)

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
