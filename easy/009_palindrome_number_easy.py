class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Проверяет, является ли целое число палиндромом.
        Палиндром — число, которое читается одинаково слева направо и справа налево.
        
        Args:
            x (int): Входное число.
        
        Returns:
            bool: True, если число палиндром, иначе False.
        
        Примечание:
            Отрицательные числа считаются не палиндромами.
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))    # True
    print(solution.isPalindrome(-121))   # False
    print(solution.isPalindrome(10))     # False
