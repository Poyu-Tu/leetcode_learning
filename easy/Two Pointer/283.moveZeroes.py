# 題目：
# 給你一個整數陣列 nums，要你把所有的 0 移到最後面，
# 同時「非 0 的數字之間的相對順序不能變」，而且必須「原地修改（in-place）」，
# 不能另外開一個新陣列來裝。

# 想法：
    # 如果可以開一個新list：
        # 假設新list為result=[]，我會寫兩個迴圈，第一個迴圈判定非0的數字，
        # 如果為非0，則將該數字新增到result裡，那麼原本nums裡，只剩下0的數字，
        # 再接著第二個迴圈，繼續將剩下的0全部加入到result中。
            # Q1：第二個迴圈「將剩下的 0 全部加入 result」，怎麼判斷要加幾個 0？
                # A：我覺得可以在第一個迴圈中判斷 如果為0 則count_0 + 1 
                # 所以必須在迴圈外層建立一個count_0 = 0 之後再一次全部新增進去
            # Q2：要怎麼把 count_0 個 0 一次補進 result？
                # A：[0] * 3 結果是 [0, 0, 0]
                # result.append([0, 0])   # ❌ 變成 [1, 3, 12, [0, 0]]  → 整包塞進去，不拆封
                # result.extend([0, 0])   # ✅ 變成 [1, 3, 12, 0, 0]    → 拆封後一個一個接上去
                # 也可以使用result = result + [0] * count_0
        # nums = [0,1,0,3,12]
        # result = []
        # count_0 = 0
        # for i in nums:
        #     if i != 0:
        #         result.append(i)
        #     else:
        #         count_0 = count_0 + 1
        # result.extend([0] * count_0)
        # print(result)
    # 不能開一個新list：
        # 我會建立兩個變數第一個是now，代表現在的位置，第二個是count_0，來計算0的數量，
        # now負責走過所有的list，然後會再建立一個變數next，代表下一個非0的數字要去的位置。
        # now會先設定為0，讓他一格一格走，如果值是0，則count_0會加1，如果值是非0，則去找目前最前面為0的那格，將值設定為那格的index。
            # 效能問題：回頭重新掃一次陣列前面的部分
            
    # Sol
    # 我會建立2個變數，第一個是now，代表現在的位置，一開始設定為0；
    # 第二個是next，代表下一個非0的數字要移動的位置，一開始設定為0；
    # 設定一個while now < len(nums)迴圈，
    # 設定if判斷now這個位置是否為0，
    # 如果這個值是0，則now = now + 1；
    # 如果非0，則將now的位置的值設定到next的位置的值，
    # 然後如果now > next，則將nums[now]設定為0，
    # 最後now = now + 1 ，next = next + 1。

from ast import List

# 覆蓋與手動補零
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # use快慢指針
#         now = 0
#         next = 0
#         while now < len(nums):
#             if nums[now] == 0:
#                 now = now + 1
#             else:
#                 nums[next] = nums[now]
#                 if now > next:
#                     nums[now] = 0
#                 now = now + 1
#                 next = next + 1
#         print(nums)

# 交換()
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0 # 建立慢指針
        for fast in range(len(nums)):   # 使用for 來操作快指針
            # 短路求值
            # 前面檢查當前數字是否為0，後面檢查快慢指針是否同位置，
            # 順序可顛倒
            if nums[fast] != 0 and fast != slow:
                nums[slow], nums[fast] = nums[fast], nums[slow] # 位置的值交換
                slow = slow + 1 # 交換位置後，將慢指針往後一格
        print(nums)

sol = Solution()
result1 = sol.moveZeroes([0,1,0,3,12])
result2 = sol.moveZeroes([0])


