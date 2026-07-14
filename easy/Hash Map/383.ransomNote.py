# 給妳兩個字串：ransomNote（妳想拼出的贖金信內容）和 magazine（雜誌上所有的字母）。
# 判斷能不能「只用 magazine 裡的字母」拼出 ransomNote。
# 規則：magazine 裡每個字母只能用一次（剪下來就沒了）。

# 想法：ransomNote裡有的 magazine裡一定要有才會是true 且magazine一定>=ransomNote 
# 先將ransomNote跟 magazine分別放到不同的list中 
# 執行一個for迴圈(for char in magazine:) 
# 然後進到if判斷 
# 如果magazine的list中有ransomNote的字 
# 則將magazine跟ransomNote相同的字remove 否則繼續迴圈 
# 如果ransomNote為空字串 則回傳true 否則false

# 改善從頭到尾做：改用字典
# 我會需要在外面先建立一個空的字典 
# 在每一次迴圈 進到一個if判斷 
# 如果char not in 空的字典 則新增一筆 
# 如果char已經有在這個字典裡 則空的字典[""] = 空的字典[""] + 1

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {} # 建立空字典（空清單）
        magazine_dict = {} # 建立空字典（空貨架）

        for char in ransomNote:
            if char not in ransomNote_dict:
                ransomNote_dict[char] = 1 # 第一次出現，新增標籤，數量從1開始
            else:
                ransomNote_dict[char] = ransomNote_dict[char] + 1 # 已存在，數量+1
            ### .get(char, 0) = 去字典裡找 char 這個 key，如果找得到就回傳它的值；如果找不到，就回傳我指定的預設值 0
            ###ransomNote_dict[char] = ransomNote_dict.get(char, 0) + 1
        for char in magazine:
            if char not in magazine_dict:
                magazine_dict[char] = 1
            else:
                magazine_dict[char] = magazine_dict[char] + 1
            ###magazine_dict[char] = magazine_dict.get(char, 0) + 1
        for char in ransomNote_dict:
            # 如果這個字母貨架上根本沒有，或者 購物清單需要的數量比貨架庫存還多，那就是買不成，直接回傳 False
            if char not in magazine_dict or ransomNote_dict[char] > magazine_dict[char]:
                return False
            
        return True

sol = Solution()
print(sol.canConstruct("a", "b")) # False  
print(sol.canConstruct("aa", "ab")) # False  
print(sol.canConstruct("aa", "aab")) # True