# Day 03 – DNA Sequence Analyzer (Modular Version)

## What I Did

This is the Day 2 DNA Sequence Analyzer, restructured to separate the business logic from the user interface.

### File Structure

| File | Description |
|------|-------------|
| `dna_library.py` | Core logic — all computation functions (shared by all interfaces) |
| `dna_input.py` | Interface 1: interactive, uses `input()` |
| `dna_cli.py` | Interface 2: command-line, uses `sys.argv` |
| `dna_gui.py` | Interface 3: graphical interface using `tkinter` |
| `test_dna.py` | Test suite for the library functions |

### How to Run

**Interactive (input):**
```bash
python dna_input.py
```

**Command-line:**
```bash
python dna_cli.py ATCGATCG
```

**GUI:**
```bash
python dna_gui.py
```

**Tests:**
```bash
python -m pytest test_dna.py -v
# or without pytest:
python test_dna.py
```

### What the Program Does

Given a DNA sequence, it computes:
- Reverse sequence
- Complement sequence
- Reverse complement (opposite strand, 5'→3')
- Base composition (A, C, G, T counts)
- GC content (%)
- Melting temperature (Wallace rule for <14 bp; basic formula for longer)
- Extinction coefficient (linear approximation, L/mol·cm)

### External Libraries

No external libraries are required. All three interfaces use only the Python standard library (`tkinter` is included with Python).

### AI Interaction

I used Claude (Anthropic) to help restructure the Day 2 code for Day 3.

- I provided my Day 2 script and described the assignment requirements.
- Claude split the code into a library (`dna_library.py`) with individual functions for each computation, and created the three interface files and the test suite.
- I reviewed the generated code and verified that the logic matches my original Day 2 solution.
- The `validate_sequence` function and the built-in test runner (so tests work without installing pytest) were additions Claude suggested that I found useful.
