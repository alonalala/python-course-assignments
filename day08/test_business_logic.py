from business_logic import calculate_rolling_metrics

def test_valid_rolling_calculation():
    test_seq = "ATGCGTATAA" 
    results = calculate_rolling_metrics(test_seq, window_size=5)
    
    assert len(results) == 6
    assert results[0]['gc_percent'] == 60.0
    assert results[2]['cpg_count'] == 1

def test_invalid_window_size():
    results = calculate_rolling_metrics("ATGC", window_size=10)
    assert results == []