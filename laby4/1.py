from typing import List, Sequence

def three_numbers_of_small_sum(arr: List[int], k: int) -> Sequence[int]:
    # Pierwsze zadanie z ćwiczeń.
    # TODO: wypełnij tę funkcję; ma zwracać trzy liczby (jako tuplę lub listę),
    # których suma nie przekracza k.
    # Można założyć, że zawsze istnieją odpowiednie trzy liczby
    # (tzn. nie przejmujemy się żadnymi przypadkami szczególnymi, że lista ma
    # mniej niż 3 elementy albo że nie da się znaleźć trzech takich liczb).
    return (1, 2, 3)


# Testowanie.

# Funkcja sprawdza, czy lista *a* jest podciągiem listy *b*.
def subsequence(a: List[int], b: List[int]) -> bool:
    i = 0
    for x in b:
        if i < len(a) and x == a[i]: i += 1
    return i == len(a)

count = 0
def test(arr: List[int], k: int):
    global count
    count += 1
    print(f'Test {count}...', end=' ')
    answer = three_numbers_of_small_sum(arr[:], k)
    debug = f'lista: {arr}, k: {k}, zwrócona wartość: {answer}'
    if len(answer) != 3: raise RuntimeError(f'Nie zwrócono trzech liczb!\n{debug}')
    if not subsequence(sorted(answer), sorted(arr)): raise RuntimeError(f'Nie zwrócono liczb z listy!\n{debug}')
    if sum(answer) > k: raise RuntimeError(f'Suma zwróconych liczb jest większa niż k!\n{debug}')
    print('OK!')

try:
    test([1, 2, 3], 7)
    test([1, 1, 1], 3)
    test([9, 8, 7, 6, 5, 4, 3, 2, 1], 6)
    test([9, 8, 7, 6, 5, 4, 3, 2, 1], 10)
    test([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5)
    test([9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9, 9, 9], 11)
except RuntimeError as e:
    print(e)
    import sys
    sys.exit()
print('Wszystkie testy zaliczone!')
