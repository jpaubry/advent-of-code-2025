"""
Day 10 - Puzzle 2: [Puzzle Title]

[Brief description of the puzzle]
"""
from struct import pack_into

from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, LpStatus, COIN_CMD
import numpy as np
import re

# Define the path where Homebrew installed CBC
# Check your specific path, but this is the standard M-series path:
path_to_cbc = "/opt/homebrew/bin/cbc"

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

    for my_machine in data:
        progress += 1
        print("Machine " + str(progress) + " / " + str(len(data)))
        my_machine.nice_print()

        nb_push = 0

        buttons_matrix = np.array([[int(c) for c in button] for button in my_machine.buttons])
        target_vector = np.array(my_machine.joltages)

        A = buttons_matrix.T
        b = target_vector

        # Number of variables (P0 to P9)
        N_VARS = A.shape[1]

        # --- 2. Set up the PuLP Problem ---

        # Since we are solving an equality constraint problem, the objective
        # doesn't matter much. We can minimize a dummy variable (like 0).
        prob = LpProblem("System_of_Equations_Solver", LpMinimize)

        # Define the variables (P0 to P9)
        # We assume non-negative integers (P_i >= 0).
        P = [LpVariable(f'P{i}', lowBound=0, cat='Integer') for i in range(N_VARS)]

        # PuLP will try to minimize this sum (Z) while satisfying the constraints.
        prob += lpSum(P), "Minimize_Sum_of_P"

        # --- 3. Add Constraints (A * P = b) ---

        # Iterate through each row of A (each equation)
        for i in range(A.shape[0]):
            # Left Hand Side (LHS): Sum(A[i, j] * P[j])
            # Note: A[i, j] is the coefficient for variable P[j] in equation i
            lhs = lpSum(A[i, j] * P[j] for j in range(N_VARS))

            # Right Hand Side (RHS): The target value b[i]
            rhs = b[i]

            # Add the equation constraint: LHS == RHS
            prob += lhs == rhs, f"Equation_{i + 1}"

        # Define the path where Homebrew installed CBC (Verify this path: /opt/homebrew/bin/cbc)
        path_to_cbc = "/opt/homebrew/bin/cbc"

        try:
            # Use the COIN_CMD class as instructed by the error message
            prob.solve(COIN_CMD(path=path_to_cbc, msg=0))

            #print(f"Status: {LpStatus[prob.status]}")

            if LpStatus[prob.status] == "Optimal":
                # Extract the minimum sum achieved (the optimal value of the objective function)
                min_sum = value(prob.objective)
                #print("\n--- Solution Vector P (P0 to P9) ---")
                P_solution = [value(p) for p in P]
                #for i, val in enumerate(P_solution):
                    #print(f"P{i} = {val}")
                print(int(min_sum))
                result += int(min_sum)

                # Final Verification
                P_np = np.array(P_solution)
                T_check = A @ P_np
                #print("\n--- Verification ---")
                #print(f"A * P (Calculated):\t {T_check}")
                #print(f"Target T (Desired):\t {b}")

            else:
                print("\nNo feasible non-negative integer solution was found for the exact equality constraints.")

        except Exception as e:
            print(f"A new critical error occurred during solving: {e}")


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
