def firstNotRepeatingCharacter(s):
    count =[0]*26
    for c in s:
        count[ord(c) - ord('a')] += 1
    print count 
    for c in range(26):
        if count[c] == 1: return chr(c + 97)
    return '_'
     
print firstNotRepeatingCharacter("abacabad")