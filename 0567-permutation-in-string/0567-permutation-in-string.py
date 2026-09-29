class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        hash_s1=[0]*26
        hash_s2=[0]*26

        m=len(s1)
        n=len(s2)

        if m>n:
            return False

        for i in range(m):
            hash_s1[ord(s1[i])-ord('a')]+=1
            hash_s2[ord(s2[i])-ord('a')]+=1

        if hash_s1==hash_s2:
            return True

        for i in range(m,n):
            hash_s2[ord(s2[i])-ord('a')]+=1
            hash_s2[ord(s2[i-m])-ord('a')]-=1
            
            if hash_s1==hash_s2:
                 return True

        return False

            
