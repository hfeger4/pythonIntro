def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    left = count = temp_count = 0
    for i in range(len(s)):
        temp_count += 1
        if s[i] in s[left:i]:
            left = s[left:i].index(s[i]) + left + 1
            temp_count = len(s[left:i]) + 1
        count = max(temp_count, count)
    return count

