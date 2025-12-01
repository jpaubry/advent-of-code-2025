advent-of-code-2025

A well-organized Python project structure for solving daily coding puzzles.
Project Structure
puzzle-solver/
├── main.py              # Main entry point to run puzzles
├── setup_day.py         # Script to create new day directories
├── day01/
│   ├── __init__.py
│   ├── puzzle1.py       # Solution for puzzle 1
│   ├── puzzle2.py       # Solution for puzzle 2
│   ├── sample1.txt      # Sample input 1
│   ├── sample2.txt      # Sample input 2
│   └── input.txt        # Actual puzzle input
├── day02/
│   └── ...
└── day25/
    └── ...
Quick Start
1. Setup a New Day
Create the directory structure for a new puzzle day:
bashpython setup_day.py 1
This creates:

day01/ directory
puzzle1.py and puzzle2.py with solution templates
sample1.txt, sample2.txt for test inputs
input.txt for the actual puzzle input

2. Add Your Inputs

Copy the sample input(s) from the puzzle into sample1.txt, sample2.txt, etc.
Copy your actual puzzle input into input.txt

3. Implement Your Solution
Edit day01/puzzle1.py:
pythondef parse_input(input_data: str):
    """Parse the input into a usable format."""
    lines = input_data.strip().split('\n')
    return [int(line) for line in lines]

def solve(input_data: str):
    """Main solution function."""
    data = parse_input(input_data)
    
    # Your solution logic here
    result = sum(data)
    
    return result
4. Test with Sample Input
Run your solution against the sample input:
bashpython main.py 1 1 sample1.txt
You can also test directly within the puzzle file:
bashpython day01/puzzle1.py
5. Solve with Real Input
Once your solution works with the sample:
bashpython main.py 1 1 input.txt
Usage
bashpython main.py <day> <puzzle_id> <input_file>
Arguments:

day: Day number (1-25)
puzzle_id: Puzzle identifier (1 or 2)
input_file: Input filename (e.g., input.txt, sample1.txt)

Examples:
bash# Run day 1, puzzle 1 with sample input
python main.py 1 1 sample1.txt

# Run day 1, puzzle 1 with actual input
python main.py 1 1 input.txt

# Run day 5, puzzle 2 with second sample
python main.py 5 2 sample2.txt
Puzzle Template Structure
Each puzzle file has this structure:
pythondef parse_input(input_data: str):
    """Parse the raw input string."""
    # Convert input to usable format
    pass

def solve(input_data: str):
    """Main solution function."""
    data = parse_input(input_data)
    # Solve the puzzle
    return result

if __name__ == "__main__":
    # Test with sample input inline
    sample_input = """..."""
    expected_result = 42
    
    result = solve(sample_input)
    assert result == expected_result
    print("✓ Sample test passed!")
Tips

Testing: Use the if __name__ == "__main__" block in puzzle files for quick inline testing
Multiple Samples: Create sample1.txt, sample2.txt, etc. for different test cases
Debugging: Add print statements in your solution and run specific samples
Reusability: Put common utility functions in a separate utils.py file

Example Workflow
bash# Day 1 arrives
python setup_day.py 1

# Add sample input from puzzle description
# Edit day01/sample1.txt

# Implement solution
# Edit day01/puzzle1.py

# Test with sample
python main.py 1 1 sample1.txt

# If it works, add real input and solve
# Edit day01/input.txt
python main.py 1 1 input.txt

# Move to puzzle 2
# Edit day01/puzzle2.py
python main.py 1 2 sample1.txt
python main.py 1 2 input.txt