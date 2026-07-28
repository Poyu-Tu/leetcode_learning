# 題目：
    # 設計一個堆疊，除了支援一般的 push、pop、top 之外，
    # 還要能在常數時間內取得堆疊裡的最小元素。

    # 實作一個 MinStack 類別，包含以下方法：
        # MinStack()：初始化一個空的堆疊
            # push(int：val)：把 val 推入堆疊頂端
            # pop()：移除堆疊頂端的元素
            # top()：回傳堆疊頂端的元素（不移除）
            # getMin()：回傳堆疊裡目前最小的元素
    # 關鍵限制： 上面四個方法，每一個都必須是 O(1) 時間複雜度。

# 想法：
    # 會需要一個可以記錄最小值的變數 min_val，
    # 在push的時候，會去記錄他，然後在pop的時候也會去記錄他
        # 變成需要兩個堆疊：
            # 1. self.stack —— 正常存數值，負責 push / pop / top
            # 2. 另一個容器 —— 負責記住「最小值」的歷史
                # 不需要比對整個容器，只需要比對一個東西：
                # 新來的 val，跟這個容器最上面那個（也就是「上一個的最小值」）。
                # 誰小就放誰進去。

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        # 原本寫法
        # self.stack.append(value)
        # if not self.min_stack:  # self.min_stack裡沒有值
        #     self.min_stack.append(value)    # 把value加進去
        # elif value <= self.min_stack[-1]:   # 現在的值<=self.min_stack頂端的值
        #     self.min_stack.append(value)    # 把value加進去
        # else:
        #     self.min_stack.append(self.min_stack[-1])   # 把目前頂端的值加進去

        # 可以使用min(a, b)這個方法優化
        self.stack.append(value)
        if not self.min_stack:  # self.min_stack裡沒有值
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))
            
    # push 無條件新增，那pop必須也要無條件移除
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]

obj = MinStack()
print(
obj.push(-2), 
obj.push(0), 
obj.push(-3), 
obj.getMin(), 
obj.pop(), 
obj.top(), 
obj.getMin()
)