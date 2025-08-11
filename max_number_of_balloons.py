class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        baloon_dict = {"b" : 1, "a" : 1, "l" : 2, "o" : 2, "n" : 1}

        input_dict = {}

        count = []

        for i in range(len(text)):
            if text[i] in baloon_dict:
                if text[i] in input_dict:
                    input_dict[text[i]] += 1
                else :
                    input_dict[text[i]] = 1
        
        if len(input_dict.keys()) < 5:
            return 0

        for key in input_dict.keys():
            value = input_dict[key] // baloon_dict[key] 
            count.append(value)
        
        return min(count)








        





