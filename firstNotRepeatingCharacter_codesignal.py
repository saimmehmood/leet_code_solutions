def firstNotRepeatingCharacter(s):

    d = {} # empty dictionary
    
    # storing the occurences of elements
    for i in range(len(s)):

        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    
    # finding the occurence of first not repeating character
    for key in d:
        if d[key] == 1:
            return key
    
    return '_'
