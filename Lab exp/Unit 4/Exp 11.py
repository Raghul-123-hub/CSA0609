class WordFilter:

    def __init__(self, words):
        self.words = words

    def f(self, pref, suff):
        answer = -1

        for i in range(len(self.words)):
            if self.words[i].startswith(pref) and self.words[i].endswith(suff):
                answer = i

        return answer


wordFilter = WordFilter(["apple"])

print(wordFilter.f("a", "e"))
