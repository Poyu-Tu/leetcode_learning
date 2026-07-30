# 題目：(維持一個有順序的狀態)>>單調遞迴堆疊
    # 給一個陣列 temperatures，代表每天的溫度。
    # 請回傳一個陣列 answer，其中 answer[i] 表示：
    # 第 i 天之後，要再等幾天才會遇到比今天更溫暖的一天。
    # 如果之後都沒有更溫暖的一天，就填 0。

    # 範例
    # 輸入：temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # 輸出：[1, 1, 4, 2, 1, 1, 0, 0]

# 重點：
# 1. 找右邊第一個比自己大的溫度 >> 要的是距離，隔了幾天(減法)
# 2. 堆疊裡該存什麼，才有辦法做這個減法 >> 該存index
# 3. 比較大小的時候怎麼辦 >> 要比的是溫度 用 temperatures[i] 去查，index 是「查表的鑰匙」
# 4. 堆疊裡的內容是index，但對應到的溫度是呈現降冪的狀態
# 5. 最後「留在堆疊裡」的天數，代表沒有比他熱的一天 >> 回傳0
    # 小技巧：如果答案陣列一開始就用 0 填滿，
    # 那留在堆疊裡的根本不用特別處理 —— 它們的位置本來就是 0。

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)    # 預設 0：等不到更熱的日子就維持 0，不用另外處理
        day = []    # 存「還在等答案」的 index

        for index, t in enumerate(temperatures):    # 同時取出陣列中每個元素的位置與數值
                                                    # index >> 今天天氣的索引（Index），從 0 開始
                                                    # t >> 今天天氣的索引對應到的溫度
            # 今天比排隊中那幾天都熱
            while day and temperatures[day[-1]] < t:
                pop_index = day.pop()    # 將小的溫度彈出(等待那天)
                answer[pop_index] =  index - pop_index    # 用大溫度的索引-小溫度的索引，答案屬於「等待的那天」，不是今天

            day.append(index)

        return answer

sol = Solution()
temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]
result1 = sol.dailyTemperatures(temperatures1)
result2 = sol.dailyTemperatures(temperatures2)
result3 = sol.dailyTemperatures(temperatures3)
print(result1, result2, result3)