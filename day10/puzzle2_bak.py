"""
Day 10 - Puzzle 2: [Puzzle Title]

[Brief description of the puzzle]
"""
import math
import re
from typing import List

#help from Claude
from collections import deque


def find_minimum_presses(buttons, target):
    """
    buttons: list of strings, e.g. ["101", "011", "110"]
             where '1' means increment that counter, '0' means no change
    target: list of integers, e.g. [5, 3, 2]
    """
    n_counters = len(target)
    start = tuple([0] * n_counters)
    target_tuple = tuple(target)

    if start == target_tuple:
        return 0

    queue = deque([(start, 0)])  # (state, num_presses)
    visited = {start}

    while queue:
        state, presses = queue.popleft()

        # Try pressing each button
        for button_str in buttons:
            # Calculate new state by adding where button has '1'
            new_state = tuple(
                state[i] + int(button_str[i])
                for i in range(n_counters)
            )

            # CRITICAL: Prune if any counter exceeds target
            if any(new_state[i] > target_tuple[i] for i in range(n_counters)):
                continue

            # Check if we've reached target
            if new_state == target_tuple:
                return presses + 1

            # Add to queue if not visited
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

    return -1  # No solution found


from collections import deque


def find_minimum_presses_backward(buttons, target):
    """
    BFS working backwards from target to (0,0,0,...)
    """
    button_increments = [
        tuple(int(c) for c in button_str)
        for button_str in buttons
    ]

    target_tuple = tuple(target)
    goal = tuple([0] * len(target))

    if target_tuple == goal:
        return 0

    queue = deque([(target_tuple, 0)])
    visited = {target_tuple}

    while queue:
        state, presses = queue.popleft()

        # Try "un-pressing" each button (subtract increments)
        for button in button_increments:
            new_state = tuple(state[i] - button[i] for i in range(len(state)))

            # Pruning: can't go negative
            if any(new_state[i] < 0 for i in range(len(state))):
                continue

            # Check if reached start
            if new_state == goal:
                return presses + 1

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

    return -1

#end of help

class Machine:
    def __init__(self, lights: str , buttons: list, joltages: list):
        self.lights = lights
        self.buttons = buttons.copy()
        self.joltages = joltages.copy()

    def nice_print(self):
        print("Lights indicator: " + self.lights)
        print("Buttons: " + str(self.buttons))
        print("Joltage: " + str(self.joltages))


def activate_button(my_joltage, my_button):
    my_new_joltage = []
    for inc in range(0, len(my_button)):
        if my_button[inc] == '1':
            my_new_joltage.append(my_joltage[inc] + 1)
        else:
            my_new_joltage.append(my_joltage[inc])
    return my_new_joltage


def reverse_button(my_joltage, my_button):
    my_new_joltage = []
    for inc in range(0, len(my_button)):
        if my_button[inc] == '1':
            my_new_joltage.append(my_joltage[inc] - 1)
        else:
            my_new_joltage.append(my_joltage[inc])
    return my_new_joltage

def check_joltages(my_joltages):
    for joltage in my_joltages:
        if joltage < 0:
            return False
    return True

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


def sort_list_by_sum(data: List[List[int]], reverse_order: bool = False) -> List[List[int]]:
    """
    Orders a list of lists of integers based on the sum of elements in each inner list.

    Args:
        data: The list of lists to be sorted.
        reverse_order: If True, sorts from largest sum to smallest sum.
                       If False (default), sorts from smallest sum to largest sum.

    Returns:
        A new list of lists, sorted by the sum of their elements.
    """

    # Use the sorted() function with 'sum' as the key function.
    sorted_list = sorted(
        data,
        key=sum,  # Key: For any list 'x' in 'data', use sum(x) for comparison
        reverse=reverse_order
    )

    return sorted_list

def best_index(my_joltage, my_buttons):
    best_score = len(my_buttons) + 1
    my_best_index = 0
    for ind in range(0, len(my_joltage)):
        if my_joltage[ind] == 0:
            continue
        score = 0
        for button in my_buttons:
            if button[ind] == '1':
                score += 1
        if score < best_score:
            best_score = score
            best_index = ind
    return best_index

def rec_how_many_push(my_joltage, my_buttons, encountered_joltages):
    if tuple(my_joltage) in encountered_joltages:
        return encountered_joltages[tuple(my_joltage)]

    joltage_sum = 0
    for ind in range(0, len(my_joltage)):
        if my_joltage[ind] == -1:
            return -1
        else:
            joltage_sum += my_joltage[ind]

    if joltage_sum == 0:
        return 0
    else:
        my_pushes = []
        for button in my_buttons:
            my_new_joltage = reverse_button(my_joltage, button)
            new_push = rec_how_many_push(my_new_joltage, my_buttons, encountered_joltages)
            if new_push != -1:
                my_pushes.append(new_push + 1)
        if my_pushes:
            #print(my_pushes)
            encountered_joltages[tuple(my_joltage)] = min(my_pushes)
            return min(my_pushes)
        else:
            encountered_joltages[tuple(my_joltage)] = -1
            return -1


from collections import deque


def find_minimum_presses_clean(buttons, target):
    """
    Clean backward BFS without aggressive pruning
    """
    n = len(target)
    target_tuple = tuple(target)
    goal = tuple([0] * n)

    if target_tuple == goal:
        return 0

    queue = deque([(target_tuple, 0)])
    visited = {target_tuple}

    while queue:
        state, presses = queue.popleft()

        # Try every button (don't filter by "best index")
        for button in buttons:
            # Subtract button effect
            new_state = tuple(
                state[i] - int(button[i])
                for i in range(n)
            )

            # Only prune if negative (invalid)
            if any(x < 0 for x in new_state):
                continue

            # Check if we reached the goal
            if new_state == goal:
                return presses + 1

            # Add to queue if not visited
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

    return -1  # No solution


def find_minimum_with_limit(buttons, target, max_presses=500):
    """
    BFS with depth limit to avoid infinite search
    """
    n = len(target)
    target_tuple = tuple(target)
    goal = tuple([0] * n)

    if target_tuple == goal:
        return 0

    queue = deque([(target_tuple, 0)])
    visited = {target_tuple}

    while queue:
        state, presses = queue.popleft()

        # Stop if too many presses
        if presses >= max_presses:
            continue

        for button in buttons:
            new_state = tuple(state[i] - int(button[i]) for i in range(n))

            if any(x < 0 for x in new_state):
                continue

            if new_state == goal:
                return presses + 1

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

    return -1


def find_minimum_with_constraints(buttons, target):
    """
    More sophisticated approach with backtracking
    """
    n_counters = len(target)
    button_effects = [[int(c) for c in b] for b in buttons]

    # Calculate theoretical minimum (if we could press fractional buttons)
    min_theoretical = max(target)  # At minimum, need this many presses

    # Use DFS with pruning
    def dfs(state, presses, depth):
        if depth > min_theoretical * 3:  # Prune if too deep
            return float('inf')

        if state == target:
            return presses

        if any(state[i] > target[i] for i in range(n_counters)):
            return float('inf')

        # Heuristic: how far from target?
        remaining = sum(max(0, target[i] - state[i]) for i in range(n_counters))
        if remaining == 0:
            return float('inf')

        min_presses = float('inf')

        # Try buttons in order of most helpful
        button_scores = []
        for i, button in enumerate(button_effects):
            score = sum(button[j] if state[j] < target[j] else 0
                        for j in range(n_counters))
            button_scores.append((score, i))

        button_scores.sort(reverse=True)

        for score, i in button_scores[:5]:  # Only try top 5 buttons
            if score == 0:
                break

            new_state = [state[j] + button_effects[i][j] for j in range(n_counters)]
            result = dfs(tuple(new_state), presses + 1, depth + 1)
            min_presses = min(min_presses, result)

        return min_presses

    start = tuple([0] * n_counters)
    result = dfs(start, 0, 0)

    return result if result != float('inf') else -1

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
    # 0: 80, 1: 243, 2: 99, 3: 25, 4: 198, 5: 55, 6: 77, 7: 169
    # algo too slow for 8
    # 9: 11, 10: 84, 11: 206, 12: 76, 13: 52, 14: 99, 15: 57, 16: 56, 17: 219, 18: 91, 19: 73, 20: 58, 21: 183, 22: 31,
    # algo too slow for 23
    # 24: 152, 25: 85, 26: 219, 27: 47, 28: 71, 29: 203, 30: 158, 31: 54, 32: 47, 33: 14, 34: 60, 35: 92, 36: 94, 37: 57, 38: 103, 39: 41, 40: 24, 41: 53
    # algo too slow for 42

    # Usage in your solve function:
    # for my_machine in data:
    #     print("Machine " + str(progress) + " / " + str(len(data)))
    #     my_machine.nice_print()
    #     progress += 1
    #
    #     nb_push = find_minimum_with_constraints(my_machine.buttons, my_machine.joltages)
    #     if nb_push != -1:
    #         print(f"Solution: {nb_push} pushes")
    #         result += nb_push
    #     else:
    #         print("No solution found!")

    for my_machine in data2:
        print("Machine " + str(progress) + " / " + str(len(data)))
        my_machine.nice_print()
        progress += 1
        nb_push = 0

        target = [0] * len(my_machine.joltages)

        my_tries = [my_machine.joltages.copy()]
        #parked_tries = {}

        keep_pushing = True

        already_encountered = set()

        while keep_pushing:

            # if not my_tries:
            #     nb_push = max(parked_tries.keys())
            #     if len(parked_tries[nb_push]) < 50000:
            #         my_tries = parked_tries[nb_push].copy()
            #         del parked_tries[nb_push]
            #     else:
            #         parked_tries[nb_push] = sort_list_by_sum(parked_tries[nb_push])
            #         my_tries = parked_tries[nb_push][:50000].copy()
            #         parked_tries[nb_push] = parked_tries[nb_push][50000:]

            nb_push += 1
            if nb_push % 10 == 0:
                print("Push: " + str(nb_push) + ". Remaining buttons: " + str(len(my_machine.buttons)))
            #print("   " + str(len(my_tries)) + "   " + str(len(already_encountered)))

            my_new_tries = []
            min_index = 0

            for my_try in my_tries:
                # retrieve index of min non-null joltage
                min_index = my_try.index(min(x for x in my_try if x != 0))
                #min_index = best_index(my_try, my_machine.buttons)

                for button in my_machine.buttons:
                    #consider only button able to decrease the min
                    if button[min_index] == '1':
                        my_new_try = reverse_button(my_try, button)
                        if check_joltages(my_new_try) and tuple(my_new_try) not in already_encountered:
                            already_encountered.add(tuple(my_new_try))
                            my_new_tries.append(my_new_try)

            my_tries = unique_list_of_lists(my_new_tries)

            if my_tries:
                # check if we pushed enough
                for my_try in my_tries:
                    if my_try == target:
                        keep_pushing = False
                        print(nb_push)
                        result = result + nb_push
                        break

                # if len(my_tries) > 100000:
                #     my_tries = sort_list_by_sum(my_tries)
                #     if nb_push in parked_tries.keys():
                #         parked_tries[nb_push] += my_tries[50000:]
                #     else:
                #         parked_tries[nb_push] = my_tries[50000:]
                #     my_tries = my_tries[:50000]

            # remove useless buttons
            if my_tries:
                for index in range(0,len(my_tries[0])):
                    if all(my_try[index] == 0 for my_try in my_tries):
                        for button in my_machine.buttons:
                            if button[index] == '1':
                                my_machine.buttons.remove(button)



    # That approach doesn't work ... combinatory issue
    # for my_machine in data:
    #     print("Machine " + str(progress) + " / " + str(len(data)))
    #     progress += 1
    #     my_machine.nice_print()
    #
    #     my_tries = [
    #         [int(c) for c in s]
    #         for s in my_machine.buttons
    #     ]
    #     nb_push = 0
    #     keep_going = True
    #
    #     while keep_going:
    #         nb_push += 1
    #         new_tries = []
    #         for my_try in my_tries:
    #             if my_try == my_machine.joltages:
    #                 result += nb_push
    #                 print(nb_push)
    #                 keep_going = False
    #                 break
    #             else:
    #                 for button in my_machine.buttons:
    #                     new_joltage = activate_button(my_try, button)
    #                     if check_joltage(new_joltage, my_machine.joltages):
    #                         new_tries.append(new_joltage)
    #         my_tries = unique_list_of_lists(new_tries)

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
