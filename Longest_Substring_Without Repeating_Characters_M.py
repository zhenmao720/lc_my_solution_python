class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        st = []
        for i in s:
            if st and (i in st):
                pos = st.index(i)
                st = st[pos+1:]
                st.append(i)
            else:
                st.append(i)
                if len(st)>max:
                    max = len(st)
        return max
