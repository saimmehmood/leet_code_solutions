class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str1 = []
        for i in range(len(s)):
            if s[i] != "#":
                str1.append(s[i])
            elif s[i] == "#" and len(str1) > 0:
                str1.pop()

        str2 = []
        for j in range(len(t)):
            if t[j] != "#":
                str2.append(t[j])
            elif t[j] == "#" and len(str2) > 0:
                str2.pop()

        if str1 == str2:
            return True
        return False