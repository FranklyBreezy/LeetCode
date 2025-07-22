#A fancy string is a string where no three consecutive characters are equal.
#Given a string s, delete the minimum possible number of characters from s to make it fancy.
#Return the final string after the deletion. It can be shown that the answer will always be unique.

def fancyString(s):
    result = []
    count = 1

    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1]:
            count+=1
        else:
            count = 1
        if count < 3:
            result.append(s[i])

    return "".join(result) 
    
inp = str(input())
print(fancyString(inp))

