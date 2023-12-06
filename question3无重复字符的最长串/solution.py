class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans;

def test_case():
    s = Solution()
    case_input1 = 'abcabcqd'
    print( s.lengthOfLongestSubstring(case_input1))
    assert s.lengthOfLongestSubstring(case_input1) == 3
    print("no error")


if __name__ == '__main__':
    test_case()