class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        i, res = 0, []
        while i<len(s):
            # print(i)
            if s[i]=="#":
                print(s[i-1])
                temp = i+1+int(s[i-1])
                # print(temp)
                res.append(s[i+1:temp])
                i+=temp
            else:
                i+=1
        return res