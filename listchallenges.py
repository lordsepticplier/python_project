def connection(list1,list2):
    for firstl in list1:
        for secondl in list2:
            if firstl==secondl:
                return True
    return False

print(connection([5,2,3,1],[4,6,7,8]))
print(connection([5,2,3,1],[4,6,5,8]))
print(connection([5,3,1],[4,6,5,8]))
print(connection([2,3,1],[4,6,5,8]))
#used to test that the fuction works being that it returns true if the lists have one common member

