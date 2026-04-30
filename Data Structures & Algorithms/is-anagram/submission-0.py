class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        else:
            charCountfors = [0] * 26
            for c in s:
                num = ord(c.lower()) - 97
                charCountfors[num] += 1
            charCountfort = [0] * 26
            for c1 in t:
                num1 = ord(c1.lower()) - 97
                charCountfort[num1] += 1
            
            if charCountfors == charCountfort:
                return True
            else:
                return False



            