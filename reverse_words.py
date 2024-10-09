def reverseWords(s: str) -> str:
    words = ""

    word = ""
    for c in s:
        if c == " ":
            words += " " + word
            word = ""
        else:
            word += c

    words += " " + word
    back = words.split()[::-1]

    return " ".join(back)

print(reverseWords("the sky is blue") == "blue is sky the")
print(reverseWords("  hello world  ") == "world hello")