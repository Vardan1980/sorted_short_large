list1 = ['hello','hi','when','byutifull','I']
sorted_list = []
while True:
    minimum = list1[0]
    for x in list1:
        if len(x) < len(minimum):
            minimum = x
    sorted_list.append(minimum)
    list1.remove(minimum)
    if len(list1)==0:
        break
print(sorted_list)