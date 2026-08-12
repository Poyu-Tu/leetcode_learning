# 題目：(固定長度視窗)
    # 給你兩個字串 s1 和 s2，問 s2 裡面是否存在一個「連續子字串」，剛好是 s1 的某個排列（permutation）。
    # 例如 s1 = "ab"，s2 = "eidbaooo" → 裡面有 "ba"，是 "ab" 的排列，回傳 True。

# 想法：
    # 想像你手上有一張採購清單（s1 需要哪些字元、各要幾個），然後你透過一個固定大小的「取景窗」看著 s2，
        # 窗口裡目前手上有的字元組合，要跟採購清單完全吻合才算通過。 >> 用字典去紀錄s1
        # s1 = "ab"
        # s1_count = {}
        # for char in s1:
        #     s1_count[char] = s1_count.get(char, 0) + 1
    # 視窗（在 s2 上滑動的那個窗口）要怎麼記錄它目前手上的字元次數？
        # 這個視窗大小固定是 len(s1)，它會在 s2 上一格一格往右移動。
        # 跟採購清單不同的地方在於——採購清單建一次就不變，但視窗內容是動態的，每次往右移動一格，會發生什麼事？
        # >> 新的字元進來 +1，被踢出去的字元 -1
    # 怎麼判斷「視窗字典」跟「採購清單」是同一份東西？
        # Python 判斷字典相等，是連 key 有沒有存在都算進去的，不是只看「有意義的次數」。
        # 當視窗左邊的字元被踢出去、次數 -1 之後，如果剛好變成 0，你會讓這個 key 留在字典裡（值是 0），還是想辦法讓它從字典裡消失？
            # >> 想辦法讓它從字典裡消失，這樣才不會影響後續的判斷。
            # 踢出左邊字元這個動作，只會在視窗往右移動、左邊需要收縮的那個時間點發生一次，不是對整個 s2 跑迴圈。
            # left_char = s2[left]  # 左邊被踢出去的舊字元
            # window_count[left_char] = window_count[left_char] - 1
            # if window_count[left_char] == 0:
            #     del window_count[left_char]   # 删除某个 key
    # 把新字元拿進來
        # right_char = s2[right]  # 新的字元進來
        # window_count[right_char] = window_count.get(right_char, 0) + 1
    # 每次 right 前進一步，視窗大小最多超出 1，而踢一個字元剛好能讓它「一次到位」變回合法
    # 程式碼架構：  
        # 1. 新字元進來 (你剛剛寫的那段)
        # 2. 判斷視窗是否超過大小，超過就踢一個 (用 if，不是 while)
        # 3. 判斷 window_count 是否等於 s1_count，相等就回傳 True
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_count = {}  # 採購清單，s1 需要哪些字元、各要幾個
        window_count = {}   # 視窗目前手上的東西(會一直變)
        left = 0 # 視窗左邊界,負責把舊字元「踢出去」

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        for right in range(len(s2)):
            # 1. 新字元進來
            right_char = s2[right]  # 新的字元進來
            window_count[right_char] = window_count.get(right_char, 0) + 1

            # 2. 判斷視窗是否超過大小，超過就踢一個 (用 if，不是 while)
            if right - left + 1 > len(s1):
                left_char = s2[left]  # 左邊被踢出去的舊字元
                window_count[left_char] = window_count[left_char] - 1
                if window_count[left_char] == 0:
                    del window_count[left_char]   # 删除某个 key
                left = left + 1

            # 3. 判斷 window_count 是否等於 s1_count，相等就回傳 True
            if window_count == s1_count:
                return True

        return False

sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))  # Should print True
print(sol.checkInclusion("ab", "eidboaoo"))  # Should print False