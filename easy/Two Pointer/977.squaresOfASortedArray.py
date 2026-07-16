# 題目：
# 給你一個由小到大排好序的整數陣列 nums（裡面可能有負數），
# 請回傳一個陣列，內容是每個數字的平方，而且結果也要是由小到大排好序。

# 想法：
    # 暴力解：會分成每個數字一個一個進去平方 然後會建立一個空的list 
    # 平方過後會將數字一個個丟進去空的list中 最後透過sorted()來排序

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         # 總體複雜度：O(n) + O(n log n)
#         result = []
#         for i in nums:
#             result.append(i ** 2)
            
#         return sorted(result) # O(n log n)

# 想法2：
    # 建立一個空的list，最大的平方值，會出現在頭尾兩端，
    # 絕對值越大的原始數字,平方後會變最大。
    # 使用雙指標，設定left=0，right=len(nums)-1，
    # 將left與right平方後比大小，將大的值填到最後一格，left填完了要往後一格，right填完了要往前一格，
    # 接著繼續比left跟right。
        # 1. 結果陣列要先開好：需要一個一開始就有 n 個位子的 list
            # 長度為 n、先全部塞 0：result = [0] * len(nums)
                # 先擺好 5 張空椅子,等等再把人一個個安排到指定座位
        # 2. 三個指針/位置變數：
            # left=0,right, position=len(nums)-1
                # position：「現在要填 result 第幾格」的變數
        # 3. while迴圈：當 left <= right

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        position = len(nums) - 1

        result = [0] * len(nums)

        while left <= right:
            l_square = nums[left] ** 2
            r_square = nums[right] ** 2

            if l_square > r_square:
                result[position] = l_square
                left = left + 1
            else:
                result[position] = r_square
                right = right - 1

            position = position - 1

        return result
    
sol = Solution()
result1 = sol.sortedSquares([-4,-1,0,3,10])
result2 = sol.sortedSquares([-7,-3,2,3,11])
result3 = sol.sortedSquares([-7, -3, -1])

print(result1, result2, result3)
