class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        n=len(words)
        freq={}

        for ch in words:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        buckets=[[] for _ in range(n+1)]

        for ch,fre in freq.items():
            buckets[fre].append(ch)

        res=[]
        for i in range(len(buckets)-1,0,-1):
            for buck in sorted(buckets[i]):
                res.append(buck)

                if len(res)==k:
                    return res