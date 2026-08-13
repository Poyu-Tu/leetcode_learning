# 題目：(固定長度視窗)
    # 給定兩個字串 s 和 p，找出 s 中所有是 p 的字母異位詞（anagram）的子字串的起始索引，回傳這些索引組成的陣列（順序不拘）。
    # 字母異位詞：由相同字母組成、但排列順序可以不同的字串。例如 "abc" 和 "cab" 互為異位詞。
        # 範例：
        # 輸入: s = "cbaebabacd", p = "abc"
        # 輸出: [0, 6]
        # 解釋: 
        # 起始索引 0 的子字串是 "cba"，是 "abc" 的異位詞。
        # 起始索引 6 的子字串是 "bac"，是 "abc" 的異位詞。
        # 輸入: s = "abab", p = "ab"
        # 輸出: [0, 1, 2]
        # 解釋:
        # 起始索引 0 的子字串是 "ab"，是異位詞。
        # 起始索引 1 的子字串是 "ba"，是異位詞。
        # 起始索引 2 的子字串是 "ab"，是異位詞。

# 想法：
    # 視窗大小固定之後，怎麼判斷「視窗內的子字串」跟 p 是不是異位詞？
        # 換句話說，你要拿什麼東西去比較？
        # 用生活化一點的方式想想看——如果你手上有一把「p 需要的字母清單」，你要怎麼確認視窗裡的字母，跟這份清單完全對得上？
            # >> 用字典去紀錄 p
                # need：記錄 p 裡每個字母需要的次數
                # window：記錄目前視窗裡每個字母的次數
    # 因為固定視窗每次 right 只前進一步，超出的量最多也只會是「多 1」，所以一次 if 收縮就能讓視窗大小回到 len(p)
    # 視窗每次 right 前進，會發生三件事：
        # 把 s[right] 加入 window
        # 判斷是否要收縮（把 s[left] 移除、left 前進）
        # 判斷視窗是否已經跟 need 一樣大，若是則比對 window == need
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}  # 採購清單，p 需要哪些字元、各要幾個
        window = {}   # 視窗目前手上的東西(會一直變)
        left = 0 # 視窗左邊界,負責把舊字元「踢出去」
        ans = []  # 存放所有異位詞的起始索引
        for char in p:
            need[char] = need.get(char, 0) + 1

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if right - left + 1 > len(p):
                window[s[left]] = window[s[left]] - 1
                if window[s[left]] == 0:
                    del window[s[left]]   # 删除某个 key
                left = left + 1

            if window == need:
                ans.append(left)  # 找到一個異位詞的起始索引，加進ans
        return ans  # 輸出所有異位詞的起始索引

solution = Solution()
s = "cbaebabacd"
p = "abc"
print(solution.findAnagrams(s, p))  # [0, 6]
s = "abab"
p = "ab"
print(solution.findAnagrams(s, p))  # [0, 1, 2]