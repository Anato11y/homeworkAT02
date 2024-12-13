def count_vowels(s):
    """Функция для подсчета количества гласных в строке."""
    vowels = 'aeiouAEIOU'  # Список гласных букв (и строчные, и прописные)
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
