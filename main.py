a1 = [1, 2, 3, 4]
a2 = [10, 20]
a3 = [100, 200, 300]
a4 = [1000, 2000, 3000, 4000]

a = [[1, 2, 3, 4],
    [10, 20],
    [100, 200, 300],
    [1000, 2000, 3000, 4000]]
count_a = [len(x) for x in a]
# print(count)

# import functools as iter
# count = iter.reduce((lambda a,x : a*x),count_a)
import math
count = math.prod(count_a)


print(count)

# count_a1 = len(a1)
# count_a2 = len(a2)
# count_a3 = len(a3)
# count_a4 = len(a4)
# count = count_a1 * count_a2 * count_a3 * count_a4

#One liner attempt
print([[counter // math.prod(count_a[i+1:]) % count_a[i] for i in range(len(a))] for counter in range(count)])
# for counter in range(count):
#     i_ = list(counter // math.prod(count_a[i+1:]) % count_a[i] for i in range(len(a)))
#     print(i_)

# for counter in range(count):
#     i1 = counter // count_a2 % count_a1
#     i2 = counter % count_a2

#     # i1 = counter // (count_a2*count_a3) % count_a1
#     # i2 = counter  // count_a3 % count_a2
#     # i3 = counter % count_a3

#     # i1 = (counter // (count_a2*count_a3*count_a4)) % count_a1
#     # i2 = (counter // (count_a3*count_a4)) % count_a2
#     # i3 = (counter // count_a4) % count_a3
#     # i4 = counter % count_a4

#     # counter = i4 + i3 * count_a4 + i2*count_a3*count_a4 + i1*count_a2 * count_a3*count_a4

#     # print(i1,i2, a1[i1],a2[i2])
#     print(a1[i1], a2[i2])
#     # print(a1[i1],a2[i2],a3[i3])
#     # print(a1[i1],a2[i2],a3[i3], a4[i4])
#     # print(i1, i2, i3, i4)
