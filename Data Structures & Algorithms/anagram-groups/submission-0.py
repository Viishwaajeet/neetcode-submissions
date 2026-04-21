class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        for i in strs:
            flag = 0
            for j in groups:
                if self.areAnagrams(i,j[0]):
                    j.append(i)
                    flag = 1
            if flag==0:
                groups.append([i])
        return groups

    def areAnagrams(self, str1, str2):
        if len(str1)!=len(str2):
            return False
        
        count = [0]*26
        for i in range(len(str1)):
            count[ord(str1[i])-ord('a')] += 1
            count[ord(str2[i])-ord('a')] -= 1

        for i in count:
            if i!=0:
                return False
        return True