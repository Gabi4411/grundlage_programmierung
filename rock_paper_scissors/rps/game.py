def match(user, pc):
    '''

    :param user: optiunea aleasa de user
    :param pc: optiunea aleasa de random de pc
    :return: cine a castigat dintre user si pc
    '''
    if user == pc:
        return 'egal'
    elif (user == 'foarfeca' and pc == 'hartie') or (user == 'hartie' and pc == 'piatra') or (user == 'piatra' and pc == 'foarfeca'):
        return 'user won'
    else:
        return 'pc won'
