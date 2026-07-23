# 題目：
    # 你正在記錄一場規則奇特的棒球比賽的比分。比賽開始時，記錄簿上沒有任何分數。
    # 給定一個字串列表operations，其中operations[i]是要套用於記錄的操作，是以下選項之一：
    # 一個整數x，記錄一個新的分數
    # +：記錄一個新的分數，該分數是前兩個分數的總和。
    # D：記錄一個新的分數，該分數是前一個分數的兩倍。
    # C：使先前的分數無效，並將其從記錄中刪除。
    # 全部處理完，回傳紀錄簿上所有分數的總和。

# 想法：
    # 問題一：為什麼這題要用堆疊？
        # C先前的分數無效是指[-1]，
        # D前一個分數的兩倍是指[-1]
        # +前兩個分數的總和是指[-2]跟[-1]
    # 問題二：資料型別
        # operations是字串，要加法乘法要用數字，用list存。
            # 把東西放進 stack 之前，要對它做什麼？
                # int(char)
    # 問題三：+ 到底有沒有「吃掉」前兩筆？
        # + 對 stack 做的動作只是看兩眼，然後多放一個
    # 指令：
        # 數字：append(int(x))，要先字串轉數字
        # C：pop()，拿走最後一筆
        # D：([-1] * 2) + append()，看一眼[-1] * 2 放進去
        # +：[-1]、[-2] + append，看兩眼 [-2]、[-1]，相加，放進去

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:   # O(n)
            if op == "C":   # O(1)
                stack.pop() # 拿走最後一筆
            elif op == "D": # O(1)
                stack.append(stack[-1] * 2) # 看一眼[-1] * 2 放進去
            elif op == "+": # O(1)
                stack.append(stack[-2] + stack[-1]) # 看兩眼 [-2]、[-1]，相加，放進去
            else:   # O(1)
                stack.append(int(op))   # 字串轉數字
        result = sum(stack) # 加總 O(n)
        return result

sol = Solution()
result1 = sol.calPoints(["5","2","C","D","+"])
result2 = sol.calPoints(["5","-2","4","C","D","9","+","+"])
result3 = sol.calPoints(["1","C"])
print(result1, result2, result3)