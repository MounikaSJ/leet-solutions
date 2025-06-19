class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for i in range(len(nums)):
            if nums[i] in count_dict:
                count_dict[nums[i]] += 1
                #print(f'count_dict: {count_dict}')
            else:
                count_dict[nums[i]] = 1
                #print(f'count_dict: {count_dict}')
        
        sorted_list = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)

        answer = []
        for i in range(k):
            answer.append(sorted_list[i][0])
        return answer