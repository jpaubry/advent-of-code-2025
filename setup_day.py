#!/usr/bin/env python3
"""
Setup script to create a new day's directory structure.
Usage: python setup_day.py <day>
Example: python setup_day.py 1
"""

import sys
from pathlib import Path

PUZZLE_TEMPLATE = '''"""
Day {day} - Puzzle {puzzle_id}: [Puzzle Title]

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
    lines = input_data.strip().split('\\n')

    # TODO: Implement parsing logic
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

    # TODO: Implement solution logic

    result = None
    return result


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None  # TODO: Set expected result from puzzle

    result = solve(sample_input)
    print(f"Sample result: {{result}}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {{expected_result}}, got {{result}}"
        print("✓ Sample test passed!")
'''


def setup_day(day: int):
    """Create directory structure for a new puzzle day."""
    if not (1 <= day <= 25):
        print(f"Error: Day must be between 1 and 25, got {day}")
        sys.exit(1)

    day_dir = Path(f"day{day:02d}")

    # Create directory
    if day_dir.exists():
        print(f"Warning: Directory '{day_dir}' already exists")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)
    else:
        day_dir.mkdir(parents=True)
        print(f"✓ Created directory: {day_dir}")

    # Create __init__.py
    init_file = day_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text("")
        print(f"✓ Created: {init_file}")

    # Create puzzle files
    for puzzle_id in [1, 2]:
        puzzle_file = day_dir / f"puzzle{puzzle_id}.py"
        if not puzzle_file.exists():
            content = PUZZLE_TEMPLATE.format(day=day, puzzle_id=puzzle_id)
            puzzle_file.write_text(content)
            print(f"✓ Created: {puzzle_file}")
        else:
            print(f"  Skipped: {puzzle_file} (already exists)")

    # Create sample input files
    for i in [1, 2]:
        sample_file = day_dir / f"sample{i}.txt"
        if not sample_file.exists():
            sample_file.write_text("")
            print(f"✓ Created: {sample_file}")

    # Create main input file
    input_file = day_dir / "input.txt"
    if not input_file.exists():
        input_file.write_text("")
        print(f"✓ Created: {input_file}")

    print(f"\n{'=' * 60}")
    print(f"Day {day} setup complete!")
    print(f"{'=' * 60}")
    print(f"\nNext steps:")
    print(f"1. Add sample input to {day_dir}/sample1.txt")
    print(f"2. Add your puzzle input to {day_dir}/input.txt")
    print(f"3. Implement solution in {day_dir}/puzzle1.py")
    print(f"4. Test with: python main.py {day} 1 sample1.txt")
    print(f"5. Run with: python main.py {day} 1 input.txt")


def main():
    if len(sys.argv) != 2:
        print("Usage: python setup_day.py <day>")
        print("Example: python setup_day.py 1")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
    except ValueError:
        print("Error: Day must be an integer")
        sys.exit(1)

    setup_day(day)


if __name__ == "__main__":
    main()