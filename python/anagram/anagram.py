from collections import Counter


def detect_anagrams(word, candidates):
    word_counter = Counter(word.lower())

    return [
        candidate for candidate in candidates
        if word_counter == Counter(candidate.lower()) and word != candidate.upper()
    ]
