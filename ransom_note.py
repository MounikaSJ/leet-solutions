class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for i in range(len(magazine)):
            if magazine[i] in mag_dict:
                mag_dict[magazine[i]] += 1
            else:
                mag_dict[magazine[i]] = 1
        
        ran_dict = {}

        for j in range(len(ransomNote)):
            if ransomNote[j] in ran_dict:
                ran_dict[ransomNote[j]] +=1
            else:
                ran_dict[ransomNote[j]] = 1

        for key,value in ran_dict.items():
            if key not in mag_dict or mag_dict[key] < ran_dict[key]:
                return False

        return True
