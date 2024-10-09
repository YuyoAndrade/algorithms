
def strStr(haystack: str, needle: str) -> int:
    i, j = 0, 0
    need = ""
    while i < len(haystack):
        if need == needle:
            return i - len(needle)
        if haystack[i] == needle[j]:
            j += 1
            need += haystack[i]
        else:
            j = 0
            i -= len(need)
            need = ""
        i += 1
    return -1 if need != needle else i - len(needle)
    
haystack = "mississippi"
needle = "issip"

print(strStr(haystack=haystack, needle=needle))