from math import log
from operator import itemgetter

ALL_ALLERGIES = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128,
}

MAX_SCORE = sum(ALL_ALLERGIES.values())


class Allergies(object):

    def __init__(self, score):
        self.detected_allergies = []
        if score > MAX_SCORE:
            score = score - (2 ** int(log(score, 2)))

        allergies = reversed(sorted(ALL_ALLERGIES.items(), key=itemgetter(1)))
        for allergy_name, allergy_score in allergies:
            if score >= allergy_score:
                score -= allergy_score
                self.detected_allergies.append(allergy_name)

    def is_allergic_to(self, item):
        return item in self.detected_allergies

    @property
    def lst(self):
        return self.detected_allergies
