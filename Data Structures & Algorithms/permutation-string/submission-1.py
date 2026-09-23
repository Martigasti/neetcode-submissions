class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1) 
        target = Counter(s1)

        for i in range(len(s2)): 
            sub_s = s2[i:i+k] 
            if target == Counter(sub_s):
                return True
        return False
        