from logik.hangman import guess


def test_guess():
    """
    MASINA

    state la start: (0, 0, [])
    choice = s: (0, 1, [2])
    choice = n: (0, 2, [2, 4])
    choice = x: (1, 2, [2, 4])
    :return:
    """

    assert guess('masina', 's', (0, 0, [])) == (0, 1, [2])
