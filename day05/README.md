# Day 05: Cis-Regulatory Sequence Profiler

## Overview
This tool analyzes DNA sequences (e.g., putative enhancer regions) to calculate rolling GC content and map CpG dinucleotide density. This is useful for predicting mammalian regulatory regions or evaluating sequences before experimental integration.

## Files Included
- `profiler.py`: The main analysis script.
- `test_profiler.py`: Pytest suite to verify the calculation logic.
- `input_sequences.fasta`: Mock dataset containing a GC-rich enhancer and an AT-rich control.
- `requirements.txt`: Required 3rd party libraries.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the analysis: `python profiler.py --input input_sequences.fasta --window 20 --outdir results`
3. Run the tests: `pytest test_profiler.py`

## AI Interaction
I utilized AI to help structure the matplotlib outputs with dual Y-axes (one for GC%, one for CpG count) to ensure both metrics could be cleanly visualized on the same scale without squashing the data.