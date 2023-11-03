# d = {'a': 1, 'b': 2}
#
# print('printing dict...')
# for key in d:
#     print(key, d[key])

# def count_to_dict(word):
#     d = {}
#     for ch in word:
#         cnt = 0
#         for other_ch in word:
#             if ch == other_ch:
#                 cnt += 1
#         d[ch] = cnt
#     return d
# print(count_to_dict('school'))
#
# def count_to_dict_2(word):
#     d = {}
#     for ch in word:
#         if ch in d:
#             d[ch] += 1
#         else:
#             d[ch] = 1
#
#     return d
# print(count_to_dict_2('masina'))


# def add_tags(i, word):
#     return '<' + i +'>' + word + '<' + i '>'

# def palindorm(word):
#     for idx in range(len(word)//2):
#         if word[idx] != word[-(idx + 1)]:
#             return False
#         return True
#
# print(palindorm('abba'))

# word = 'anna'
# print(word[0:len(word):2])
# print(word[::-1] == word)
# print(word[0:len(word):-1])

# def factorial(nr):
#     p = 1
#     for i in range(1, nr + 1): p *= i
#     return p
#
# print(factorial(4))


# def count_unique(word):
#     counts = count_to_dict_2(word)
#     cnt = 0
#
#     for key in counts:
#         if counts[key] == 1:
#             cnt += 1
#
#     return cnt
#
# print(count_unique('school'))


# def anagramme(str, word):
#     if len(str) != len(word):
#         return False
#     else:
#         for idx in str:
#             if idx not in word:
#                 return False
#         for i in word:
#             if i not in str:
#                 return False
#     return True
#
#
# print(anagramme('anna', 'nnnn'))


# def encrypt(string, shift):
#     new_string = ''
#     for str in string:
#         char = chr(((ord(str) - ord('a') + shift) % 26) + ord('a'))
#         new_string += char
#     return new_string
#
#
# print(encrypt('string', 3))


# def str_find(target, source):
#     return target.find(source)
#
#
# print(str_find('testing', 'ing'))

