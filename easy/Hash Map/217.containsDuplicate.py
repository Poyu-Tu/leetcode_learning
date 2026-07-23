# 題目：
    # 給你一個整數陣列 nums,
    # 請你判斷這個陣列裡面是否有任何數字出現超過一次。
    # 如果有重複的數字,回傳 True;
    # 如果所有數字都是獨一無二的,回傳 False。

# 想法：
    # 假設nums = [1,2,3,1]。
    # 我會使用set()，將nums的這個list丟到set()中確認，
    # 然後拿nums的list 跟set()比對長度len 
    # 如果一樣長 代表false 
    # 如果不一樣長 代表set()中有一樣的被刪去 回傳true

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums_set = set(nums)  # 將nums轉成set，會自動去除重複的數字
#         if len(nums) != len(nums_set):
#             return True  # 如果set的長度小於原本的list，表示有重複的數字
#         return False  # 如果set的長度等於原本的list，表示沒有重複的數字

# Hash Map
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for n in nums:
            if n in nums_set:
                return True
            else:
                nums_set.add(n)
        return False
         
sol = Solution()
result1 = sol.containsDuplicate(nums=[1, 2, 3, 1])
result2 = sol.containsDuplicate(nums=[1, 2, 3, 4])
result3 = sol.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
print(result1, result2, result3)