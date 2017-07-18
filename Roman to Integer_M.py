class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1:
            return None
        dic = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        re = 0
        for i in range(len(s)-1):
            if dic[s[i]]<dic[s[i+1]]:
                re -= dic[s[i]]
            else:
                re += dic[s[i]]
        re += dic[s[len(s)-1]]
        return re