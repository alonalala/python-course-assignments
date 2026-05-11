# Day 04 Assignment: Advanced DNA Sequence Analyzer

## Overview
This repository contains an updated version of the DNA Sequence Analyzer from Day 3. Based on peer feedback, the application has been extended to include complex biological sequencing features, specifically tailored for cloning verifications and sequence exploration.

## New Features
1. **Amino Acid Translation:** The library now includes a standard codon table and translates the raw DNA sequence into its corresponding peptide sequence.
2. **Open Reading Frame (ORF) Detection:** Scans the sequence for start codons (`ATG`) and standard stop codons (`TAA`, `TAG`, `TGA`), returning the coordinates, length, and peptide translation for each valid reading frame.
3. **Colorized Terminal Output:** Implemented the 3rd party library `colorama` to create a more readable and visually distinct command-line interface.

## Prerequisites
To run this script, you must install the required dependencies:
```bash
pip install -r requirements.txt