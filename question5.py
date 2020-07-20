class Solution_1:
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        n = len(s)
        max_len = 1
        max_s = s[0]
        for i in range(n):
            for j in range(i+1, n+1):
                if j - i >= max_len and s[i:j] == s[i:j][::-1]:
                    max_len = j - i
                    max_s = s[i:j]
        return max_s
# time: 5440 ms, memory: 13.6 MB


class Solution_2:
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        n = len(s)
        max_s = s[0]
        for i in range(n):
            max_s = max(self.find_str(s, i, i), self.find_str(s, i, i+1), max_s, key=len)
        return max_s

    def find_str(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
# time: 260 ms, memory: 13.6 MB


if __name__ == "__main__":
    s = Solution_2()
    s_str = "abbab"
    print(s.longestPalindrome(s_str))


