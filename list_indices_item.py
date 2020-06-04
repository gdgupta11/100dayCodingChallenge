"""
Goal: Write a python challenge to index all list items in a lists

Input: List of search, value to search for

Output: List of indices represented by list of getPrimeNumbers

Note: Keep in mind that python lists contains list of list, should be able to traverse multidimentional list
"""

def index_all(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                indices.append([i]+index)

    return indices

search_list = [2,[1,1,3],[1,3,2],[[1,3],[1,3,2]]]
print("List to look up is --  {}  ".format(search_list))
indices = index_all(search_list, 2)
print("Result -- {} ".format(indices))

"""
Learnings:
    Using a recursive function here to reiterate over lists of list
list of list of indices for the value matching

output will be like: [[0], [2, 2], [3, 1, 2]]
"""
