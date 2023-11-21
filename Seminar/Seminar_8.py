lis = [[1, 2, 3, 4], [4, 5, 1, 1], [1, 7, 8, 5, 1, 4, 1]]


def gemeinsam(lista):
    gem = []
    dic = {}
    cnt = 0
    for i in lista:
        cnt += 1
        for j in i:
            if j in dic and i.count(j) == 1:
                dic[j] += 1
            elif i.count(j) > 1:
                if cnt - 1 == dic[j]:
                    dic[j] = cnt
                if cnt == dic[j]:
                    dic[j] = cnt
            else:
                dic[j] = 1

    nr = len(lista)
    for k, v in dic.items():
        if v == nr:
            gem.append(k)

    return gem


print(gemeinsam(lis))
