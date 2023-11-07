from repository.state import get_current_state

def guess(word, choice, current_state):
    """
    builds a state based on the cjoice of the user
    :param word: what to guess
    :param choice: character
    :return: state as Tuple
    """

    guessed_indexes = []
    current_guessed_indexes = current_state[2]
    found = False

    for idx in range(len(word)):
        if choice == word[idx] and idx not in current_guessed_indexes:
            guessed_indexes.append(idx)
            found = True

    tries = 1 if not found else 0
    guessed = 1 if found else 0

    return current_state[0] + tries, current_state[1] + guessed, current_state[2] + guessed_indexes


def win(states, word, max_tries):
    if get_current_state(states)[1] == len(word):
        return True

    # if get_current_state(states)[0] > max_tries:
    #     return False