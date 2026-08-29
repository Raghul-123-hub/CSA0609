def word_break_words(s, dictionary):
    words = set(dictionary)
    dp = [None] * (len(s) + 1)
    dp[0] = []

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] is not None and s[j:i] in words:
                dp[i] = dp[j] + [s[j:i]]
                break

    return dp[-1]


dictionary = [
    "i", "like", "sam", "sung", "samsung",
    "mobile", "ice", "cream", "icecream",
    "man", "go", "mango"
]

for text in ["ilike", "ilikesamsung"]:
    result = word_break_words(text, dictionary)

    if result:
        print("Yes:", " ".join(result))
    else:
        print("No")
