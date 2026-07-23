# 題目：
    # 給你一個只含小寫英文字母的字串 s。
    # 你可以重複執行這個動作：選兩個相鄰且相同的字母，把它們一起刪掉。
    # 一直做到沒有任何相鄰重複為止，回傳最後剩下的字串。題目保證答案唯一。
    # EX："abbaca" >> "ca" / "azxxzy" >> "ay"

# 想法：
    # 假如s = "abbaca"，建立一個空的list temp_stack，2; 
    # 假設當掃到第三個字元時發現重複，則將目前這個及上一個字元做pop()
        # 將目前這個及上一個字元做pop()：
            # 這裡因為目前看得這個還沒被放入list中，所以可以先去確認再去改動
            # 可以使用[-1]確認list最頂端的元素
            # 架構：
                # 建立一個空清單 stack
                # 從左到右掃過 s 的每一個字元 char:
                #     如果 (籃子不是空的) 而且 (籃子最上面 == char):
                #         把籃子最上面拿掉        ← 消除
                #     否則:
                #         把 char 放進籃子        ← 存起來等以後配對
                # 回傳 ???
                    # (籃子不是空的) 而且 (籃子最上面 == char)
                        # >> 短路求值 左邊是true才繼續右邊
                    # 回傳：
                        # 使用"".join() 用空字串當作「連接符」,把 list 裡每個元素接在一起

class Solution:
    def removeDuplicates(self, s: str) -> str:
        temp_stack = []
        for char in s:  # O(n)
            if temp_stack and temp_stack[-1] == char:   # if temp_stack >> 如果籃子裡有東西
                temp_stack.pop()    # 消除 O(1)
            else:
                temp_stack.append(char) # 存起來 O(1)

        result = "".join(temp_stack)    # O(n)
        return result

sol = Solution()
result1 = sol.removeDuplicates("abbaca")
result2 = sol.removeDuplicates("azxxzy")
print(result1, result2)
