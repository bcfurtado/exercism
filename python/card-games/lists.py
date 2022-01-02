def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return [number + increment for increment in range(3)]


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    actual_average = card_average(hand)
    strategy_1_average = (hand[0] + hand[-1]) / 2
    strategy_2_average = hand[int(len(hand) / 2)]

    return strategy_1_average == actual_average or strategy_2_average == actual_average


def is_even(number):
    return number % 2 == 0

def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_hand = [card for index, card in enumerate(hand) if is_even(index)]
    odd_hand = [card for index, card in enumerate(hand) if not is_even(index)]

    return card_average(even_hand) == card_average(odd_hand)


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last_card = hand[-1]
    if last_card == 11:
        return hand[:-1] + [last_card * 2]
    return hand
