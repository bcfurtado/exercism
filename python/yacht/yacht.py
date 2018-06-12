# Score categories
# Change the values as you see fit

def yacht_points(dice):
    return 50 if len(set(dice)) == 1 else 0

def ones_points(dice):
    return sum_points(dice, 1)

def twos_points(dice):
    return sum_points(dice, 2)

def threes_points(dice):
    return sum_points(dice, 3)

def fours_points(dice):
    return sum_points(dice, 4)

def fives_points(dice):
    return sum_points(dice, 5)

def sixes_points(dice):
    return sum_points(dice, 6)

def sum_points(dice, digit):
    return sum([number for number in dice if number == digit])

def full_house_points(dice):
    stats = { number: dice.count(number) for number in dice }
    if set(stats.values()) == (set([2, 3])):
        return sum([number for number in dice])
    return 0

def four_of_a_kind_points(dice):
    stats = { number: dice.count(number) for number in dice }
    if set(stats.values()) == set([4, 1]):
        more_dices = [number for number, amount in stats.iteritems() if amount == 4][0]
        return sum([number for number in dice if number == more_dices])

    if set(stats.values()) == set([5]):
        return sum([number for number in dice[:-1]])

    return 0

def little_straight_points(dice):
    return 30 if set(dice) == set([1,2,3,4,5]) else 0

def big_straight_points(dice):
    return 30 if set(dice) == set([2,3,4,5,6]) else 0

def choice_points(dice):
    return sum(dice)


YACHT = yacht_points
ONES = ones_points
TWOS = twos_points
THREES = threes_points
FOURS = fours_points
FIVES = fives_points
SIXES = sixes_points
FULL_HOUSE = full_house_points
FOUR_OF_A_KIND = four_of_a_kind_points
LITTLE_STRAIGHT = little_straight_points
BIG_STRAIGHT = big_straight_points
CHOICE = choice_points


def score(dice, category):
    return category(dice)
