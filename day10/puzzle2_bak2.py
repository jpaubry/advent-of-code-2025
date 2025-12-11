"""
Day 10 - Puzzle 2: [Puzzle Title]

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

def reverse_button(my_joltage, my_button):
    my_new_joltage = []
    for inc in range(0, len(my_button)):
        if my_button[inc] == '1':
            my_new_joltage.append(my_joltage[inc] - 1)
        else:
            my_new_joltage.append(my_joltage[inc])
    return my_new_joltage

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

def get_button_affecting_one_counter(my_buttons):
    my_counters_affectation = {}

    for ind in range(0, len(my_buttons[0])):
        my_counters_affectation[ind] = []

    for button in my_buttons:
        for ind in range(0, len(button)):
            if button[ind] == '1':
                my_counters_affectation[ind].append(button)
    for counter_index in my_counters_affectation.keys():
        if len(my_counters_affectation[counter_index]) == 1:
            return counter_index, my_counters_affectation[counter_index][0]
    return -1, None

def check_joltages(my_joltages):
    for joltage in my_joltages:
        if joltage < 0:
            return False
    return True

def unique_list_of_lists(list_of_lists: list[list]) -> list[list]:
    """
    Finds unique inner lists by converting them to tuples, using a set
    to eliminate duplicates, and converting them back to lists.
    """

    # 1. Convert the list of lists into a set of tuples
    #    (list is unhashable; tuple is hashable)
    set_of_tuples = set(tuple(inner_list) for inner_list in list_of_lists)

    # 2. Convert the set of unique tuples back into a list of lists
    unique_lists = [list(t) for t in set_of_tuples]

    return unique_lists

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
    progress = 0
    data2 = [data[8]]

    for my_machine in data2:
        progress += 1
        print("Machine " + str(progress) + " / " + str(len(data)))
        my_machine.nice_print()

        target = [0] * len(my_machine.joltages)
        my_tries = [my_machine.joltages.copy()]

        nb_push = 0
        keep_pushing = True
        already_encountered = set()

        

        while keep_pushing:
            if nb_push % 10 == 0:
                print("Push: " + str(nb_push) + ". Remaining buttons: " + str(len(my_machine.buttons)))

            nb_push += 1
            my_new_tries = []

            # check if a counter is incremented by only 1 counter
            uniq_counter, special_button = get_button_affecting_one_counter(my_machine.buttons)
            if uniq_counter > -1:
                for my_try in my_tries:
                    if(my_try[uniq_counter] > -2):
                        my_new_try = reverse_button(my_try, special_button)
                        if check_joltages(my_new_try) and tuple(my_new_try) not in already_encountered:
                            already_encountered.add(tuple(my_new_try))
                            my_new_tries.append(my_new_try)
                    else:
                        min_index = my_try.index(min(x for x in my_try if x != 0))
                        for button in my_machine.buttons:
                            # consider only button able to decrease the min
                            if button[min_index] == '1':
                                my_new_try = reverse_button(my_try, button)
                                if check_joltages(my_new_try) and tuple(my_new_try) not in already_encountered:
                                    already_encountered.add(tuple(my_new_try))
                                    my_new_tries.append(my_new_try)

            else:
                for my_try in my_tries:
                    min_index = my_try.index(min(x for x in my_try if x != 0))
                    for button in my_machine.buttons:
                        # consider only button able to decrease the min
                        if button[min_index] == '1':
                            my_new_try = reverse_button(my_try, button)
                            if check_joltages(my_new_try) and tuple(my_new_try) not in already_encountered:
                                already_encountered.add(tuple(my_new_try))
                                my_new_tries.append(my_new_try)

            # for my_try in my_tries:
            #     # check if a counter is incremented by only 1 counter that has still a non null value
            #     uniq_counter, special_button = get_button_affecting_one_counter(my_machine.buttons, my_try)
            #     if uniq_counter > -1:
            #         my_new_try = reverse_button(my_try, special_button)
            #         if check_joltages(my_new_try) and tuple(my_new_try) not in already_encountered:
            #             already_encountered.add(tuple(my_new_try))
            #             my_new_tries.append(my_new_try)
            #     else:
            #         min_index = my_try.index(min(x for x in my_try if x != 0))
            #         for button in my_machine.buttons:
            #             # consider only button able to decrease the min
            #             if button[min_index] == '1':
            #                 my_new_try = reverse_button(my_try, button)
            #                 if check_joltages(my_new_try) and tuple(my_new_try) not in already_encountered:
            #                     already_encountered.add(tuple(my_new_try))
            #                     my_new_tries.append(my_new_try)
            #
            # my_tries = unique_list_of_lists(my_new_tries)


            my_tries = unique_list_of_lists(my_new_tries)
            #print(my_tries)
            #print(my_machine.buttons)

            if my_tries:
                # check if we pushed enough
                for my_try in my_tries:
                    if my_try == target:
                        keep_pushing = False
                        print(nb_push)
                        result = result + nb_push
                        break

            # remove useless buttons
            if my_tries:
                for index in range(0,len(my_tries[0])):
                    if all(my_try[index] == 0 for my_try in my_tries):
                        new_machine_buttons = []
                        for button in my_machine.buttons:
                            if button[index] == '0':
                                new_machine_buttons.append(button)
                        my_machine.buttons = new_machine_buttons

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
