def full_justify(words, maxWidth):
    result = []
    i = 0

    while i < len(words):
        j = i
        length = 0

        while j < len(words) and length + len(words[j]) + (j - i) <= maxWidth:
            length += len(words[j])
            j += 1

        line_words = words[i:j]
        spaces = maxWidth - sum(len(word) for word in line_words)
        gaps = len(line_words) - 1

        if j == len(words) or gaps == 0:
            line = " ".join(line_words)
            line += " " * (maxWidth - len(line))
        else:
            base = spaces // gaps
            extra = spaces % gaps

            line = ""
            for k in range(gaps):
                line += line_words[k]
                line += " " * (base + (1 if k < extra else 0))

            line += line_words[-1]

        result.append(line)
        i = j

    return result


words1 = ["This", "is", "an", "example", "of", "text", "justification."]
words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]

print(full_justify(words1, 16))
print(full_justify(words2, 16))
