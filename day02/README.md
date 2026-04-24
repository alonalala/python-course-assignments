# Day 02: DNA Sequence Analyzer

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