# 1# filter

#lst = [1, 3, 4, 6, 10, 11, 15, 12, 14]
#new_lst = list(filter(lambda x: (x%2 == 0) , lst))
#print(new_lst)

#2#
lst = [1, 3, 4, 6, 10, 11, 15, 12, 14]
for i in lst:
    if int(i)%2==0:
        print(i)

