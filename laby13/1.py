def find_prefix_matches(pattern, text):
    results = []
    for i in range(len(text)):
        matches = []
        # Sprawdzamy dopasowania od najdłuższego możliwego prefixu do najkrótszego
        max_k = min(len(pattern), i + 1)
        for k in range(1, max_k + 1):
            if pattern[:k] == text[i-k+1:i+1]:
                matches.append(k)
        results.append((i, matches))
    return results

# Przykład 1
pattern1 = "abab"
text1 = "abaabab"
matches1 = find_prefix_matches(pattern1, text1)
for index, match_list in matches1:
    print(f"i = {index}, k = {match_list}")