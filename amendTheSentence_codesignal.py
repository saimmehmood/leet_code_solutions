def amendTheSentence(s):
    
    count = 0 # keeping counter for single word sentence
    newStr = s[0].lower() # storing first element
    for i in range(1, len(s)):
        if s[i].isupper() == True:
            count += 1
            # look for capitalize letters and put space
            newStr += " " + s[i].lower()
        else:
            newStr += s[i]
    
    if count > 0:
        return newStr
    
    return s.lower() 
        
