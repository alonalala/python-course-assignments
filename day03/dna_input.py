# dna_input.py
# Version 1: Interactive interface using the input() function.

from dna_library import analyze, format_results

print("--- DNA Sequence Analyzer ---")
sequence = input("Enter a DNA sequence (5' to 3'): ")

try:
    results = analyze(sequence)
    print(format_results(results))
except ValueError as e:
    print(f"Error: {e}")
