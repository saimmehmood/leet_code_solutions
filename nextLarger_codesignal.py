def nextLarger(a):
    res = []
    for i in range(len(a)):
        k = 0 # keeping check if no larger element was found
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                res.append(a[j])
                k += 1
                break
        # adding -1 in that case
        if k == 0:
            res.append(-1)

    return res