def firstDuplicate(a):
    
    # intialize empty dicttionary
    d = {}

    # check if the element is in dictionary
    # and store it
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

        # return the first occurence of duplicate
        if(d[a[i]] == 2):
            return a[i]

    return -1