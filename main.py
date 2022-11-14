import math


def get_entropy(probabilities):
    return -sum(map(lambda p: p * math.log(p, 2), probabilities))

