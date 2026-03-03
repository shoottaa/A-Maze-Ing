import sys
from src.parse_config import parse_config


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python a_maze_ing.py <input_file>")
        sys.exit(1)

    config = parse_config(sys.argv[1])


if __name__ == "__main__":
    main()
