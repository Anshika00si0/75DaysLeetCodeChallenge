class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

my_solver = Solution()

example_array_1 = [1, 2, 3, 1]
example_array_2 = [1, 2, 3, 4]

result_1 = my_solver.containsDuplicate(example_array_1)
print("Does example_array_1 have duplicates?", result_1) 

result_2 = my_solver.containsDuplicate(example_array_2)
print("Does example_array_2 have duplicates?", result_2)
        