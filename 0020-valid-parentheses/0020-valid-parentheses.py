class Solution:
    def isValid(self, s: str) -> bool:
        
        maps={'}':'{',')':'(',']':'['}

        stack=[]

        for ch in s:

            if ch in maps.values():
                stack.append(ch)
            
            elif ch in maps:

                if not stack or maps[ch]!=stack[-1]:
                    return False

                stack.pop()

        return not stack