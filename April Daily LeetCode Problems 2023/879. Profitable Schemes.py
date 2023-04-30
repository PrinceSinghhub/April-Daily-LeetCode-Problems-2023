# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

# class Solution:
#     def ispefsuif(self,ln,strs,s1):


#         for i in range(len(s1)):

#             pref = s1[i][0:ln]
#             suff = s1[i][len(s1[i])-ln::]

#             if pref == strs or suff == strs:

#                 return 1

#         return 0


#     def prefixSuffixString(self, s1, s2) -> int:

#         count = 0
#         for i in range(len(s2)):
#             ln = len(s2[i])
#             strs = s2[i]
#             res = self.ispefsuif(ln,strs,s1)
#             count+=res

#         return count

# optimize code

class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        # code here
        ans = 0
        i = 0
        j = 0
        m = len(s1)
        n = len(s2)
        while (i < m and j < n):
            if s2[j] in s1[i]:
                l = len(s2[j])
                if s2[j] == s1[i][:l] or s2[j] == s1[i][-l:]:
                    ans += 1
                    i = 0
                    j += 1
                else:
                    i += 1
            else:
                i += 1
        return ans
        # code here


# {
# Driver Code Starts.

if __name__ == "__main__":
    for _ in range(int(input())):
        s1 = list(map(str, input().split()))
        s2 = list(map(str, input().split()))
        obj = Solution()
        print(obj.prefixSuffixString(s1, s2))
# } Driver Code Ends