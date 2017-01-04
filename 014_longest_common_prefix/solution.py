def longestCommonPrefix(strs):
    if (len(strs) <= 0):
        return ""
    lenMin = min([len(currStr) for currStr in strs])
    answer=""
    for charIdx in range(lenMin):
        currChar = strs[0][charIdx]
        for strToCompareIdx in range(len(strs)):
            if (currChar != strs[strToCompareIdx][charIdx]):
                return answer
        answer=answer+currChar
    return answer
print(longestCommonPrefix(["catt","cayt","cattttt"])) #ca
print(longestCommonPrefix(["ca","cat","catt"])) #ca
print(longestCommonPrefix(["cat","dog",""])) #""
print(longestCommonPrefix(["cat","dog","cattttttttt"])) #""
print(longestCommonPrefix([])) #""
