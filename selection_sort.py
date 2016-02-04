#sort = [33, 24, 534, 1, 35, 2, 65, 3289, 4, 46, 39, 223, 3, 25]
sort = [42, 9, 17, 54, 602, -3, 54, 999, -11]
sort_len = len(sort)

print(sort)

for i in range(0, sort_len-1):
    ind = i + 1
    for j in range (ind, sort_len):
        if sort[ind] > sort[j]:
            ind = j
    if sort[i] > sort[ind]:
        temp = sort[i]
        sort[i] = sort[ind]
        sort[ind] = temp
        print(sort)

print(sort)
