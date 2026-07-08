# 給妳一個字串，找出第一個只出現一次的字元，回傳它的索引位置（如果都沒有，回傳 -1）。

# 想法：感覺要兩個迴圈 第一個迴圈:先把s建立一個空的字典s_dict 然後進入迴圈for char in s:
# 之後用if-else 如果char not in s_dict: 則將s_dict[char] 設定為1 
# 如果有的話 將s_dict[char]設定為s_dict[char] + 1 
# 這樣就會有整個字串的key跟value了
# 然後在第二個迴圈 讓他跑完所有的s_dict 
# 如果第一個碰到value的值為1 則return 這個index -> s.index(char)
# 如果跑完都沒有1 則代表都為重複的 則return -1

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         s_dict = {}
#         for char in s:
#             if char not in s_dict:
#                 s_dict[char] = 1
#             else:
#                 s_dict[char] = s_dict[char] + 1
        # 效能上不好
#         for char in s_dict: # O(n)
#             if s_dict[char] == 1:
#                 return s.index(char) #O(n)
#         return -1

# 僅需判斷：
# 這個字母出現了幾次（判斷是不是「只出現一次」）
# 這個字母第一次出現的位置在哪（如果它真的只出現一次，才需要回傳這個位置）
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}

        for index, char in enumerate(s): # enumerate()把字串（或 list），每個元素前面自動加上一個編號，從 0 開始。
            if char not in s_dict:
                s_dict[char] = [1, index] # [出現次數, 第一次出現的位置]
            else:
                s_dict[char] = [s_dict[char][0] + 1, s_dict[char][1]]
                #                ^次數部分+1              ^位置維持原本的，不動
                # s_dict[char] = [次數, 位置]
        for char in s_dict: # O(1)
            if s_dict[char][0] == 1:
                return s_dict[char][1]
        return -1
    
sol = Solution()
print(sol.firstUniqChar("leetcode")) # 0   

