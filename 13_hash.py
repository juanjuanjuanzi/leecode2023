class Solution:
    def romanToInt(self, s: str) -> int:
        spec_dict={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        roma_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        if s in spec_dict:
            return spec_dict[s]
        ans=0
        i=0
        while i<len(s)-1:
            if s[i]+s[i+1] in spec_dict:
                ans+=spec_dict[s[i]+s[i+1]]
                i+=2
            else:
                ans+=roma_dict[s[i]]
                i+=1
        if i==len(s)-1:
            ans+=roma_dict[s[i]]
        return ans
