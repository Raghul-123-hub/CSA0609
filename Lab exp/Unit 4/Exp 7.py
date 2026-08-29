def longest_unique_substring(s):
    seen = {}
    left = 0
    maximum = 0

    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right
        maximum = max(maximum, right - left + 1)

    return maximum


print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("bbbbb"))
print(longest_unique_substring("pwwkew"))
