# my_list = [10, 20, 30]
# sum_of_list = sum(my_list)
# lenght_of_list = len(my_list)
# mean_list = sum_of_list / lenght_of_list
# print('mean =')
# print(mean_list)
#
# list_0 = [1,2,3,4,5,6]
# list_1 = list_0[0:3] + list_0[-1:2:-1]
# print(list_1)


list_4 = [1,2,3,4,5,6,7,8,9]
list_5 = [*list_4[:4],*list_4[4:7], *list_4[10:6:-1]]
print('\nlist_5=')
print(list_5)

list_6 = list_4[:4] + list_4[4:7] + list_4[10:6:-1]
print('\nlist_6')
print(list_6)

