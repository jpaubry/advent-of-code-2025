"""
Day 8 - Puzzle 2: [Puzzle Title]

[Brief description of the puzzle]
"""
import math

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
    # retrieve coordinate and compute distances now

    distances = {}
    junction_boxes = {}
    circuits = {}

    circuit_id = 0

    for line in lines:
        my_coordinates = line.split(',')
        my_x = int(my_coordinates[0])
        my_y = int(my_coordinates[1])
        my_z = int(my_coordinates[2])

        for my_box in junction_boxes.keys():
            if math.dist((my_x, my_y, my_z), my_box) in distances:
                print("EDGE CASE ERROR: SAME DISTANCE TWICE, WORK WIH LISTS")
                exit(1)
            distances[math.dist((my_x, my_y, my_z), my_box)] = ((my_x, my_y, my_z), my_box)
        junction_boxes[(my_x,my_y,my_z)] = circuit_id
        circuits[circuit_id] = [(my_x,my_y,my_z)]
        circuit_id += 1

    return {"distances": distances, "junction_boxes": junction_boxes, "circuits": circuits}


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
    last_box1 = (0,0,0)
    last_box2 = (0,0,0)

    my_distances = list(data["distances"].keys())
    my_distances.sort()
    my_distances.reverse()

    while len(data["circuits"]) > 1:
        my_distance = my_distances[-1]
        my_box1 = data["distances"][my_distance][0]
        my_box2 = data["distances"][my_distance][1]
        last_box1 = my_box1
        last_box2 = my_box2

        my_circuit_id1 = data["junction_boxes"][my_box1]
        my_circuit_id2 = data["junction_boxes"][my_box2]

        if my_circuit_id1 != my_circuit_id2:
            for box in data["circuits"][my_circuit_id2]:
                # transfer boxes from circuit2 to circuit1
                data["junction_boxes"][box] = my_circuit_id1
                data["circuits"][my_circuit_id1].append(box)
            # circtuit2 is empty, so delete it
            data["circuits"].pop(my_circuit_id2)

        my_distances.pop()

    print(last_box1, last_box2)
    return last_box1[0] * last_box2[0]


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
