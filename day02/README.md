# Day 02: DNA Sequence Analyzer

## AI Usage
* **AI Used:** Google Gemini
* **Prompts used to generate this work:**
    1. *"I have a Python assignment to create a script that performs a well-known scientific calculation from my field. Could we brainstorm some ideas relevant to molecular biology and genomics?"*
    2. *"Let's build a DNA sequence analyzer. The program should take a DNA sequence string as input and calculate the reverse sequence, complement sequence, reverse complement, base composition, GC content percentage, melting temperature, and extinction coefficient based on standard reference formulas. Please help me structure the Python code and the accompanying README documentation."*


## Description
This program is a standard molecular biology utility that analyzes a given DNA sequence. Understanding these metrics is essential when analyzing genomic sequence grammar or designing primers for experiments. 

The user is prompted to input a DNA sequence (in the 5' to 3' direction). The program then computes and outputs the following data:
* **Reverse, Complement, and Reverse Complement sequences:** Useful for identifying binding sites on opposite strands.
* **Base composition & GC Content:** Calculates the specific counts of A, C, G, and T, and the overall percentage of Guanine and Cytosine.
* **Melting Temperature (°C):** Estimates the temperature at which the DNA strands will dissociate. It uses the Wallace rule ($T_m = 2(A+T) + 4(G+C)$) for sequences under 14 base pairs, and a standard salt-adjusted calculation for longer sequences.
* **Extinction Coefficient:** Estimates how strongly the sequence absorbs light at 260 nm, calculated using a standard additive model of individual nucleotide values.

## Sample Input
```text
Enter a DNA sequence (5' to 3'): ATGCGTACGTTAGC
