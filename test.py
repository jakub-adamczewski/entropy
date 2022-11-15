results = []


def flatten(l):
    return [item for sublist in l for item in sublist]

flat = flatten(results)
print(max(flat))
print(min(flat))
