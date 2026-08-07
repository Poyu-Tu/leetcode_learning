# 題目：(可變視窗)
    # 給一個只含 0 和 1 的陣列 nums，和一個整數 k。
    # 你最多可以把 k 個 0 翻成 1，回傳翻完之後「最長連續 1」的長度。
    # nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 → 答案 6

# 想法構建：
    # 檢查某一段區間合不合格 >> 區間內 0 的個數 ≤ k → 合格
    # 需要有雙指標，right從左到右一個一個走，left當視窗內 0 的個數 > k 時，才往右移動
    # 不合格時left一直縮，縮到重新合格為止

from ast import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 初始max_len設為0
        max_len = 0
        left = 0
        zero_count = 0

        # right 從左到右掃，把新元素吃進來
        for right in range(len(nums)):

            # 維護一個「視窗內 0 的個數」
            if nums[right] == 0:    # 如果是0，zero_count +1
                zero_count = zero_count + 1

            # 當個數 > k，就 while 迴圈縮 left，直到 <= k
            while zero_count > k:
                if nums[left] == 0: # 如果是0，zero_count -1
                    zero_count = zero_count - 1
                left = left + 1 # 不管是不是0，left都要往右移動
            # 每輪記錄最長長度
            max_len = max(max_len, right - left + 1)

        return max_len

sol = Solution()
result1 = sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
result2 = sol.longestOnes([0,0,1,1,1,0,0], 0)
print(result1, result2)
