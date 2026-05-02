# dna_library.py
# Core business logic for DNA sequence analysis.
# This module is shared by all interface versions.

VALID_BASES = set('ACGT')


def validate_sequence(sequence: str) -> tuple[bool, str]:
    """
    Validates a DNA sequence string.
    Returns (True, '') if valid, or (False, error_message) if not.
    """
    if not sequence:
        return False, "No sequence provided."
    invalid = set(sequence.upper()) - VALID_BASES
    if invalid:
        return False, f"Invalid characters found: {', '.join(sorted(invalid))}. Only A, C, G, T are allowed."
    return True, ""


def get_base_counts(sequence: str) -> dict:
    """Returns a dict with counts for each base A, C, G, T."""
    seq = sequence.upper()
    return {
        'A': seq.count('A'),
        'C': seq.count('C'),
        'G': seq.count('G'),
        'T': seq.count('T'),
    }


def get_complement(sequence: str) -> str:
    """Returns the complement sequence (same direction, 3' to 5')."""
    seq = sequence.upper()
    return seq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()


def get_reverse(sequence: str) -> str:
    """Returns the sequence reversed (3' to 5' written 5' to 3')."""
    return sequence.upper()[::-1]


def get_reverse_complement(sequence: str) -> str:
    """Returns the reverse complement (the opposite strand, 5' to 3')."""
    return get_complement(sequence)[::-1]


def get_gc_content(sequence: str) -> float:
    """Returns GC content as a percentage (0–100)."""
    seq = sequence.upper()
    length = len(seq)
    if length == 0:
        return 0.0
    counts = get_base_counts(seq)
    return ((counts['G'] + counts['C']) / length) * 100


def get_melting_temperature(sequence: str) -> float:
    """
    Calculates melting temperature in °C.
    Uses the Wallace rule for sequences shorter than 14 bases,
    and the basic formula for longer sequences.
    """
    seq = sequence.upper()
    counts = get_base_counts(seq)
    length = len(seq)
    if length < 14:
        return 2 * (counts['A'] + counts['T']) + 4 * (counts['G'] + counts['C'])
    else:
        return 64.9 + 41 * (counts['G'] + counts['C'] - 16.4) / length


def get_extinction_coefficient(sequence: str) -> int:
    """
    Calculates the extinction coefficient using a linear approximation.
    Unit: L/(mol·cm)
    """
    counts = get_base_counts(sequence.upper())
    return (counts['A'] * 15200 +
            counts['C'] * 7050 +
            counts['G'] * 12010 +
            counts['T'] * 8400)


def analyze(sequence: str) -> dict:
    """
    Runs the full analysis on a DNA sequence.
    Returns a dict with all results, or raises ValueError if the sequence is invalid.
    """
    seq = sequence.upper().strip()
    valid, error = validate_sequence(seq)
    if not valid:
        raise ValueError(error)

    counts = get_base_counts(seq)
    return {
        'sequence':           seq,
        'reverse':            get_reverse(seq),
        'complement':         get_complement(seq),
        'reverse_complement': get_reverse_complement(seq),
        'counts':             counts,
        'gc_content':         get_gc_content(seq),
        'melting_temp':       get_melting_temperature(seq),
        'extinction_coef':    get_extinction_coefficient(seq),
        'length':             len(seq),
    }


def format_results(results: dict) -> str:
    """Formats the analysis results dict into a human-readable string."""
    r = results
    c = r['counts']
    lines = [
        "\n--- Results ---",
        f"Sequence (5' -> 3'):          {r['sequence']}",
        f"Reverse complement (5' -> 3'): {r['reverse_complement']}",
        f"Reverse sequence (5' -> 3'):   {r['reverse']}",
        f"Complement sequence (5' -> 3'):{r['complement']}",
        f"Base composition:             A: {c['A']}, C: {c['C']}, G: {c['G']}, T: {c['T']}",
        f"GC content [%]:               {r['gc_content']:.2f}%",
        f"Melting temperature [°C]:     {r['melting_temp']:.2f} °C",
        f"Extinction coefficient:       {r['extinction_coef']} L/(mol·cm)",
    ]
    return "\n".join(lines)
