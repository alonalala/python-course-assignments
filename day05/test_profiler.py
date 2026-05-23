import pandas as pd
from profiler import calculate_rolling_metrics

def test_calculate_rolling_metrics():
    # A 10bp sequence with 50% GC and one CpG
    test_seq = "ATGCGTATAA" 
    
    # Test with window size 5
    df = calculate_rolling_metrics(test_seq, window_size=5)
    
    # Total positions should be Length(10) - Window(5) + 1 = 6
    assert len(df) == 6
    
    # Window 0: "ATGCG" -> 3 G/C out of 5 = 60%
    assert df.iloc[0]['GC_Percent'] == 60.0
    
    # Window 2: "GCGTA" -> contains one "CG"
    assert df.iloc[2]['CpG_Count'] == 1
    
    # Window 5: "TATAA" -> 0 G/C = 0%
    assert df.iloc[5]['GC_Percent'] == 0.0