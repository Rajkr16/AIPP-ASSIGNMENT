from pathlib import Path
import sys

def count_lines(path: str) -> int:
    """
    Return the number of lines in a .txt file.

    Raises:
        ValueError: if the file does not have a .txt extension.
        FileNotFoundError: if the file does not exist.
        OSError: for other I/O related errors.
    """
    p = Path(path)
    if p.suffix.lower() != '.txt':
        raise ValueError("Only .txt files are supported")
    with p.open('r', encoding='utf-8', errors='replace') as f:
        return sum(1 for _ in f)


if __name__ == "__main__":
    # If no filename is supplied, use the file mentioned here as "word.txt"
    if len(sys.argv) == 1:
        file_path = "word.txt"
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("Usage: python Task05.py [word.txt]")
        sys.exit(1)

    try:
        # Print the result in the requested format
        print(f" number of lines = {count_lines(file_path)}")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)