class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            student_id = abs(nums[i])
            desk_index = student_id - 1
            if nums[desk_index] > 0:
                nums[desk_index] = -nums[desk_index]
                
        missing_students = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_students.append(i + 1)
                
        return missing_students

my_solver = Solution()
my_test_array = [4, 3, 2, 7, 8, 2, 3, 1]
final_answer = my_solver.findDisappearedNumbers(my_test_array)
print("The missing numbers are:", final_answer)
        