class Solution:
    def simplifyPath(self, path):

        ans = []

        for name in path.split("/"):

            if name == '.':
                continue

            elif name == '..':
                if len(ans) > 0:
                    ans.pop()

            elif name == '':
                continue

            else:
                ans.append(name)

        return '/' + '/'.join(ans)