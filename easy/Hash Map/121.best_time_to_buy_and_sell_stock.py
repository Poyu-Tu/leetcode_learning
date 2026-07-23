# 題目：
    # 給你一個陣列 prices,代表股票每一天的價格(prices[0] 是第一天的價格、prices[1] 是第二天...以此類推)。
    # 你只能買一次、賣一次,而且必須先買才能賣(不能先賣後買)。請你算出這樣操作下,最多能賺多少錢。如果怎麼買賣都賺不到錢,回傳 0。

# 想法：
    # 假設prices = [7, 1, 5, 3, 6, 4] ，我會用兩個for迴圈跑，
    # 外層假設取出第0個位置的數字prices[0]，然後在內層迴圈去跟後面的每一位數比，
    # 假設外層是prices[i]內層則要prices[i+1]，
    # 在內層，如果取出來的數字(7)>後面比較的所有數字(1, 5, 3, 6, 4)，則回到外層迴圈接續下一個prices[1]；
    # 如果取出來的數字(1)<後面比較的數字(5)，則將後面的數字減掉取出來的數字，然後我會存放到temp的變數中暫存，
    # 如果後面的數字減掉取出來的數字的結果，又有>temp的數字，則將temp設定為較大的數字。
    # 最後迴圈都跑完後，回傳temp的數字

# 暴力破解法
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         temp = 0  # 用來暫存最大利潤
#         for i in range(len(prices) - 1):  # 外層迴圈，固定買入的價格
#             for j in range(i + 1, len(prices)):  # 內層迴圈，賣出的價格
#                 if prices[j] - prices[i] > temp:  # 如果賣出價格 - 買入價格 > 暫存的最大利潤
#                     temp = prices[j] - prices[i]  # 更新最大利潤
#         return temp  # 回傳最大利潤
    
# sol = Solution()
# result1 = sol.maxProfit(prices=[7, 1, 5, 3, 6, 4])
# result2 = sol.maxProfit(prices=[7, 6, 4, 3, 1])
# print(result1, result2)

# 上面這會超時，因為時間複雜度是O(n^2)，所以要改成O(n)的解法。

# 想法2：
    # 需要準備now_cheap = max(prices)跟max_profit = 0，
    # 設定一個for迴圈，首先先看今天賣掉賺多少錢，就是用目前的prices[i] - now_cheap，
    # 如果>max_profit，更新max_profit，然後再進到第二個if，看看prices[i]是不是<now_cheap，
    # 如果是，則更新now_cheap，都跑完後，回傳max_profit
    # max(prices) 這個函式本身,需要先把整個陣列 prices 完整掃過一遍才能找到最大值(這也是一次 O(n) 的操作)。
    # 如果不用 max(prices),而是直接用 prices[0](陣列的第一天價格)當作 now_cheap 的初始值,結果會一樣嗎?

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        now_cheap = prices[0]  # 記錄目前最便宜的價格
        max_profit = 0  # 記錄最大利潤
        for i in range(len(prices)):
            if prices[i] - now_cheap > max_profit:  # 如果當前價格 - 最便宜的價格 > 最大利潤
                max_profit = prices[i] - now_cheap  # 更新最大利潤
            if prices[i] < now_cheap:  # 如果當前價格 < 最便宜的價格
                now_cheap = prices[i]  # 更新最便宜的價格
        return max_profit  # 回傳最大利潤

sol = Solution()
result1 = sol.maxProfit(prices=[7, 1, 5, 3, 6, 4])
result2 = sol.maxProfit(prices=[7, 6, 4, 3, 1])
print(result1, result2)