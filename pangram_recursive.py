"""
A simpler but ~10x slower implementation
"""

from collections import defaultdict
from string import ascii_lowercase as alphabet


def read_words(filename):
    return open(filename).read().split()


def filter_words(words):
    vowels = "aeiou"
    one_vowel = lambda w: sum(v in w for v in vowels) == 1
    no_dupes = lambda w: len(w) == len(set(w))
    return [w for w in words if one_vowel(w) and no_dupes(w)]


def pangrams(n, words, letters):
    if n == 0:
        return ()

    for w in words:
        wletts = set(w)
        if wletts.issubset(letters) and len(wletts) == 5:
            poss_letts = letters - wletts
            poss_words = [w for w in words if set(w).issubset(poss_letts)]

            rest = pangrams(n - 1, poss_words, poss_letts)
            if rest is not None:
                return (w, *rest)

    return None


if __name__ == "__main__":

    words = read_words("data/words.txt")
    letters = set(alphabet.replace("j", ""))

    print(pangrams(5, words, letters))
