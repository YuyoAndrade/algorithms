def count(n):
    counts = {}
    for c in n:
        if c in counts.keys():
            counts[c] += 1
        else:
            counts[c] = 1
    return counts


print(count([1, 1, 1, 1, 3, 4, 5, 2, 2, 2, 8]))
