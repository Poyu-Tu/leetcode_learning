# 題目描述:
# 給你一個字元陣列 s(注意是 List[str],不是字串本身),
# 請你原地(in-place) 把它反轉,不能回傳新的陣列,也不能開額外的陣列來存結果。
# 不能：s = s[::-1] >> 建立一個新的 list 再指派回去,不算原地

# 想法：使用雙指標概念，從s 的最外圍開始做交換，然後慢慢往內縮。

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
        # 通用寫法
            # temp = s[left]
            # s[left] = s[right]
            # s[right] = temp
        # python可以這樣寫:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1
        # print(s)
        
sol = Solution()
result1 = sol.reverseString(["h","e","l","l","o"])
result2 = sol.reverseString(["H","a","n","n","a","h"])
