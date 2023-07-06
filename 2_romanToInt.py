class Solution: 
    def romanToInt(self, s):
        ans = 0
        m = { 'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        for i in range(len(s)):
           if i < len(s)-1 and m[s[i]] < m[s[i+1]]:
               ans -= m[s[i]]
           else:
               ans += m[s[i]]

        return ans
s = Solution()
print(s.romanToInt("IX"))