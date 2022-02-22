from collections import defaultdict
from string import ascii_lowercase as alphabet
import numpy as np


def read_words(filename):
    return open(filename).read().split()


def filter_words(words):
    vowels = "aeiou"

    one_vowel = lambda w: sum(v in w for v in vowels) == 1
    no_dupes = lambda w: len(w) == len(set(w))
    return [w for w in words if one_vowel(w) and no_dupes(w)]


def count_bits(n):
    """
    Use the Kernighan trick to count set bits in an int
    """
    c = 0
    while n:
        n &= n - 1
        c += 1

    return c


def word_to_int(word):
    """
    Write a word as an bit mask of 26 letters, then as an int
    """
    join = "".join
    return int(join(str(int(a in word)) for a in reversed(alphabet)), 2)


def word_mapping(words):
    """
    map the binary to the words
    """
    b2w = defaultdict(list)
    for w in words:
        b2w[word_to_int(w)] += [w]

    return b2w


def partition_words(words):
    """
    Split the words into 5 groups, one per vowel
    encode them as ints
    """
    splits = [[], [], [], [], []]
    vowels = "aeiou"

    for w in words:
        index, *_ = [vowels.index(l) for l in w if l in vowels]
        splits[index].append(word_to_int(w))

    return [list(set(s)) for s in splits]


def iterate_xor(target, splits):
    """
    Create a dag by starting from the target and xor'ing one of
    our vowel-split lists of words. In each place store the state that got
    you there, so we can traverse back. If the slot memory[0] is populated
    then we have a solution.
    """
    memory = np.zeros(2 ** 26, dtype=int)
    memory[target] = target
    for s in splits:
        states = memory.nonzero()[0]
        for state in states:
            inds = np.bitwise_xor(state, s)
            memory[inds] = state

    return memory


def traverse_dag(target, dag):
    """
    walk the dag from index 0 until we git the target,
    or'ing out the words at each step so we end up with a list
    of ints encoding the words.
    """
    state = i = 0
    words = []

    while i != target:
        words.append(state ^ dag[i])
        i = dag[i]
        state = i | state

    return words


if __name__ == "__main__":

    words = filter_words(read_words("data/words.txt"))
    b2w = word_mapping(words)
    partitions = partition_words(words)

    target = word_to_int(alphabet.replace("j", ""))
    memory = iterate_xor(target, partitions)
    assert memory[0] != 0, "Solution not found"

    bits = traverse_dag(target, memory)
    print([b2w[b] for b in bits])
