#

# def find(target, source):
#     for i in range(len(target) - len(source) + 1):
#         cnt = 0
#         j = i
#         for index in range(len(source)):
#             if target[j] == source[index]
#                 cnt += 1
#             j += 1
#         if cnt == len(source):
#             return i
#     return -1


# def find(target, source):
#     position = -1
#     j = 0
#
#     for i in range(len(target)):
#         if target[i] != source[j]:
#             j = 0
#             position = -1
#
#         if target[i] == source[j]:
#             if j == 0:
#                 position = i
#
#             if j >= len(source) - 1:
#                 break
#             else:
#                 j += 1
#
#     return position
#
#
# print(find('string', 'ing'))

# 1


# def check_sum(numbers, sum):
#     for i in range(len(numbers) - 1):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == sum:
#                 return True
#
#     return False


# def check_sum(numbers, sum):
#     for number in numbers:
#         if sum - number in numbers:
#             return number, sum - number
#
#     return None
#
#
# print(check_sum([1, 2, 3, 4], 5))
# print(check_sum([1, 2, 3, 4], 9))

# 2

# def generate_multiple(num, length):
#     l = []
#     i = 1
#
#     while i <= length:
#         l.append(num * i)
#         i += 1
#
#     return l
#
#
# print(generate_multiple(3, 4))

# 3
#
# def big_sum(a, b):
#     sum = 0
#     cf = 0
#     i = len(a) - 1
#     p = 1
#
#     while i >= 0:
#         s = int(a[i]) + int(b[i]) + cf
#         cf = 0
#         if (int(a[i]) + int(b[i])) > 9:
#             cf = 1
#
#         sum  = s + sum * p
#         p *= 10
#         i -= 1
#
#     if cf == 1:
#         sum = "1" + sum
#     return str(sum)
#
#
# print(big_sum('123123123', '456456456'))

# 4

def reverse(word):
    i = 0
    j = len(word) - 1
    prima = ''
    doua = ''
    while i < len(word) // 2:
        while j >= len(word) // 2:
            if word[i] in 'aeiou':
                if word[j] in 'aeiou':
                    prima = prima + word[j]
                    doua  = word[i] + doua
                    i += 1
                    j -= 1
                else:
                    doua = word[j] + doua
                    j -= 1
            else:
                prima = prima + word[i]
                i += 1
            if len(prima) + len(doua) >= len(word):
                break
    if len(word) % 2 != 0:
        prima = prima + word[len(word) / 2]
    return prima + doua

print(reverse('terminator'))


def swap(word):
    vok = 'aeiou'
    voks = []
    for ch in word:
        if ch in vok:
            voks.append(ch)
    s = ''
    i = 1
    for ch in word:
        if ch not in vok:
             s += ch
        else:
            s +=  voks[-i]
            i += 1
    return s

print(swap('terminator'))
