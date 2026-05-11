# dna_library.py
# Core business logic for DNA sequence analysis.

VALID_BASES = set('ACGT')

CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

def validate_sequence(sequence: str) -> tuple[bool, str]:
    if not sequence:
        return False, "No sequence provided."
    invalid = set(sequence.upper()) - VALID_BASES
    if invalid:
        return False, f"Invalid characters found: {', '.join(sorted(invalid))}. Only A, C, G, T are allowed."
    return True, ""

def get_base_counts(sequence: str) -> dict:
    seq = sequence.upper()
    return { 'A': seq.count('A'), 'C': seq.count('C'), 'G': seq.count('G'), 'T': seq.count('T') }

def get_complement(sequence: str) -> str:
    seq = sequence.upper()
    return seq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()

def get_reverse(sequence: str) -> str:
    return sequence.upper()[::-1]

def get_reverse_complement(sequence: str) -> str:
    return get_complement(sequence)[::-1]

def get_gc_content(sequence: str) -> float:
    seq = sequence.upper()
    length = len(seq)
    if length == 0: return 0.0
    counts = get_base_counts(seq)
    return ((counts['G'] + counts['C']) / length) * 100

def get_melting_temperature(sequence: str) -> float:
    seq = sequence.upper()
    counts = get_base_counts(seq)
    length = len(seq)
    if length < 14:
        return 2 * (counts['A'] + counts['T']) + 4 * (counts['G'] + counts['C'])
    else:
        return 64.9 + 41 * (counts['G'] + counts['C'] - 16.4) / length

def get_extinction_coefficient(sequence: str) -> int:
    counts = get_base_counts(sequence.upper())
    return (counts['A'] * 15200 + counts['C'] * 7050 + counts['G'] * 12010 + counts['T'] * 8400)

def translate_sequence(sequence: str) -> str:
    seq = sequence.upper()
    protein = []
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein.append(CODON_TABLE.get(codon, '?'))
    return "".join(protein)

def find_orfs(sequence: str) -> list:
    orfs = []
    seq = sequence.upper()
    stop_codons = {'TAA', 'TAG', 'TGA'}
    
    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    orf_seq = seq[i:j+3]
                    orfs.append({
                        'start': i + 1,
                        'end': j + 3,
                        'length': len(orf_seq),
                        'translation': translate_sequence(orf_seq)
                    })
                    break 
    return orfs

def analyze(sequence: str) -> dict:
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
        'translation':        translate_sequence(seq),
        'orfs':               find_orfs(seq)
    }

def format_results(results: dict) -> str:
    r = results
    c = r['counts']
    
    lines = [
        f"Sequence (5' -> 3'):           {r['sequence']}",
        f"Reverse complement (5' -> 3'): {r['reverse_complement']}",
        f"Base composition:             A: {c['A']}, C: {c['C']}, G: {c['G']}, T: {c['T']}",
        f"GC content [%]:               {r['gc_content']:.2f}%",
        f"Melting temperature [°C]:     {r['melting_temp']:.2f} °C",
        f"Extinction coefficient:       {r['extinction_coef']} L/(mol·cm)",
        f"Direct Translation:           {r['translation']}",
        "\n--- Open Reading Frames (ORFs) ---"
    ]
    
    if not r['orfs']:
        lines.append("No valid ORFs (ATG ... Stop) found.")
    else:
        for idx, orf in enumerate(r['orfs'], 1):
            lines.append(f"ORF {idx}: Start {orf['start']} to End {orf['end']} | Length: {orf['length']} bp")
            lines.append(f"Peptide: {orf['translation']}")
            
    return "\n".join(lines)