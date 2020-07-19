class Solution_1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        for i in range(n):
            s_set = set()
            s_set.add(s[i])
            temp_len = 1
            for j in range(i+1, n):
                if s[j] not in s_set:
                    temp_len += 1
                    s_set.add(s[j])
                else:
                    break
            if max_len <= temp_len:
                max_len = temp_len
        return max_len
# time: 568 ms, memory: 13.4 MB


class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        max_len = 0
        n = len(s)
        left_idx = -1
        for i in range(n):
            if i != 0:
                s_set.remove(s[i-1])
            while left_idx+1 < n and s[left_idx+1] not in s_set:
                s_set.add(s[left_idx+1])
                left_idx += 1
            max_len = max(max_len, len(s_set))
        return max_len
# time: 92 ms, memory: 13.6 MB


if __name__ == "__main__":
    s = Solution_2()
    str_s = "abbcehbc"
    print(s.lengthOfLongestSubstring(str_s))


