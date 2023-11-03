# 9, 12

#9, a

# def primfaktoren(n):
#     lis = []
#     i = 2
#     while n != 1:
#         if n % i == 0:
#             lis.append(i);
#             n //= i
#         else:
#             i += 1
#     return lis
#
#
# print(primfaktoren(20))


#9, b


# def langste_teilfolge(teil):
#
#     if not teil:
#         return []
#
#     long = [teil[0]]
#     current = [teil[0]]
#
#     for i in range(1, len(teil)):
#         if teil[i] == teil[i - 1]:
#             current.append(teil[i])
#         else:
#             if len(current) > len(long):
#                 long = current
#             current = [teil[i]]
#
#     if len(current) > len(long):
#         long = current
#
#     return long
#
#
# print(langste_teilfolge([414, 14, 41, 41]))



#12, a


# def ggt(a, b):
#     while b != 0:
#          a, b = b, a % b
#     return a
#
#
# def relativ_prim(n):
#     prim_zahlen = []
#
#     for i in range(1, n):
#         if ggt(n, i) == 1:
#             prim_zahlen.append(i)
#
#     return prim_zahlen
#
#
# print(relativ_prim(35))

#12, b


def max_summe(nums):
    max_global = max_current = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])

        if max_current > max_global:
            max_global = max_current

    return max_global


print(max_summe([1, -2, 3, 4, -1, 2, 1, -5, 4, 10, 20]))