# 題目：(可變視窗)
    # 給你一個只包含大寫英文字母的字串 s，和一個整數 k。
    # 你可以選擇字串中任意最多 k 個字元，把它們替換成任意其他大寫字母。
    # 求：經過這樣的替換後，能得到的「全部由同一字元組成」的最長子字串長度?
        # 輸入: s = "ABAB", k = 2
        # 輸出: 4
        # 解釋: 把兩個 'A' 換成兩個 'B'，或反過來，可以得到 "BBBB" 或 "AAAA"。
        
        # 輸入: s = "AABABBA", k = 1
        # 輸出: 4
        # 解釋: 把第一個字串中間的 'A' 換成 'B'，得到 "AABBBBA"。
        # 子字串 "BBBB" 長度為 4。

# 想法：
    # 選擇數量多的當成主要的，替換起來才最划算。
    # 換的次數 = 視窗長度 - 數量最多的字母
    # 合法 >> 視窗長度 - 數量最多的字母 <= k(換的次數)
    # 視窗內最多的那個字元的出現次數怎麼追蹤？ >> 用dict
    # right 每向右一格，判斷是否為新的字母，如果是則將她加入dict中並給她1的數值，
        # 如果不是新的字母，則將這個字母再加1。
    # 數量最多的字母 >> 每次都跟目前最高紀錄比大小
    # 視窗長度 - 數量最多的字母 > k(換的次數) >> 不合法，left 要開始移動
        # left 移動，要同時對 dict 的值 -1。

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        max_count = 0   # 計算視窗內出現次數最多的字元數量(字典裡)
        max_len = 0 # 「全部由同一字元組成」的最長子字串(答案)
        d = {}

        for right in range(len(s)):
            # 更新目前字元在字典中的出現次數
            d[s[right]] = d.get(s[right], 0) + 1
            # 更新當前視窗內出現次數最多的字元數量
            max_count = max(max_count, d[s[right]])

            # 如果需要替換的字元數超過 k，代表視窗不合法
            while (right - left + 1) - max_count > k:
                # 將字典中left的值減少
                d[s[left]] = d[s[left]] - 1
                # 然後left向右移動
                left = left + 1
                
            # 更新最長合法視窗的長度
            max_len = max(max_len, right - left + 1)

        return max_len

sol = Solution()
r1 = sol.characterReplacement(s = "ABAB", k = 2)
r2 = sol.characterReplacement(s = "AABABBA", k = 1)

print(r1, r2)

