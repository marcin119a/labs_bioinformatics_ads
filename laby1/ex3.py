def print_subsets(current, n, i =1):
    if (i> n):
      print(current)
      return
    print_subsets(current, n, i + 1)

    print_subsets(current + [i], n, i+1)

n = 3
print_subsets([], n)