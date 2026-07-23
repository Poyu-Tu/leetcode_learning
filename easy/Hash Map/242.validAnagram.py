# 題目：
    # 給你兩個字串 s 跟 t,
    # 請你判斷 t 是不是由 s 重新排列組合而成的。

# 想法：
    # 如果s為apple，t是plaep，那t的字數及字符出現的數量都應該會與s相同，
    # 那只能一個一個字符比對，會需要用到一個for迴圈，
    # 裡面t的字串會一個一個去比對s的字串，像是第一次迴圈，t的字串中第0個字符是p，
    # 那他會去s的字串中，從0開始到len(s)去比對，那他比對到的是s的第1個字符，
    # 比對過的就要被拿出來，所以s還剩下0、2、3、4個字符，
    # 然後t就繼續拿他的第1個字符l去跟s的字串比對，然後持續下去。
    # 如果s都被拿光，則回傳true，否則為false

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) == len(t):  # 如果s跟t的長度一樣，才開始執行
#             s_list = list(s)
#             # for i in range(len(t)): # 這裡i拿到的是0 1 2
#             for char in t:  # 這裡char拿到的是t的字串中的每個字符 a b c
#                 if char in s_list:
#                     s_list.remove(char)  # 移除已比對過的字符
#                 else:
#                     return False  # 如果t的字符不在s中，則不是anagram
#             return True  # 如果s的字符都被比對完，則是anagram
#         return False  # 如果s跟t的長度不一樣，則不是anagram

# Hash Map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}  # 紀錄字串 s 中每個字元出現的次數
                    # 結構：{ 字元 : 出現次數 }
        # 邏輯：如果兩個字串長度根本不同，字元數量必然不可能相同，因此直接回傳 False 結束，避免後續不必要的計算。
        if len(s) == len(t):
            for char in s:  # 統計字串 s 的字元頻率
                # 嘗試取得 char 的次數，如果字典裡還沒有這個字元，就預設回傳 0
                # 否則把該字元的出現次數加 1
                # 範例：若 s = "aab"，跑完這個迴圈後
                # count 會變成 {'a': 2, 'b': 1}
                count[char] = count.get(char, 0) + 1
            for char in t:  # 用字串 t 扣抵次數並檢查
                # 1、如果 char 不在字典裡（get 拿到 0），
                    # 代表 t 出現了 s 完全沒有的字元
                # 2、如果 count[char] 已經被扣到 0 了，
                #   代表 t 中該字元出現的次數超過了 s 所擁有的數量
                if count.get(char, 0) == 0:
                    return False
                else:
                    count[char] = count[char] - 1   # 通過檢查後，把該字元在字典中的剩餘次數扣掉 1
        else:
            return False
        return True
    
sol = Solution()
result1 = sol.isAnagram(s="anagram", t="nagaram")
result2 = sol.isAnagram(s="rat", t="car")
result3 = sol.isAnagram(s="a", t="ab")
print(result1, result2, result3)

# 加深理解：想像成去商店用「代幣」換東西
    # 例如 s = "aab"，字典 count 現在就像是：
    # a 代幣：有 2 個
    # b 代幣：有 1 個
# for ch in t:  拿出 t 裡面的下一個字母 ch，準備去字典核銷（扣掉）。
#     if count.get(ch, 0) == 0: 在扣除之前，先檢查：我們還有這個字母的代幣可以扣嗎？
        # 這裡的 count.get(ch, 0) 會拿到兩個結果之一：
            # 1、拿到 0（完全沒這個字母）：
                # 比如 t 裡面出現了字母 'c'，
                # 但 s 從來沒有 'c'，所以 get('c', 0) 回傳 0。
                    # 結論：t 拿了一個 s 根本沒有的字母，
                    # 兩邊不可能一樣，直接判定失敗 (return False)！
            # 2、原本有代幣，但已經被扣到剩 0 了（用光了）：
                # 假設 s = "aab"（只有 2 個 a），
                # 但 t = "aaa"（有 3 個 a）。
                # 當 t 處理到第 3 個 a 時，
                # 前兩個 a 已經把代幣透支完了，此時 count['a'] 變成 0。
                # 這次 get('a', 0) 又拿到 0！
                    # 結論：t 裡面的這個字母數量太多了（超過了 s 擁有的數量），
                    # 直接判定失敗 (return False)！
#         return False
#     count[ch] -= 1    檢查通過（代表還有代幣），順利扣掉 1 個代幣！