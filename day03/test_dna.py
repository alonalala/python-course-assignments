# test_dna.py
# Test cases for dna_library.py
# Run with:  python -m pytest test_dna.py -v
# (or just:  python test_dna.py  for the built-in runner)

import pytest
from dna_library import (
    validate_sequence,
    get_base_counts,
    get_complement,
    get_reverse,
    get_reverse_complement,
    get_gc_content,
    get_melting_temperature,
    get_extinction_coefficient,
    analyze,
)

# ── validate_sequence ────────────────────────────────────────────────────────

def test_validate_empty():
    valid, msg = validate_sequence("")
    assert valid is False
    assert "No sequence" in msg

def test_validate_valid():
    valid, msg = validate_sequence("ATCG")
    assert valid is True
    assert msg == ""

def test_validate_lowercase_accepted():
    # validate_sequence uppercases internally
    valid, msg = validate_sequence("atcg")
    assert valid is True

def test_validate_invalid_chars():
    valid, msg = validate_sequence("ATXG")
    assert valid is False
    assert "X" in msg

def test_validate_mixed_invalid():
    valid, msg = validate_sequence("ATCGZ1")
    assert valid is False


# ── get_base_counts ──────────────────────────────────────────────────────────

def test_base_counts_simple():
    counts = get_base_counts("AACGT")
    assert counts == {'A': 2, 'C': 1, 'G': 1, 'T': 1}

def test_base_counts_all_same():
    counts = get_base_counts("AAAA")
    assert counts == {'A': 4, 'C': 0, 'G': 0, 'T': 0}

def test_base_counts_lowercase():
    counts = get_base_counts("atcg")
    assert counts == {'A': 1, 'C': 1, 'G': 1, 'T': 1}


# ── get_complement ───────────────────────────────────────────────────────────

def test_complement_basic():
    assert get_complement("ATCG") == "TAGC"

def test_complement_all_A():
    assert get_complement("AAAA") == "TTTT"

def test_complement_all_G():
    assert get_complement("GGGG") == "CCCC"

def test_complement_mixed():
    assert get_complement("AATTCCGG") == "TTAAGGCC"


# ── get_reverse ──────────────────────────────────────────────────────────────

def test_reverse_basic():
    assert get_reverse("ATCG") == "GCTA"

def test_reverse_palindrome():
    assert get_reverse("ABBA") == "ABBA"

def test_reverse_single():
    assert get_reverse("A") == "A"


# ── get_reverse_complement ───────────────────────────────────────────────────

def test_reverse_complement_basic():
    # ATCG -> complement TAGC -> reverse CGAT
    assert get_reverse_complement("ATCG") == "CGAT"

def test_reverse_complement_known():
    # Classic check: rev-comp of rev-comp should give original
    seq = "GCATCGAT"
    assert get_reverse_complement(get_reverse_complement(seq)) == seq


# ── get_gc_content ───────────────────────────────────────────────────────────

def test_gc_content_50():
    assert get_gc_content("ATCG") == pytest.approx(50.0)

def test_gc_content_0():
    assert get_gc_content("AAAA") == pytest.approx(0.0)

def test_gc_content_100():
    assert get_gc_content("GCGC") == pytest.approx(100.0)

def test_gc_content_custom():
    # AAATCG: 2 GC out of 6 = 33.33%
    assert get_gc_content("AAATCG") == pytest.approx(33.33, rel=1e-2)


# ── get_melting_temperature ──────────────────────────────────────────────────

def test_tm_short_sequence():
    # "ATAT" (length 4, <14): 2*(2+2) + 4*(0+0) = 8
    assert get_melting_temperature("ATAT") == pytest.approx(8.0)

def test_tm_short_with_gc():
    # "ATGC" (length 4): 2*(1+1) + 4*(1+1) = 4 + 8 = 12
    assert get_melting_temperature("ATGC") == pytest.approx(12.0)

def test_tm_long_sequence():
    # Length >= 14, use the basic formula
    seq = "ATCGATCGATCGATCG"   # 16 bases: 4G, 4C, 4A, 4T
    expected = 64.9 + 41 * (8 - 16.4) / 16
    assert get_melting_temperature(seq) == pytest.approx(expected)


# ── get_extinction_coefficient ───────────────────────────────────────────────

def test_ext_coef_single_A():
    assert get_extinction_coefficient("A") == 15200

def test_ext_coef_single_C():
    assert get_extinction_coefficient("C") == 7050

def test_ext_coef_single_G():
    assert get_extinction_coefficient("G") == 12010

def test_ext_coef_single_T():
    assert get_extinction_coefficient("T") == 8400

def test_ext_coef_combined():
    # ACGT: 15200 + 7050 + 12010 + 8400 = 42660
    assert get_extinction_coefficient("ACGT") == 42660


# ── analyze (integration) ────────────────────────────────────────────────────

def test_analyze_returns_all_keys():
    result = analyze("ATCG")
    for key in ['sequence', 'reverse', 'complement', 'reverse_complement',
                'counts', 'gc_content', 'melting_temp', 'extinction_coef', 'length']:
        assert key in result

def test_analyze_uppercase_normalization():
    result = analyze("atcg")
    assert result['sequence'] == "ATCG"

def test_analyze_raises_on_empty():
    with pytest.raises(ValueError):
        analyze("")

def test_analyze_raises_on_invalid():
    with pytest.raises(ValueError):
        analyze("ATXG")

def test_analyze_length():
    result = analyze("ATCGATCG")
    assert result['length'] == 8


# ── built-in runner (no pytest needed) ───────────────────────────────────────

if __name__ == "__main__":
    import sys
    passed = 0
    failed = 0
    errors = []

    test_functions = {name: obj for name, obj in list(globals().items())
                      if name.startswith("test_") and callable(obj)}

    for name, fn in test_functions.items():
        try:
            fn()
            print(f"  PASS  {name}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {name}: {e}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed out of {passed + failed} tests.")
    sys.exit(0 if failed == 0 else 1)
