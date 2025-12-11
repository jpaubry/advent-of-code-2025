"""
Day 10 - Puzzle 1: [Puzzle Title]

[Brief description of the puzzle]
"""

import re

class Machine:
    def __init__(self, lights: str , buttons: list, joltages: list):
        self.lights = lights
        self.buttons = buttons.copy()
        self.joltages = joltages.copy()

    def nice_print(self):
        print("Lights indicator: " + self.lights)
        print("Buttons: " + str(self.buttons))
        print("Joltage: " + str(self.joltages))


def activate_button(my_light, my_button):
    my_size = len(my_light)
    my_light_b = int(my_light, 2)
    my_button_b = int(my_button, 2)

    new_light = my_light_b ^ my_button_b
    return format(new_light, f'0{my_size}b')


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

    my_machines = []

    for line in lines:
        #my_match = re.match(r'\[(.*)\](\s\([\d,]+\)]+)\s\{(.*)\}', line)
        my_match = re.match(r'\[(.*)\]\s(.*)\s\{(.*)\}', line)
        if my_match:
            my_lights_len = len(my_match.group(1))
            my_lights = ""
            for light in my_match.group(1):
                if light == '#':
                    my_lights += '1'
                else:
                    my_lights += '0'

            my_buttons = []
            for button_action in my_match.group(2).split(' '):
                my_button = '0' * my_lights_len
                my_match2 = re.match(r'\((.*)\)', button_action)
                if my_match2:
                    for light_switch in my_match2.group(1).split(','):
                        my_button = my_button[:int(light_switch)] + '1' + my_button[int(light_switch)+1:]
                else:
                    print("THERE IS A BUG")
                my_buttons.append(my_button)

            my_joltages = []
            for joltage in my_match.group(3).split(','):
                my_joltages.append(int(joltage))

            my_machines.append(Machine(my_lights, my_buttons, my_joltages))

    return my_machines


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
    for my_machine in data:
        my_machine.nice_print()

        my_tries = my_machine.buttons.copy()
        nb_push = 0
        keep_going = True

        while keep_going:
            nb_push += 1
            new_tries = []
            for my_try in my_tries:
                if my_try == my_machine.lights:
                    result += nb_push
                    print(nb_push)
                    print("###########")
                    keep_going = False
                    break
                else:
                    for button in my_machine.buttons:
                        new_tries.append(activate_button(my_try, button))
            my_tries = new_tries

    return result


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None  # Set expected result from puzzle
    # add

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
