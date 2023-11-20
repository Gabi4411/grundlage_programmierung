from ui.inputurile import utilizatorul, computer
from rps.game import match


def main():
    user_cnt = 0
    pc_cnt = 0

    while (user_cnt != 3) and (pc_cnt != 3):
        pc = computer()
        user = utilizatorul()
        rezultat = match(user, pc)

        if rezultat == 'egal':
            print('Egal, mai incearca.')
        if rezultat == 'user won':
            user_cnt += 1
            print(f'Ai un punct, bravo! Uite-ti punctajul: {user_cnt}')
        if rezultat == 'pc won':
            pc_cnt += 1
            print(f'Calculatorul a castigat, el are {pc_cnt} puncte!')

    if user_cnt > pc_cnt:
        print('Ai castigat!')
    if user_cnt < pc_cnt:
        print('Ai pierdut!')
    if user_cnt == pc_cnt:
        print('Egalitate!')


main()
