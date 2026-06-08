def calculate_rolling_metrics(sequence: str, window_size: int = 100):
    """
    Core business logic function. 
    Calculates rolling GC% and CpG counts for a given sequence.
    """
    seq_str = sequence.upper().strip()
    
    if not seq_str or window_size > len(seq_str) or window_size <= 0:
        return []
        
    results = []
    for i in range(len(seq_str) - window_size + 1):
        window = seq_str[i:i+window_size]
        gc_content = (window.count('G') + window.count('C')) / window_size * 100
        cpg_count = window.count('CG')
        
        results.append({
            'position': i,
            'window_sequence': window,
            'gc_percent': round(gc_content, 2),
            'cpg_count': cpg_count
        })
        
    return results