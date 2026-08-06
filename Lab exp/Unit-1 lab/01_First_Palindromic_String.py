def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
words = input("Enter the words separated by space: ").split()

result = first_palindrome(words)

if result:
    print("First Palindromic String:", result)
else:
    print("No Palindromic String Found")
