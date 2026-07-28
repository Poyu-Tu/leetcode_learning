# 題目：
    # 只能用堆疊（stack）的操作，去實作出一個佇列（queue）。
    # 實作 MyQueue 類別：
        # push(x)：把 x 放到佇列尾端
        # pop()：移除並回傳佇列前端的元素
        # peek()：回傳佇列前端的元素（不移除）
        # empty()：佇列是不是空的
    # 限制： 你只能用 stack 的標準操作——
        # append（推入尾端）、pop()（從尾端拿出）、[-1]（看尾端）、len()。
        # 不能用 pop(0)、不能用 insert(0, x)、
        # 不能直接把 list 當 queue 用。

# 想法：
    # 使用第二個stack，在pop的功能裡，
    # 把第一個stack裡的東西，一個個pop出來，
    # 再一個個append到第二個stack，這樣取[-1]時，就可以拿到最前面的了
        # 當第二個stack空的時候再將第一個stack倒進來，
        # 避免拿到第一個stack後面進來的，
        # 因為題目是要在pop()時，移除最前面的元素
    # push(x)：丟進stack1就好，不用管stack2
    # pop()：先確認第二個stack有沒有東西，如果沒有才將第一個stack的內容倒進第二個stack，
        # 然後從第二個stack pop掉
    # peek()：看一眼第二個stack最後的元素
    # empty()：確認兩個stack是不是都空的

class MyQueue:

    def __init__(self):
        self.stack1 = []    # 紀錄push進去的
        self.stack2 = []    # 負責將stack變成queue的

    def push(self, x: int) -> None:
        self.stack1.append(x)   # 丟進stack1就好

    def pop(self) -> int:
        self._transfer()
        return self.stack2.pop()

    def peek(self) -> int:
        self._transfer()
        return self.stack2[-1]

    def empty(self) -> bool:
        # 原寫法
        # if not self.stack1 and not self.stack2:
        #     return True
        # return False

        #簡短寫法
        return not self.stack1 and not self.stack2
    
    def _transfer(self) -> None:    # _ = 內部用、外部不該呼叫
        if not self.stack2: # 先確認第二個stack沒有東西
            while self.stack1:   # 當stack1有東西就執行
                s1_pop = self.stack1.pop()  # 把第一個stack裡的東西，一個個pop出來
                self.stack2.append(s1_pop)  # 一個個append到第二個stack

obj = MyQueue()
print(
obj.push(1), 
obj.push(2), 
obj.peek(),  
obj.pop(), 
obj.empty()
)