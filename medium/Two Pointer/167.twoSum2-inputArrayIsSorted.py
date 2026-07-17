# 題目：
# 給你一個已經由小到大排好序的陣列 numbers，還有一個目標值 target。
# 你要找出兩個數字，讓它們加起來剛好等於 target，然後回傳這兩個數字的位置
# （注意：這題是 1-indexed，也就是位置從 1 開始算，不是從 0）。
# 題目保證：一定剛好有一組答案，而且同一個元素不能用兩次。

# 想法：
    # 我覺得這題比較適合用對撞型去解，因為數字越大，排的越靠右邊，
    # 可以就先判斷target的數字是不是小於右邊的變數，
    # 如果大於就讓右邊的變數往內靠，
    # 然後左邊因為是從小到大，所以當target小於右邊的變數的時候，
    # 再讓左邊的變數開始動起來去比對。
        # 會有幾種case：
            # 情況 A：和剛好等於 target → 直接回傳答案。
            # 情況 B：和「太小」了（比 target 小）→ 我需要讓總和變大。動 left 往右
            # 情況 C：和「太大」了（比 target 大）→ 我需要讓總和變小。動 right 往左

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                right = right - 1

sol = Solution()
result1 = sol.twoSum([2,7,11,15], 9)
result2 = sol.twoSum([2,3,4], 6)
result3 = sol.twoSum([-1,0], -1)
print(result1, result2, result3)