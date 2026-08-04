# 題目：(固定長度視窗)
    # 給你一個字串 s 和整數 k，找出所有長度為 k 的子字串中，
    # 母音（a、e、i、o、u）數量最多的是幾個。
        # s = "abciiidef", k = 3  →  3   （"iii"）
        # s = "aeiou", k = 2      →  2
        # s = "leetcode", k = 3   →  2   （"lee"、"eet"...）

# 想法構建：
    # 滑動視窗裡要維護的是包含aeiou的數量
    # 移出移入時的數字變化量是-1/0/+1，移出移入這邊要用if，取決於進出的字元「是不是母音」
    # 判斷「某個東西在不在一堆東西裡」→ 反射性想到 set。

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        now_window = 0  # 當前視窗總和，每輪必更新

        # 1.母音用 set 存
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # 2.先算出第一個視窗（前 k 個字元）的母音數，直接當初始冠軍
        for c in range(k):
            if s[c] in vowels:  # 如果有在vowels中
                now_window = now_window + 1 # 將滑動視窗+1

        max_vowels = now_window # 第一個視窗直接當初始冠軍

        # 3.從第 k 個字元開始滑動：移出左邊（是母音才 -1）、移入右邊（是母音才 +1）
        for c2 in range(k, len(s)):
            if s[c2 - k] in vowels: # 如果最左邊的是母音則-1
                now_window = now_window - 1
            if s[c2] in vowels:   # 如果最右邊的是母音則+1
                now_window = now_window + 1

        # 4.每滑一次就更新最大值
            if now_window > max_vowels:
                max_vowels = now_window

        return max_vowels

sol = Solution()
result1 = sol.maxVowels("abciiidef", 3)
result2 = sol.maxVowels("aeiou", 2)
result3 = sol.maxVowels("leetcode", 3)

print(result1, result2, result3)

