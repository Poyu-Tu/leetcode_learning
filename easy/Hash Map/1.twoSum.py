# 給你一個整數陣列 nums 和一個目標值 target，
# 請你找出陣列中兩個數字，使得它們相加等於 target，並回傳這兩個數字的索引（index）。

# 想法：假設為nums = [2,7,11,15], target = 9，
# 首先 我會將nums的第0個跟nums的第一個先進行相加 
# 如果結果是9 那就印出這兩個數字分別所在nums中的位置 
# 如果不是9 則nums的第0個繼續跟nums的第2個進行相加 以此類推 
# 所以外層會需要一個無窮迴圈 如果nums相加後等於target 則break 終止迴圈

# 「固定一個數字，換另一個數字去掃過所有可能」，跑完之後再換下一個固定的數字。
# 「已知範圍內全部跑過一遍」用 for 迴圈就能做到，不需要 while 迴圈的無窮迴圈+break。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ex [2, 7, 11, 15]
         for i in range(len(nums)): # 外層,固定一個數字(從第0個開始)
            for j in range(len(nums)): # 內層,拿這個數字跟後面每一個數字比對
                if j <= i:
                    continue    # 如果j小魚等於i，跳過，到下一個j
                if nums[i] + nums[j] == target: # 如果結果是9
                    return [i, j]

sol = Solution()
result1 = sol.twoSum(nums=[2,7,11,15], target=9)
result2 = sol.twoSum(nums=[3, 2, 4], target=6)
result3 = sol.twoSum(nums=[3, 3], target=6)

print(result1, result2, result3)