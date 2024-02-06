class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        substr_start = 0
        substr_end = 1
        longest_substr = s[0]

        for i in range(1, len(s)):
            curr_substr = s[substr_start:substr_end]
            # print(substr_start, substr_end, s[substr_start:substr_end])

            if s[i] in curr_substr:
                for j in range(substr_start, substr_end):
                    if s[j] == s[i]:
                        substr_start = j + 1
                        substr_end = i + 1
                        break
            else:
                substr_end += 1

            curr_substr = s[substr_start:substr_end]

            if len(curr_substr) > len(longest_substr):
                longest_substr = curr_substr

        # print(str(len(longest_substr)) + " " + longest_substr)
        return len(longest_substr)

    # alternative solution
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s) == 0:
    #         return 0

    #     if len(s) == 1:
    #         return 1

    #     longest_substr = 0

    #     charSet = set()
    #     left = 0

    #     for right in s:
    #       while s[right] in charSet:
    #         charSet.remove(s[left])
    #         left += 1
    #       charSet.add(s[right])

    #       longest_substr = max(longest_substr, right - left + 1)

    #     return longest_substr
