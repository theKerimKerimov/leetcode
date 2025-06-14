from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Находит два индекса index_1 и index_2 в списке nums, таких что nums[index_1] + nums[index_2] == target.
        
        Args:
            nums (List[int]): Список целых чисел.
            target (int): Целевое число, сумма двух элементов которого нужна.
        
        Returns:
            List[int]: Список из двух индексов [index_1, index_2], где сумма элементов равна target.
        
        Примечание:
            Предполагается, что ровно одно решение существует,
            и нельзя использовать один и тот же элемент дважды.
        """
        # Перебираем каждый элемент и ищем второй, чтобы сумма была target
        for index_1, num_1 in enumerate(nums):
            for index_2, num_2 in enumerate(nums):
                if num_1 + num_2 == target and index_1 != index_2:
                    return [index_1, index_2]


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))   # [0, 1]
    print(solution.twoSum([3,2,4], 6))       # [1, 2]
    print(solution.twoSum([3,3], 6))         # [0, 1]