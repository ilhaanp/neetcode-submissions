class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = dict()

        for num in nums:
            if num not in my_dict:
                my_dict[num] = 0
            
            my_dict[num] += 1

            if my_dict[num] > 1:
                return True

        return False
