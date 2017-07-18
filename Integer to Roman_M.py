class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic_M = ["", "M", "MM", "MMM"]
        dic_C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        dic_X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        dic_I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        re = dic_M[num/1000]+dic_C[(num/100)%10]+dic_X[(num%100)/10]+dic_I[num%10]
        return re
