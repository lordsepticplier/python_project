def connection(list1,list2):  # this function will check all the boxs in two list and return true if they have any in common
    for firstl in list1:
        for secondl in list2:
            if firstl==secondl:
                return True
    return False

print(connection([5,2,3,1],[4,6,7,8]))
print(connection([5,2,3,1],[4,6,5,8]))
print(connection([5,3,1],[4,6,5,8]))
print(connection([2,3,1],[4,6,5,8]))
 #  used to test that the fuction works being that it returns true if the lists have one common member

def minOfList(list1,n):  # this function will return all the words in the list that are larger then n
    result=[]
    for word in list1:
       if len(word)>n:
           result.append(word)
    return result
             
print(minOfList(["harry","pet","peter","e"],4))
print(minOfList(["harry","pet","peter","e"],2))
print(minOfList(["happy","pet","peter","e"],7))
print(minOfList(["harry","pet","peter","eeeeeee"],6))
  # used to test that the fuction works being that it returns all the words in a list that are longer then n
