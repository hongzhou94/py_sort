#sort = [33, 24, 534, 1, 35, 2, 65, 3289, 4, 46, 39, 223, 3, 25]
sort = [42, 9, 17, 54, 602, -3, 54, 999, -11]
sort_len = len(sort)

print(sort)

for i in range(1, sort_len):
    j = i;
    while (j > 0) and (sort[j-1] > sort[j]):
        temp = sort[j-1]
        sort[j-1] = sort[j]
        sort[j] = temp
        j = j - 1

print(sort)
