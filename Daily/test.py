def isSubstringDistinct(str, num):
    return len(set(str)) is num

def subStringsKDist(inputStr, num):
    strlen = len(inputStr)
    if num < 1 or strlen < 1 or num > strlen:
        return []
    result = []
    for start in range(strlen-num+1):
        sub = inputStr[start:start+num]
        if isSubstringDistinct(sub, num):
            result.append(sub)
    # distinct
    return list(set(result))
    

print(subStringsKDist('abcd', 3))
print(subStringsKDist('abcd', 0))
print(subStringsKDist('abcd', -1))
print(subStringsKDist('abcd', 1))
print(subStringsKDist('abcde', 5))
print(subStringsKDist('abcde', 6))
print(subStringsKDist('', 1))
print(subStringsKDist('', 0))
print(subStringsKDist('aaaaa', 1))
print(subStringsKDist('aaaaa', 2))
print(subStringsKDist('awaglknagawunagwkwagl', 4))