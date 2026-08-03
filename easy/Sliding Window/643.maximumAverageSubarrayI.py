# 題目：
    # 給你一個整數陣列 nums 和一個整數 k。
    # 找出長度剛好為 k 的連續子陣列中，平均值最大的那一個，回傳那個平均值。

# 暴力破解想法：
    # 外層：
        # 我會建立一個for迴圈，走過len(nums)-k+1，
        # 內層迴圈跑完的時候，在最後return sum_big的平均數
    # 內層：
        # 我會用for迴圈走過k，在迴圈外層設定一個變數sum，預設為0，
        # 還有另一個變數sum_big，預設負無限大(float('-inf'))，
        # 在這裡面，每次都將該數字加進sum，跑完後跟sum_big比大小，
        # 如果sum大的話就將sum的值丟到sum_big。

# 滑動視窗核心公式：新總和 = 舊總和 - 離開的那個 + 進來的那個
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        now_sum = 0 # 當前視窗總和，每輪必更新

        # 先把第一個視窗的總和算出來（這一步是 O(k)，只做一次）
        # 用這個總和當 max_sum 的初始值（順便解決剛剛那個 0 的陷阱）
        for i in range(k):
            now_sum = now_sum + nums[i] # 先算第一個視窗

        # 歷史最大值，只在超越時更新
        max_sum = now_sum   # 第一個視窗直接當初始冠軍


        # 從第 k 個元素開始往後跑，每一步做「減掉離開的、加上進來的」，然後比大小
        for j in range(k, len(nums)):
            now_sum = now_sum - nums[j - k] + nums[j]   # 滑動視窗

            if now_sum > max_sum:   # 比大小
                max_sum = now_sum

        avg = max_sum / k   # 算平均數

        return avg  # Python 3 裡 / 出來一定已經是 float

sol = Solution()
Result1 = sol.findMaxAverage([1,12,-5,-6,50,3], 4)
Result2 = sol.findMaxAverage([5], 1)

print(Result1, Result2)