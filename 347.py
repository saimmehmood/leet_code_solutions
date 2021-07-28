from collections import Counter

def fun(nums, k):
    # getting list of tuples with most common element at the begining
    most_common = Counter(nums).most_common()

    res = []
    for i in range(0, k):
        res.append(most_common[i][0])

    return res