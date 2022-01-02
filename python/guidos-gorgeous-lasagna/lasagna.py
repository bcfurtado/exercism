EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Return remining bake time

    This function takes the actual minutes the lasagna has been in the
    oven as an argument and returns how many minutes the lasagna
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time needed in minutes

    This function that takes the number of layers you want to add to the
    lasagna as an argument and returns how many minutes you would
    spend making them.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers
    & the time already spent baking and calculates the total elapsed
    minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

