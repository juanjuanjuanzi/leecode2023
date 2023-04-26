class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict={"2":"abc","3":"def",
                    "4":"ghi","5":"jkl","6":"mno",
                    "7":"pqrs","8":"tuv","9":"wxyz"}

        n=len(digits)
        ans=[]
        if n==0:
            return []
        for v in num_dict[digits[0]]:
            ans.append(v)
        
        for i in range(1,n):
            temp=[]
            for v1 in ans:
                for v2 in num_dict[digits[i]]:
                    temp.append(v1+v2)
            ans=temp

        return ans
