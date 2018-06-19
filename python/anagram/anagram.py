from collections import Counter


def detect_anagrams(word, candidates):
    counters = {
        candidate: Counter(candidate.lower())
        for candidate in candidates
    }
    word_counter = Counter(word.lower())

    return sorted([
        candidate for candidate, counter in counters.iteritems()
        if word_counter == counter and word != candidate.upper()
    ])
