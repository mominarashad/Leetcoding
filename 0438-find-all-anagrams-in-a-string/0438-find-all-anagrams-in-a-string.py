class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        
        hash_p=[0]*26
        hash_s=[0]*26

        m=len(p)
        n=len(s)
        res=[]
        if m>n:
            return []

        for i in range(m):
            hash_p[ord(p[i])-ord('a')]+=1
            hash_s[ord(s[i])-ord('a')]+=1

        if hash_p==hash_s:
            res.append(0)

        for i in range(m,n):
            hash_s[ord(s[i])-ord('a')]+=1
            hash_s[ord(s[i-m])-ord('a')]-=1
            
            if hash_p==hash_s:
                res.append(i-m+1)

        return res

            
