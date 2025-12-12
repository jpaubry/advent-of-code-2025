"""
Day 12 - Puzzle 1: [Puzzle Title]

[Brief description of the puzzle]
"""
import re

class Present:
    def __init__(self, my_id, my_shape):
        self.my_id = my_id
        self.my_shape = my_shape

        self.min_size = sum(s.count("#") for s in my_shape)


    def nice_print(self):
        print("my_id: " + str(self.my_id))
        for line in self.my_shape:
            print(line)

    def get_min_size(self):
        return self.min_size

def parse_input(input_data: str):
    """
    Parse the input data into a usable format.

    Args:
        input_data: Raw input string from file

    Returns:
        Parsed data structure (list, dict, etc.)
    """
    lines = input_data.strip().split('\n')

    regions = []
    box_id = -1
    my_boxes = {}
    presents = {}

    # Implement parsing logic
    for line in lines:
        my_match = re.search(r'^(\d+)x(\d+):\s(.*)', line)
        if my_match: # section section of the input
            my_surface = (int(my_match.group(1)), int(my_match.group(2)))
            my_target = [int(counter) for counter in my_match.group(3).split(' ')]
            my_region = {"surface":my_surface, "target":my_target}
            regions.append(my_region)
        else:
            if line == "":
                box_id = -1
            else:
                my_match2 = re.search(r'^(\d):', line)
                if my_match2:
                    box_id = int(my_match2.group(1))
                    my_boxes[box_id] = []
                else:
                    my_boxes[box_id].append(line)
    for id in my_boxes.keys():
        presents[id] = Present(id, my_boxes[id])

    return {"presents": presents, "regions": regions}

def easy_discard(my_region, my_presents):
    my_surface = my_region["surface"][0] * my_region["surface"][1]

    min_occupied = 0
    for index in range(0, len(my_region["target"])):
        min_occupied += my_presents[index].get_min_size() * my_region["target"][index]

    # print("my surface: " + str(my_surface) + ". min_occupied: " + str(min_occupied))

    return my_surface < min_occupied

def easy_validate(my_region):
    present_side = 3
    my_surface = (3 * (my_region["surface"][0] // 3)) * (3 * (my_region["surface"][1] // 3))
    max_occupied = 0
    for index in range(0, len(my_region["target"])):
        max_occupied += 9 * my_region["target"][index]

    # print("my surface: " + str(my_surface) + ". max_occupied: " + str(max_occupied))
    return my_surface >= max_occupied


def solve(input_data: str):
    """
    Main solution function.

    Args:
        input_data: Raw input string from file

    Returns:
        The puzzle answer
    """
    data = parse_input(input_data)

    my_regions = data["regions"]
    my_presents = data["presents"]

    # for present in my_presents.values():
    #     present.nice_print()
    #     print("")
    # exit(0)

    nb_presents = len(data["presents"].keys())

    # Implement solution logic
    easy_discarded = 0
    easy_validated = 0
    i_have_to_code = 0
    for region in my_regions:
        if easy_discard(region, my_presents):
            easy_discarded += 1

        else:
            if easy_validate(region):
                easy_validated += 1
            else: i_have_to_code += 1

    # print(easy_discarded)
    # print(easy_validated)
    # print(i_have_to_code)

    if i_have_to_code:
        return "I have to code"
    else:
        return easy_validated


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
