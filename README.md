# LeetCode 

Репозиторий с моими решениями задач с платформы LeetCode, написанными на Python. Здесь я практикую алгоритмы и структуры данных, улучшая навыки программирования.

---

## Описание

В этом репозитории собраны решения задач с LeetCode разной сложности — от простых до сложных. Каждое решение снабжено комментариями и иногда кратким объяснением подхода.

---

## Структура репозитория

- easy/ — решения простых задач  
- medium/ — решения средних задач  
- hard/ — решения сложных задач  

---

## Как использовать

1. Клонируйте репозиторий:  
   
```bash
   git clone https://github.com/theKerimKerimov/leetcode.git
```

2. Перейдите в нужную папку (например, easy/) и откройте интересующую задачу.

---

## Примеры решений

### Two Sum (Простая задача)

[Ссылка на задачу](https://leetcode.com/problems/two-sum/)

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 + num2 == target and i != j:
                    return [i, j] 
```
