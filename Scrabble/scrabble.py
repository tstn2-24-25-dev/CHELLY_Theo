def scrabble(word):
    score = 0
    for letter in word:
        score += letter_scores[letter]
    return score

import random

letter_scores = {
    'a': random.randint(1, 10), 'b': random.randint(1, 10), 'c': random.randint(1, 10),
    'd': random.randint(1, 10), 'e': random.randint(1, 10), 'f': random.randint(1, 10),
    'g': random.randint(1, 10), 'h': random.randint(1, 10), 'i': random.randint(1, 10),
    'j': random.randint(1, 10), 'k': random.randint(1, 10), 'l': random.randint(1, 10),
    'm': random.randint(1, 10), 'n': random.randint(1, 10), 'o': random.randint(1, 10),
    'p': random.randint(1, 10), 'q': random.randint(1, 10), 'r': random.randint(1, 10),
    's': random.randint(1, 10), 't': random.randint(1, 10), 'u': random.randint(1, 10),
    'v': random.randint(1, 10), 'w': random.randint(1, 10), 'x': random.randint(1, 10),
    'y': random.randint(1, 10), 'z': random.randint(1, 10)
}
print(scrabble("manger"))