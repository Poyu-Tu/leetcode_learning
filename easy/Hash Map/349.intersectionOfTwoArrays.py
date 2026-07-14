# 給你兩個整數陣列 nums1 和 nums2,回傳它們的交集(重複的元素只需要出現一次)。
# 例如:
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    # 輸出: [2]

# 暴力破解法想法O(nxm)：
    # 我會先建立一個空的list，用來存放有交集的元素，
    # 會用到兩個迴圈，第一個迴圈是跑nums1的項目，長度是len(nums1)，
    # 接著跑第二個迴圈，是跑nums2的項目，長度是len(nums2)，
    # 在第二個迴圈中，寫if-else，
    # 如果nums1[i]與nums2[j]相等，則加入到空的list中，
    # 如果沒有相等則繼續迴圈，全都比對完後回傳空的字串裡的所有元素。

# 優化想法：
    # 問題 1:重複元素的處理
        # 這樣會執行2次，裡面有兩個2，這不符合題目需求，
        # 所以還需要在加入結果 list前面，加上一個if判斷，
        # 如果不在空的字串裡面的話，在新增進去，
        # 但也可以在要回傳結果前使用set()，來拿掉重複元素，再回傳。
    # 問題 2:換成 dictionary 的思路
        # 可能會先幫nums1建立一個空的字典n_dict_1，
        # 然後我會做一個for迴圈跑nums1，如果nums1[i]沒有在n_dict_1裡面，
        # 則將nums1[i]設定為1，寫進n_dict_1裡面，
        # 如果有在n_dict_1中，則將其加一。
        # 後續判斷「另一個陣列的元素有沒有在交集裡」的方式就是跑第二個for迴圈 for j in nums2，
        # 如果nums[j]的元素沒有在n_dict_1中，則nums2.remove(j)，
        # 最後回傳nums2，然後一開始先針對nums2做set()，移除重複的元素。
        # ->> 會有IndexError: list index out of range或可能會漏刪東西
    # 修改成：
        # 如果nums2[j]的元素有在n_dict_1中，
        # 且nums2[j] 沒有在result中，則result.append(nums[j])，
        # 最後回傳result，在外面建立一個result = []。
    # 其實只用到了「這個 key 存不存在」：
        # 先將nums1與nums2轉成set()，再做交集運算，最後回傳list()。

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1) # 將nums1轉成set()，移除重複的元素
        result = set()
        for i in nums2:        
            if i in nums1:
                result.add(i) # 如果nums2[i]有在nums1中，則加入result
        return list(result) # 將set()轉成list()，回傳結果
    
sol = Solution()
print(sol.intersection([1, 2, 2, 1], [2, 2])) # 輸出: [2]
print(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4])) # 輸出: [9, 4]
print(sol.intersection([1, 2, 3], [4, 5, 6])) # 輸出: []