#!/usr/bin/env python3
"""
Daily Puzzle Solver - Main Entry Point
Usage: python main.py <day> <puzzle_id> <input_file>
Example: python main.py 1 1 input.txt
"""

import sys
import importlib
from pathlib import Path


def solve_puzzle(day: int, puzzle_id: int, input_file: str):
    """
    Load and execute the specified puzzle solution.

    Args:
        day: Day number (1-25)
        puzzle_id: Puzzle identifier (1 or 2)
        input_file: Name of the input file (e.g., 'input.txt', 'sample1.txt')
    """
    # Validate inputs
    if not (1 <= day <= 25):
        print(f"Error: Day must be between 1 and 25, got {day}")
        sys.exit(1)

    if puzzle_id not in (1, 2):
        print(f"Error: Puzzle ID must be 1 or 2, got {puzzle_id}")
        sys.exit(1)

    # Build paths
    day_dir = Path(f"day{day:02d}")
    input_path = day_dir / input_file

    # Check if day directory exists
    if not day_dir.exists():
        print(f"Error: Directory '{day_dir}' does not exist")
        sys.exit(1)

    # Check if input file exists
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' does not exist")
        sys.exit(1)

    # Import the puzzle module
    module_name = f"day{day:02d}.puzzle{puzzle_id}"
    try:
        puzzle_module = importlib.import_module(module_name)
    except ImportError as e:
        print(f"Error: Could not import {module_name}")
        print(f"Make sure 'day{day:02d}/puzzle{puzzle_id}.py' exists")
        print(f"Details: {e}")
        sys.exit(1)

    # Check if solve function exists
    if not hasattr(puzzle_module, 'solve'):
        print(f"Error: {module_name} does not have a 'solve()' function")
        sys.exit(1)

    # Read input file
    try:
        with open(input_path, 'r') as f:
            input_data = f.read()
    except Exception as e:
        print(f"Error reading file '{input_path}': {e}")
        sys.exit(1)

    # Run the solution
    print(f"{'=' * 60}")
    print(f"Running Day {day}, Puzzle {puzzle_id}")
    print(f"Input file: {input_path}")
    print(f"{'=' * 60}\n")

    try:
        result = puzzle_module.solve(input_data)
        print(f"\n{'=' * 60}")
        print(f"Result: {result}")
        print(f"{'=' * 60}")
    except Exception as e:
        print(f"\nError running solution: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <day> <puzzle_id> <input_file>")
        print("Example: python main.py 1 1 input.txt")
        print("         python main.py 5 2 sample1.txt")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        puzzle_id = int(sys.argv[2])
        input_file = sys.argv[3]
    except ValueError:
        print("Error: Day and puzzle_id must be integers")
        sys.exit(1)

    solve_puzzle(day, puzzle_id, input_file)


if __name__ == "__main__":
    main()