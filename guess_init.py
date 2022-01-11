from functools import reduce
from functools import partial
from itertools import permutations
from collections import Counter
from typing import List
import utils


def counter_letter(words) -> dict:
    lst = reduce(lambda x, y: x + y, [list(w) for w in words], [])
    res = dict(Counter(lst))
    return res


def ana_word_l5():
    words = utils.load_words('words-l5.txt')
    res = counter_letter(words)
    return res


def find_freq_l5():
    words: List[str] = utils.load_words('./words-l5.txt')
    c = ana_word_l5()

    def sorted_key(xs: tuple):
        return sum(c[x] for x in xs)

    choices = list(sorted([p for p in permutations(c.keys(), 5)],
                          key=sorted_key, reverse=True))

    def predicate(word, letters):
        return all([x in word for x in letters])

    for choice in choices:
        freq_words = list(filter(partial(predicate, letters=choice), words))
        if len(freq_words) >= 1:
            return freq_words
    return []


def find_init():
    def point(w1, w2):
        res = 0
        for i in range(min(len(w1), len(w2))):
            if w1[i] == w2[i]:
                res += 1
        return res

    words: List[str] = utils.load_words('./words-l5.txt')
    freq5_words = find_freq_l5()
    res = {}
    for guess in freq5_words:
        p = 0
        for word in words:
            p += point(guess, word)
        res.update({guess: p})
    return list(sorted([(k, v) for k, v in res.items()],
                       key=lambda x: x[1],
                       reverse=True))


if __name__ == '__main__':
    # ['aesir', 'aires', 'aries', 'arise', 'erisa', 'raise', 'saire', 'serai']
    print(find_init())
    # 'serai' or 'raise' may be good init
