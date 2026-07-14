# 給你兩個字串 s 和 t，判斷它們是否為「同構」(isomorphic)。
# 也就是說，s 中的每個字元都可以被「替換」成另一個字元，得到 t。
# 但這個替換規則必須滿足：
# 1、相同的字元必須被替換成相同的字元
# 2、不同的字元不能被替換成相同的字元（也就是不能「多對一」）

# 舉例：
# s = "egg", t = "add" → true（e→a, g→d）
# s = "foo", t = "bar" → false（f→b, o→a, 但第二個 o 卻要對應 r，矛盾！）

# zip() 就是很適合這裡用的函式。生活例子：
# 假設你有兩排學生要「配對」，
# 一排是 s = ['e', 'g', 'g']，另一排是 t = ['a', 'd', 'd']。
# zip(s, t) 做的事情，就像老師喊「一號配一號、二號配二號、三號配三號」，
# 把兩排「同位置」的人綁成一對一對，變成：('e', 'a'), ('g', 'd'), ('g', 'd')

# 想法：建立兩個空的字典s_dict跟t_dict，分別記錄s跟t的對應關係，
# 然後用zip()迴圈的方式，將s跟t逐一配對，假設
# s = 'egg'
# t = 'add'
# 配對完應該會是('e', 'a'), ('g', 'd'), ('g', 'd')，
# 檢查char_s有沒有在s_dict中出現過，如果沒有，新增char_t進去；
# 如果有，檢查對應字元是否一致，如果不一致，回傳false；
# 如果一致，進到下一個if-else中，檢查char_t的部分，
# 如果又一致，在迴圈外面回傳true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False
        else:
            # 假如遇到長短不一樣的情況，
            # zip()以「較短」的那個字串為準，
            # 多出來的部分直接忽略，不會報錯，也不會補空值。
            for char_s, char_t in zip(s, t): 
                if char_s not in s_dict:
                    s_dict[char_s] = char_t
                elif s_dict[char_s] != char_t:
                    return False
                
                if char_t not in t_dict:
                    t_dict[char_t] = char_s
                elif t_dict[char_t] != char_s:
                    return False
            return True
        
sol = Solution()
print(sol.isIsomorphic("egg", "add")) # True
print(sol.isIsomorphic("foo", "bar")) # False

