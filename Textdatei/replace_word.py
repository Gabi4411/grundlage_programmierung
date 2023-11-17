def replace(file, word, replace_word):
    with open(file, 'r') as datei:
        text = datei.read()
        replace_text = text.replace(word, replace_word)
        cnt = replace_text.count(replace_word)

    with open(file, 'w') as date:
        date.write(replace_text)

    return cnt


def main():
    file_name = 'ex2_fisier.txt'
    word = 'ion'
    replace_word = 'barb'
    cnt = replace(file_name, word.lower(), replace_word)

    if cnt > 0:
        print(f'Ersetzt {word} durch {replace_word} an {cnt} Stellen.')
    else:
        print('Ups, in deine Datei ist nichts verandert.')


main()
