# 題目：給你兩個已經各自排序好的陣列：
# nums1 的長度是 m + n：前面 m 個是真正有效的數字，後面 n 個是 0，純粹是「預留的空位」
# nums2 有 n 個數字
# 任務：把 nums2 合併進 nums1，讓整個 nums1 變成一個排序好的陣列，而且要**原地（in-place）**修改

# 初步想法(暴力解)：
    # 我會拿nums2裡所有的值，從nums1最後面開始，慢慢把nums2最後的值放進nums1最後，
    # 放完後nums1往左移一格，nums2也往左移一格，繼續放，直到nums2放完後，我在對nums1裡的值做排序
        # 把 nums2 塞進空位 O(n)
        # 對整個 nums1 排序 O(n log n)

    # 先把 nums2 的值放進 nums1 尾巴的空位（那些 0 的位置）
    # 再對整個 nums1 做排序
    # class Solution:
    #     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    #         for i in range(n):
    #             nums1[m + i] = nums2[i]

    #         nums1.sort()

    # sol = Solution()
    # nums1 = [1,2,3,0,0,0]
    # result1 = sol.merge(nums1, 3, [2,5,6], 3)
    # print(nums1)

# 優化：
    # 1. 空位在後面（那些 0）→ 所以我們就從後面開始填、每次填「最大的」。
    # 2. 需要三個指標：
        # 一個指著 nums1 的有效值最後一個（也就是 3 的位置）>> m_end = m - 1
        # 一個指著 nums2 的最後一個（也就是 6 的位置） >> n_end = n - 1
        # 一個指著 nums1 整體最後一個空位（要往裡面填東西的位置）   >> n1_end = (m + n) - 1
    # 邏輯：
        # 比大小，大的放進n1_end，然後放進去的跟n1_end都要左移
    # 迴圈：
        # while n_end >= 0
    # 注意：
        # 當m_end < 0時，n_end就自己比

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         m_end = m - 1
#         n_end = n - 1
#         n1_end = (m + n) - 1

#         while n_end >= 0:
#             if nums1[m_end] > nums2[n_end]:
#                 nums1[n1_end] = nums1[m_end]
#                 n1_end = n1_end - 1
#                 m_end = m_end - 1
#             else:
#                 nums1[n1_end] = nums2[n_end]
#                 n1_end = n1_end - 1
#                 n_end = n_end - 1
            # 下面這邊每輪都還是會被比較一次=一輪可能同時填了兩次
            # 可用elif改寫，先將m_end < 0在前面過濾
#             if m_end < 0:
#                 nums1[n1_end] = nums2[n_end]
#                 n1_end = n1_end - 1
#                 n_end = n_end - 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_end = m - 1
        n_end = n - 1
        n1_end = (m + n) - 1

        while n_end >= 0:
            if m_end < 0:   # ① nums1 空了 → 直接搬 nums2
                nums1[n1_end] = nums2[n_end]
                n1_end = n1_end - 1
                n_end = n_end - 1
            elif nums1[m_end] > nums2[n_end]:   # ② nums1 這邊大 → 填 nums1
                nums1[n1_end] = nums1[m_end]
                n1_end = n1_end - 1
                m_end = m_end - 1
            else:   # ③ nums2 這邊大(或相等) → 填 nums2
                nums1[n1_end] = nums2[n_end]
                n1_end = n1_end - 1
                n_end = n_end - 1

sol = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [3,4,0,0,0]
result1 = sol.merge(nums1, 3, [2,5,6], 3)
result2 = sol.merge(nums2, 2, [1,2,3], 3)
print(nums1, nums2)