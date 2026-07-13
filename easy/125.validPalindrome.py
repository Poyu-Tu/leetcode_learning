# 題目描述:
# 給你一個字串 s,先忽略所有「非英數字元」(標點符號、空白等),
# 並把所有英文字母轉成小寫,判斷這個字串是否為「回文」(palindrome,也就是正著讀和反著讀是一樣的)。
# 也就是正讀反讀都一樣

# 想法：
    # 可以使用.isalnum()這個方法來判斷是否為數字或字元
    # 我會先在外面先建立一個空字串，用來存放判斷為字元或數字的字浮，同時可以去掉標點符號及空白
    # 然後進入一個for迴圈中，走過s這個字串，如果是字串的話，就新增到空字串中，
    # 最後再將空字串轉成小寫。
    # 然後會需要再從最後面走回來跟空字串比對，如果是一樣的話就是true，否則為false。
# 問題：
    # 1.字串特性為不可變，等於需要重新建立一個新字串，把舊的內容加上新字元，在整個複製一份。(On x n)
        # 可以用list，搭配.append()，最後再用.join()把list轉成字串。
    # 2.[::-1] >> 可以使用雙指標的新方法，從前面跟後面同時走，直到兩個指標相遇為止。
    # 3.不知道要跑幾次迴圈的 >> 用while true。

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for char in s:
            if char.isalnum():
                temp.append(char)
        listToStr = "".join(temp) # 用空字串當作「連接符」,把 list 裡每個元素接在一起
        cleaned = listToStr.lower() # 轉小寫

        left = 0
        right = len(cleaned) - 1 # 從最後開始
        while left < right:
            if cleaned[left] == cleaned[right]:
                left = left + 1
                right = right -1
            else:
                return False
        return True
    
sol = Solution()
result1 = sol.isPalindrome("A man, a plan, a canal: Panama")
result2 = sol.isPalindrome("race a car")
result3 = sol.isPalindrome(" ")
print(result1, result2, result3)


    