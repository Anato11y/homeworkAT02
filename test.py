import pytest
from main import count_vowels

def test_all_vowels():
    """Проверка строки, содержащей только гласные."""
    assert count_vowels("aeiouAEIOU") == 10  # 10 гласных (5 строчных и 5 прописных)

def test_no_vowels():
    """Проверка строки, не содержащей гласных."""
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0  # Нет гласных

def test_mixed_string():
    """Проверка строки с смешанными буквами (гласные и согласные, строчные и прописные)."""
    assert count_vowels("Hello World!") == 3  # Гласные: e, o, o

if __name__ == "__main__":
    pytest.main()
