# 題目描述:
# 給你一個已經排序好的整數陣列 nums,裡面可能有重複的數字。
# 請你原地(in-place) 移除重複項,讓每個不重複的數字只出現一次,並且維持原本的順序。
# 不能開新陣列,而且函式最後要回傳「不重複元素的個數」k
# ——陣列的前 k 個位置要放好正確答案,後面的內容 LeetCode 不會檢查。

# 想法：
    # 一樣使用快慢指針的方式，建立三個變數now、next跟countRepeat，
    # now一開始設定為0，代表目前的位置，
    # next一開始設定為0，代表出現重複後要移動的位置，
    # countRepeat一開始設定為0，代表計算重複次數。
    # 建立一個while now < len(nums)迴圈，
    # 設定if-else判斷是否重複，next不會跟著now一起走，
    # 如果nums[now] == nums[next]，now會加1，countRepeat會加1，
    # 然後如果countRepeat為2，則將next設定為now的值；
    # 如果nums[now] != nums[next]，則nums[next] = nums[now]，
    # 然後now加1，next加1，countRepeat歸零。
    # 最後再迴圈外面再判斷不重複的數量len(set(nums))

# 優化：
    # 建立二個變數now、next，now一開始設定為1，因為第0格確認不會有問題，
    # next則從1開始，因為下一個空位是 1 號格,因為 0 號格已經放好了，
    # 建立一個while now < len(nums)迴圈，
    # 設定if-else判斷是否重複，next不會跟著now一起走，
    # 如果nums[now] == nums[next-1]，now會加1，
    # 如果nums[now] != nums[next-1]，則nums[next] = nums[now]，
    # 然後now加1，next加1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # use 快慢指針
        now = 1 # 因為第0格沒問題
        k = 1    # 下一個可以放的位置

        while now < len(nums):
            if nums[now] == nums[k-1]:   # 如果目前now這格=next前一格的數值
                now = now + 1
            else:
                nums[k] = nums[now]
                now = now + 1
                k = k + 1
        return k
    
sol = Solution()
result1 = sol.removeDuplicates([1,1,2])
result2 = sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(result1, result2)

        
        