class Solution:
    def reverseWords(self, s: str) -> str:

        res=[]
        i=0
        n=len(s)
        
        while i<n:

            while i<n and s[i]==" ":
                i+=1

            if i>=n:
                break

            start=i

            while i<n and s[i]!=" ":
                i+=1


            res.append(s[start:i])

        reverse=[]

        for word in reversed(res):
            reverse.append(word)

        return " ".join(reverse)

            