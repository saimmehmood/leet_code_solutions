class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str1 = []
        str2 = []

        # adding array characters in stack if they are != to "#"
        # and poping the last added character if stack is not
        # empty

        for i in range(len(s)):
            if s[i] != "#":
                str1.append(s[i])
            elif s[i] == "#" and len(str1) > 0:
                str1.pop()


        for j in range(len(t)):
            if t[j] != "#":
                str2.append(t[j])
            elif t[j] == "#" and len(str2) > 0:
                str2.pop()

        # comparing both stacks
        if str1 == str2:
            return True
        return False