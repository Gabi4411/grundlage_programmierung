def add_state(states, state):
    """
    Stores a state in a list of states
    :param states: list of states
    :param state single state as tuple (number_of_tries, guessed, guessed_positions)
    """
    states.append(state)


def get_current_state(states):
    return states[-1]

def set_initial_state(states, word):
    states.append([0, 2, [0, len(word) - 1]])