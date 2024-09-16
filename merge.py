class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = []
        l1, l2 = len(word1), len(word2)

        for i in range(min(l1, l2)):
            merged.append(word1[i])
            merged.append(word2[i])
    
        if l1 > l2:
            merged.extend(word1[l2:])
        else:
            merged.extend(word2[l1:])
    
        return ''.join(merged)
