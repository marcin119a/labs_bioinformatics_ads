import re
from ex2 import KMPMatch, NaiveMatch

def regex_search(pattern, text):
    return re.search(pattern, text) is not None


import timeit

pattern = "example"
text = "this is an example text with example as a word"
number = 10000  # Ilość powtórzeń

naive_time = timeit.timeit('NaiveMatch(pattern, text)', globals=globals(), number=number)
in_time = timeit.timeit('pattern in text', globals=globals(), number=number)
regex_time = timeit.timeit('regex_search(pattern, text)', globals=globals(), number=number)
kmp_time = timeit.timeit('KMPMatch(pattern, text)', globals=globals(), number=number)

print(f"Naive search time: {naive_time:.6f} s")
print(f"In operator time: {in_time:.6f} s")
print(f"Regex search time: {regex_time:.6f} s")
print(f"KMP search time: {kmp_time:.6f} s")