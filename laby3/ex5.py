def is_valid_brackets(s):
    stack = []
    # Mapowanie zamykających nawiasów do ich otwierających odpowiedników
    bracket_map = {')': '(', ']': '['}

    for char in s:
        # Jeśli char jest otwierającym nawiasem, dodaj go do stosu
        if char in bracket_map.values():
            stack.append(char)
        # Jeśli char jest zamykającym nawiasem
        elif char in bracket_map:
            # Jeśli stos jest pusty lub nawias na szczycie stosu nie pasuje do zamykającego nawiasu, nawiasowanie jest niepoprawne
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # Usuwamy pasujący otwierający nawias ze stosu
            stack.pop()

    # Jeśli stos jest pusty, wszystkie nawiasy zostały poprawnie zamknięte
    return not stack

# Przykłady
print(is_valid_brackets("([()[]])()"))  # True - nawiasowanie jest poprawne
print(is_valid_brackets("(]"))         # False - nawiasowanie jest niepoprawne
print(is_valid_brackets(")("))         # False - nawiasowanie jest niepoprawne
print(is_valid_brackets("([]"))        # False - nawiasowanie jest niepoprawne
