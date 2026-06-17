def first_unique_char(s):
    counts={}

    for char in s:
        counts[char]=counts.get(char, 0)+1

    for index, char in enumerate(s):
        if counts[char]==1:
            return index
        
    return -1

print(first_unique_char("leetcode"))

print(first_unique_char("loveleetcode"))

print(first_unique_char("aabb"))