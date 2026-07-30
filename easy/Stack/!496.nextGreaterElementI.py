# 題目：(維持一個有順序的狀態)
    # 給你兩個陣列 nums1 和 nums2，nums1 是 nums2 的子集合。
    # 對 nums1 裡的每個數字 x，找出它在 nums2 中的位置，
    # 然後回傳「在 nums2 中，x 右邊第一個比 x 大的數字」。
    # 如果不存在就回傳 -1。

# 想法：(暴力破解)V1
    # 我會先建立一個空的list，
    # 在最外層，我會先針對nums1做一個for迴圈，
    # 然後在裡面，在針對nums2做一個for迴圈。
    # 裡面的邏輯是這樣，我會讓nums1跟nums2一個個比對，
    # 如果nums1的數字=nums2的數字，
    # 這裡會再做一個迴圈，跑目前nums2的位置+1的數字到nums2的最後一格數字，
    # 然後如果nums2的數字>nums1的數字，
    # 則將nums2的位置+1的數字加入到那個空的list，
    # 否則將-1加入到那個空的list。
    # 最後迴圈跑完，回傳空的list。
        # 會有問題：「否則加入 -1」被放在迴圈裡面了
            # Q：「加入 -1」這個動作，應該放在程式的哪個位置？
                # 還有——當你在第三層迴圈裡找到了那個比較大的數字之後，
                # 還需要繼續往右跑嗎？為什麼？
# A：
    # 1.加入的是「當下正在看的那個數字」，不是「位置 +1 的數字」
        # 因為往右跑的時候，位置一直在變。
    # 2.「先假設 -1，找到再覆蓋」 取代了「否則加入 -1」。
        # 這樣就不會每比對一次就塞一個 -1。

# 修正過的想法：
    # 我會先建立一個空的 list。
    # 最外層針對 nums1 做 for 迴圈，取出每個數字 x。
    # 第二層針對 nums2 做 for 迴圈，找出 x 在 nums2 中的位置。
    # 找到之後，先假設答案是 -1，再從那個位置的下一格開始往右跑第三層迴圈。
    # 只要遇到比 x 大的數字，就把那個數字記下來當答案，然後立刻 break 跳出。
    # 第三層迴圈結束後，把記下來的答案加入 list
    # （如果從頭到尾都沒遇到更大的，它就還是一開始假設的 -1）。
    # 全部跑完，回傳這個 list。
# O(m x n)
# nums1 = [1,5,3]
# nums2 = [1,3,4,2,5]
# a = []
# for i in range(len(nums1)):
#     ans = -1    # 這一輪的預設答案
#     for j in range(len(nums2)):
#         if nums1[i] == nums2[j]:
#             for k in range(j + 1, len(nums2)):
#                 if nums2[k] > nums1[i]:
#                     ans = nums2[k]
#                     break
#             a.append(ans)
# print(a)
# O(m + n)
# 與其讓每個數字自己「往右去找」，不如反過來——讓後面的數字主動來「認領」前面還在等答案的數字。
# 「內部永遠保持降冪」的堆疊，就叫做單調遞減堆疊。
    # 只要堆疊頂端的數字比新數字小，就把它彈出來，
        # 彈出來的數字用字典存放，key是彈出來的數字，value是害他彈出來的數字
    # 並且它的答案就是這個新數字。 
    # 一直重複這個動作，直到頂端的數字比新數字大（或堆疊空了），
    # 然後把新數字自己推進堆疊。
        # 帶出一個規律：迴圈跑完後，還留在堆疊裡的人，答案通通是 -1。

# 真正的計算全部發生在 nums2，nums1 只是「查答案」。
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 掃一次 nums2，用單調遞減堆疊算出每個數字的答案，存進字典
        d = {}
        stack = []
        result = []

        for num in nums2: # 走過所有nums2的值
            # 先清（可能清很多次）：只要堆疊不空，而且 stack頂端 < nums2[i] → 彈出，並記錄答案 → 重複
            while stack and stack[-1] < num:   # 當stack有值 且 stack頂端<nums2[i]
                temp = stack.pop()  # 接住彈出來的值

                d[temp] = num  # 將值填入d字典中，value設定為大於stack頂端的那個數字
            # 再推：清完之後，把 nums2[i] 推進堆疊
            stack.append(num)   

        # 掃 nums1，每個數字去字典查答案，查不到就 -1
        for num in nums1:
            n1_get = d.get(num, -1) # 「查得到就回傳，查不到就回傳你指定的預設值」
            result.append(n1_get)
        return result

sol = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2] 
nums3 = [2,4]
nums4 = [1,2,3,4]
print(sol.nextGreaterElement(nums1, nums2))   
print(sol.nextGreaterElement(nums3, nums4))    
    