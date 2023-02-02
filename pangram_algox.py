from string import ascii_lowercase as alphabet
from algox import exact_cover, solve


join = "".join


def check_vowels(word, one_vowel):
    # if one_vowel is True we should return True
    # if one_vowel is False, return True if there's one_vowel
    # regardless, we should return False for words with 3 vowels
    n_vows = sum(v in word for v in "aeiou")
    if one_vowel:
        return n_vows == 1
    # you can have 0, 1, or 2 vowels
    return n_vows < 3


def filter_words(words, skip="a", one_vowel=True):
    # only include words with one vowel, if required
    no_dupes = lambda w: len(w) == len(set(w))

    return [
        w
        for w in words
        if no_dupes(w) and (skip not in w) and check_vowels(w, one_vowel)
    ]


if __name__ == "__main__":
    with open("data/words.txt") as f:
        all_words = f.read().split("\n")

    for skip in alphabet:
        alpha = join(a for a in alphabet if a != skip)
        words = filter_words(all_words, skip=skip)

        word_letts = {w: list(w) for w in words}

        X, Y = exact_cover(set(alpha), word_letts)

        solutions = list(solve(X, Y, []))
        for s in solutions:
            print(f"Without {skip}: {','.join(s)}")

        if solutions == []:
            print(f"No solutions for {skip}")
