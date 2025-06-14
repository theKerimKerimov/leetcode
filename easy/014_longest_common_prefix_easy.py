from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Находит самый длинный общий префикс среди списка строк.
        
        Длиннейший общий префикс — это начальная часть строк, 
        которая присутствует в каждой строке из списка.

        Args:
            strs (List[str]): Список строк.

        Returns:
            str: Самый длинный общий префикс.
                 Если списка пуст или общего префикса нет — возвращается пустая строка.

        Пример:
            >>> solution = Solution()
            >>> solution.longestCommonPrefix(["flower","flow","flight"])
            'fl'
            >>> solution.longestCommonPrefix(["dog","racecar","car"])
            ''
        """
        if not strs:
            return ""
        
        most_short = len(min(strs, key=len))
        result = ""

        for i in range(most_short):
            char = strs[0][i]
            for cut_word in strs:
                if char != cut_word[i]:
                    return result
            result += char
        
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))   # fl
    print(solution.longestCommonPrefix(["dog","racecar","car"]))      # (пусто)
    print(solution.longestCommonPrefix([""]))                         # (пусто)
    print(solution.longestCommonPrefix([]))                           # (пусто)
