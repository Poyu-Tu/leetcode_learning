# 題目：
    # 給你兩個字串 s 和 t，裡面的 # 代表按了一次退格鍵（Backspace）。
    # 請判斷：把這兩個字串分別「打」進兩個空白的文字編輯器之後，
    # 最終顯示的內容是不是一樣？

# 想法：
    # 一開始會先建立兩個空stack，來後續存放予刪除s跟t的內容，
    # 會需要迴圈來走過整個字串，將所有字串放到stack中，
    # 在pop()的地方，一開始要先確認stack是不是空的，然後遇到#時，
    # 才pop掉[-1]的元素，
    # 最後用兩個list比對是否是相同的。
    # s跟t的做法一樣，可以直接寫一個函式包起來，然後再呼叫就好。

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # 兩個變數來接回傳值
        s_stack = self._pushAndPop(s)
        t_stack = self._pushAndPop(t)

        return s_stack == t_stack   # 比較後回傳true或false
    
    # 將s跟t都在做的事定義成一個方法
    # 因為是在class底下建立一個函式，所以第一個參數一定是self
    # st 是來接s或t的字串
    def _pushAndPop(self, st) -> list:
        stack = []  # 直接在這裡定義一個list，
                    # 因為在backspaceCompare定義的話會需要寫兩行，
                    # 在這裡可以直接用還不用接參數
        for char in st:
            # if char == "#" and stack: # 寫成這樣的話，當 # 且 stack 空被歸進了 else，
                                        # 而 else 的動作是 append會導致錯誤的結果!!!
            if char == "#": # 如果字元是#
                if stack:   # 如果stack中有東西

                    stack.pop()
            else:
                stack.append(char)  # 否則就加到stack中

        return stack    # 將stack這個list的內容回傳
                   
sol = Solution()
result1 = sol.backspaceCompare(s = "ab#c", t = "ad#c")
result2 = sol.backspaceCompare(s = "ab##", t = "c#d#")
result3 = sol.backspaceCompare(s = "a#c", t = "b")

print(result1, result2, result3)