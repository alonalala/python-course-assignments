# dna_analyzer.py

print("--- DNA Sequence Analyzer ---")
# Get input from the user and ensure it's uppercase
sequence = input("Enter a DNA sequence (5' to 3'): ").upper()

length = len(sequence)

if length == 0:
    print("Error: No sequence provided.")
else:
    # 1. Base composition
    count_A = sequence.count('A')
    count_C = sequence.count('C')
    count_G = sequence.count('G')
    count_T = sequence.count('T')

    # 2. Reverse sequence
    reverse_seq = sequence[::-1]

    # 3. Complement sequence
    # We replace bases one by one. We use lowercase temporarily to avoid double replacements.
    comp_seq = sequence.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()

    # 4. Reverse complement (5' -> 3')
    rev_comp_seq = comp_seq[::-1]

    # 5. GC content [%]
    gc_content = ((count_G + count_C) / length) * 100

    # 6. Melting temperature [°C]
    # Using Wallace rule for short sequences, basic formula for longer ones
    if length < 14:
        tm = 2 * (count_A + count_T) + 4 * (count_G + count_C)
    else:
        tm = 64.9 + 41 * (count_G + count_C - 16.4) / length

    # 7. Extinction coefficient (linear approximation)
    # Values in L/(mole·cm)
    ext_coef = (count_A * 15200) + (count_C * 7050) + (count_G * 12010) + (count_T * 8400)

    # Print the results matching the requested format
    print("\n--- Results ---")
    print(f"Sequence (5' -> 3'):         {sequence}")
    print(f"Reverse complement (5' -> 3'):{rev_comp_seq}")
    print(f"Reverse sequence (5' -> 3'):  {reverse_seq}")
    print(f"Complement sequence (5' -> 3'):{comp_seq}")
    print(f"Base composition:            A: {count_A}, C: {count_C}, G: {count_G}, T: {count_T}")
    print(f"GC content [%]:              {gc_content:.2f}%")
    print(f"Melting temperature [°C]:    {tm:.2f} °C")
    print(f"Extinction coefficient:      {ext_coef} L/(mol·cm)")