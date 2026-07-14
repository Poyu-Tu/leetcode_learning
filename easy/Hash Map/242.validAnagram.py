# 給你兩個字串 s 跟 t,請你判斷 t 是不是由 s 重新排列組合而成的。

# 想法：如果s為apple，t是plaep，那t的字數及字符出現的數量都應該會與s相同，
# 那只能一個一個字符比對，會需要用到一個for迴圈，
# 裡面t的字串會一個一個去比對s的字串，像是第一次迴圈，t的字串中第0個字符是p，
# 那他會去s的字串中，從0開始到len(s)去比對，那他比對到的是s的第1個字符，
# 比對過的就要被拿出來，所以s還剩下0、2、3、4個字符，
# 然後t就繼續拿他的第1個字符l去跟s的字串比對，然後持續下去。
# 如果s都被拿光，則回傳true，否則為false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):  # 如果s跟t的長度一樣，才開始執行
            s_list = list(s)
            # for i in range(len(t)): # 這裡i拿到的是0 1 2
            for char in t:  # 這裡char拿到的是t的字串中的每個字符 a b c
                if char in s_list:
                    s_list.remove(char)  # 移除已比對過的字符
                else:
                    return False  # 如果t的字符不在s中，則不是anagram
            return True  # 如果s的字符都被比對完，則是anagram
        return False  # 如果s跟t的長度不一樣，則不是anagram
    
sol = Solution()
result1 = sol.isAnagram(s="anagram", t="nagaram")
result2 = sol.isAnagram(s="rat", t="car")
result3 = sol.isAnagram(s="a", t="ab")
print(result1, result2, result3)