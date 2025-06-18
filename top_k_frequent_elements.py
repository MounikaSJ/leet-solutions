from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for i in range(len(nums)): #loop through nums for i
            if nums[i] not in count_dict: # check for ith element in dict
                count = 0 #set count to 0
                for j in range(len(nums)): #now loop through nums to compate with i
                    if nums[i] == nums[j]: #if i=j
                        count += 1 # add count
                count_dict[nums[i]] = count #add key value in dict

                print('Frequency dictionary:', count_dict)
    
        sorted_list = sorted(count_dict.items(), key=lambda item:item[1], reverse = True)
        print("Sorted by frequency:", sorted_list)

        answer =[] #to add the elements which should be return
        for i in range(len(sorted_list[:k])): #loop through the sorted list
            item = sorted_list[:k][i] #pick the items only from the list
            answer.append(item[0]) #append the items list to answer
        return answer # return answer