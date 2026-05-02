# dna_cli.py
# Version 2: Command-line interface using sys.argv.
#
# Usage:
#   python dna_cli.py ATCGGCTA
#   python dna_cli.py atcggcta   (lowercase is fine too)

import sys
from dna_library import analyze, format_results

def main():
    if len(sys.argv) != 2:
        print("Usage: python dna_cli.py <DNA_SEQUENCE>")
        print("Example: python dna_cli.py ATCGGCTA")
        sys.exit(1)

    sequence = sys.argv[1]

    try:
        results = analyze(sequence)
        print("--- DNA Sequence Analyzer ---")
        print(format_results(results))
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
