# 題目：(可變視窗)
    # 給你一個字串 s，找出不含重複字元的最長子字串的長度。
    # 注意是「子字串（substring）」＝ 連續的一段，不能跳著挑。
    # 範例：
        #       輸入	輸出	說明
        # "abcabcbb"	3	是 "abc"
        # "bbbbb"	    1	是 "b"
        # "pwwkew"	    3	是 "wke"

# 想法構建：
    # 視窗大小是答案，不是條件 → 變動視窗（橡皮筋），與 1004 同一家族。
        # 條件：視窗內不能有任何重複字元
        # 答案：符合條件時，視窗能撐到多長
    # left 和 right 都只往索引變大的方向走（往右），都不回頭。
        # right 往右移 → 從右邊加人 → 視窗變長
        # left 往右移 → 從左邊踢人 → 視窗變短
    # 用 set
        # 只需要知道字元「在不在」視窗裡，不需要知道出現幾次（出現第 2 次就已違規）→ 
        # 用 set 就夠，不用 dict。
    # 停止條件不是「window 裡沒有重複」，而是「那個跟新字元撞名的舊字元被踢掉了」。
        # 換句話說，你要一直踢，踢到 s[right] not in window 為止。
    # 結算放最後，因為只有合法的視窗才有資格被記錄。
        # 變動視窗的結算，永遠放在「確保視窗合法之後」。先修好，再記帳。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化
        left = 0    # 從最左邊開始跑
        max_len = 0
        window = set()  # 初始化一個set

        # 主迴圈（right 從頭走到尾），每步三件事
        # 檢查 & 收縮
        for right in range(len(s)):
            while s[right] in window:   # 已在視窗中，left 踢人
                window.remove(s[left])  # 移除在視窗中的 left 位置元素
                left = left + 1 # left 往右移一格
        # 如果不在視窗中，加入視窗
            window.add(s[right])
        # 結算
            max_len = max(max_len, right - left + 1) 

        return max_len

sol = Solution()
result1 = sol.lengthOfLongestSubstring("abcabcbb")
result2 = sol.lengthOfLongestSubstring("bbbbb")
result3 = sol.lengthOfLongestSubstring("pwwkew")

print(result1, result2, result3)
