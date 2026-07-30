# Two Pointers 系列筆記

> LeetCode 刷題筆記 · Python
> 題目：125, 344, 283, 26, 977, 88, 167

---

## 一、什麼時候該想到 Two Pointers

**核心前提：順序本身就是線索。**

Hash map 會弄丟順序，two pointers 剛好相反——它**完全靠順序吃飯**。所以判斷第一步永遠是問：

> 這筆資料排序了嗎？或者「相對順序」對答案有意義嗎？

如果答案是「有」，那雙指標通常可以把 hash map 的 O(n) 空間降到 **O(1)**。

### 判斷訊號

- 題目明講 **sorted / 已排序**
- 要求 **in-place（原地修改）**、不能用額外陣列
- 回文、反轉、對稱
- 從兩端往中間夾
- 移除 / 搬移 / 去重，且要保持相對順序

---

## 二、兩種模型（一定要分清楚）

### 模型 A：對撞型（左右夾擊）

兩個指標從**兩端往中間走**，直到相遇。

**生活比喻**：兩個人從走廊兩端往中間走，一起找中間的東西。太重就右邊的人往左退一步，太輕就左邊的人往右進一步。

```python
left, right = 0, len(arr) - 1
while left < right:
    # 根據判斷決定縮哪一邊
    ...
```

**適用**：已排序陣列找兩數和、回文檢查、反轉、由大到小/由小到大填值。

**為什麼有效**：因為排序過，所以「和太小」這件事只有一種補救方式（左指標右移），不會漏解。

---

### 模型 B：快慢型（同方向）

兩個指標**同方向前進**，速度不同。

**生活比喻**：整理書架。
- **慢指標** ＝ 已整理好的區域的下一個空位
- **快指標** ＝ 正在檢查的那本書

快指標一路往前掃，遇到「合格」的書就搬到慢指標的位置，然後慢指標才前進一格。不合格的書快指標就直接跳過。

```python
slow = 0
for fast in range(len(nums)):
    if 合格條件:
        nums[slow] = nums[fast]
        slow += 1
```

**適用**：原地移除元素、去重、把某類元素搬到後面。

> 26 和 283 用的是**完全一樣的骨架**，只有中間那個「合格條件」不同。認出這件事之後，這類題目就不用重想了。

---

### 兩種模型怎麼選

| 問自己 | 選 |
| --- | --- |
| 要找一組符合條件的**配對**，而且資料已排序 | 對撞型 |
| 要**原地整理**陣列（刪、搬、去重） | 快慢型 |
| 要從兩端比較（回文、反轉） | 對撞型 |

---

## 三、常見陷阱（自己踩過的）

1. **`while left < right` vs `while left <= right`**
   - 用 `<`：中間那一格**不會**被處理。回文、反轉可以用（中間那格跟自己比，沒意義）。
   - 用 `<=`：中間那格**會**被處理。當每個元素都必須經手時要用這個。

2. **兩個獨立的 `if` 會在同一圈裡執行兩次**
   多分支的指標邏輯請用 `if / elif / else`，不然一圈之內指標可能被移動兩次，直接跳過元素。

3. **Python 負索引的坑**
   指標減到 `-1` 時，`arr[-1]` **不會報錯**，它會繞回去拿最後一個元素。這種 bug 不會 crash，只會默默算錯。凡是指標可能變負的地方，都要先檢查 `if p >= 0`（見 88）。

4. **由後往前填，必須先預留空間**
   `[0] * n` 先配置好陣列，不能用 `append()`——`append` 只能從尾巴長，沒辦法指定「填在第 i 格」（見 977）。

5. **搬移時可能覆蓋掉還沒處理的值**
   當 `slow` 和 `fast` 指到不同位置時要用**交換**而不是**覆寫**，否則原本在 `slow` 位置的值會被蓋掉（見 283）。

6. **`sorted()` vs `.sort()`**
   - `sorted(arr)` 回傳**新的 list**，原本的不動
   - `arr.sort()` **原地**排序，回傳 `None`
   題目要求 in-place 時用後者；但要注意排序本身是 O(n log n)，可能反而拖垮複雜度。

---

## 四、題目

### 125. Valid Palindrome

忽略大小寫與非英數字元，判斷是否為回文。

**思路**：對撞型的標準款。左右各派一個指標往中間走，遇到不是英數的字元就跳過。

```python
def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

**內層 while 也要寫 `left < right`**：不然全是符號的字串（例如 `".,"`）會讓指標一路衝出邊界。

**這裡用 `<` 不用 `<=`**：奇數長度時中間那個字元跟自己比一定相等，不用檢查。

| | 複雜度 |
| --- | --- |
| 時間 | O(n)（兩個指標加起來總共只走 n 步） |
| 空間 | O(1) |

---

### 344. Reverse String

原地反轉字元陣列。

**思路**：對撞型最單純的形態，左右交換再各往中間收一步。

```python
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

**Python 慣用法**：`a, b = b, a` 這種 tuple unpacking 交換，不需要暫存變數。右邊會先整個算完再賦值給左邊。

| | 複雜度 |
| --- | --- |
| 時間 | O(n)（實際只跑 n/2 圈，係數丟掉） |
| 空間 | O(1) |

---

### 283. Move Zeroes

把所有 0 移到最後面，其餘元素保持相對順序，且要原地做。

**思路**：快慢型。慢指標守著「下一個非零元素該放的位置」，快指標負責掃描。

```python
def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            if slow != fast:                              # 關鍵守衛
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

**為什麼用交換而不是覆寫？**
如果直接寫 `nums[slow] = nums[fast]`，原本在 `slow` 位置的那個 0 就被蓋掉了，最後還得再補一輪把尾巴填 0。用交換的話 0 會自動被推到後面去，一趟解決。

**`if slow != fast` 這個守衛的意義**：兩個指標重疊時（例如開頭一連串都是非零），交換等於自己跟自己換，白做工。

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(1) |

---

### 26. Remove Duplicates from Sorted Array

已排序陣列原地去重，回傳去重後的長度。

**思路**：跟 283 **同一個骨架**，只換中間的判斷條件。

因為已排序，**重複的元素必定相鄰**——所以只要跟「上一個已保留的元素」比就夠了，不需要 hash map。

```python
def removeDuplicates(nums):
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
```

**這裡 `slow` 的語意跟 283 略有不同**：283 的 `slow` 是「下一個空位」，這裡的 `slow` 是「最後一個已保留元素的位置」。所以回傳長度要 `+1`。

**fast 從 1 開始**：第 0 個元素必定保留，不用比。

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(1) |

---

### 977. Squares of a Sorted Array

已排序（可能含負數）陣列，回傳各元素平方後的排序結果。

**思路**：直接平方再 `sort()` 是 O(n log n)。要做到 O(n) 的關鍵洞見是：

> 平方之後**最大值一定出現在兩端**（因為最負的數平方後也很大）。

所以用對撞型比較兩端的絕對值，大的先取——但因為是**從大到小**取出，結果陣列要**從後往前填**。

```python
def sortedSquares(nums):
    n = len(nums)
    result = [0] * n                 # 必須預先配置，不能用 append
    left, right = 0, n - 1

    for i in range(n - 1, -1, -1):   # i 從 n-1 倒數到 0
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1

    return result
```

**為什麼不能 `append()`？**
`append` 只會往尾巴接，但我們是「先算出最大的」，最大的必須放在**最後一格**。要指定位置就得先有那個位置存在 → `[0] * n`。

**邊界檢查**：全正數（左指標一路不動）、全負數（右指標一路不動）、單一元素——這三種都要手動走一遍確認。

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(n)（題目要求回傳新陣列，不算額外開銷） |

---

### 88. Merge Sorted Array

把 nums2 合併進 nums1（nums1 尾端已預留 n 個空位），原地完成。

**思路**：從前面往後合併會覆蓋掉 nums1 還沒處理的元素。反過來**從後往前填**就不會——因為尾巴那 n 格本來就是空的。

生活比喻：兩排已經排好隊的人要合成一排，從**隊尾**開始比誰最高，最高的先站到新隊伍的最後面。

```python
def merge(nums1, m, nums2, n):
    p1 = m - 1          # nums1 有效資料的尾端
    p2 = n - 1          # nums2 的尾端
    p = m + n - 1       # 要填入的位置

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
```

**兩個關鍵設計**：

1. **迴圈條件只看 `p2 >= 0`**
   如果 nums2 先跑完，剩下的 nums1 元素本來就已經在正確位置上了，不用動。反之 nums1 先跑完，nums2 剩下的還得搬過去，所以要繼續。

2. **`if p1 >= 0 and ...` 這個檢查是必須的**
   `p1` 減到 `-1` 時，`nums1[-1]` 在 Python 不會報錯，它會拿到**陣列最後一格**——那格是我們剛剛才填進去的值，直接算錯。這種 bug 不會 crash，只會默默給錯答案。

| | 複雜度 |
| --- | --- |
| 時間 | O(m + n) |
| 空間 | O(1) |

---

### 167. Two Sum II — Input Array Is Sorted

已排序陣列找兩數和等於 target，回傳 **1-indexed** 索引。

**思路**：這題是理解 two pointers 價值的最佳範例。跟 LeetCode 1 是同一個問題，唯一差別是**輸入排序了**。

- 題目 1：沒排序 → 順序無意義 → 只能 hash map，空間 O(n)
- 題目 167：已排序 → 順序是線索 → 對撞型，空間 **O(1)**

**為什麼排序後就能對撞？**
因為和太小的時候，你**確定**只有把左指標右移才可能變大（右移左指標 = 換一個更大的數）；和太大就只能把右指標左移。方向是唯一的，所以不會漏解。

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]   # 題目要 1-indexed
        elif total < target:
            left += 1
        else:
            right -= 1

    return []
```

**`+1` 的坑**：題目說明是 1-indexed，Python 是 0-indexed。這種調整放在 **return 的那一刻**做最安全——中間過程都用 0-indexed 思考，不然很容易在迴圈裡算錯。

**用 `elif / else` 不用兩個 `if`**：三種情況互斥，寫成獨立 `if` 的話一圈之內可能同時移動兩個指標，就會跳過解。

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(1) |

---

## 五、系列總結

| 題號 | 模型 | 關鍵洞見 |
| --- | --- | --- |
| 125 | 對撞 | 內層 while 也要守邊界 |
| 344 | 對撞 | tuple 交換不用暫存 |
| 283 | 快慢 | 用交換避免覆蓋 |
| 26 | 快慢 | 排序後重複必相鄰 |
| 977 | 對撞 | 從大到小取 → 從後往前填 |
| 88 | 對撞（雙來源） | 負索引不報錯，必須手動守 |
| 167 | 對撞 | 排序讓 O(n) 空間降到 O(1) |

**一句話帶走**：two pointers 是拿**順序**當線索，換掉 hash map 的額外空間。看到「已排序」或「原地修改」這兩個字，先想它。

---

## 六、跟 Hash Map 的分工

| 情境 | 選誰 |
| --- | --- |
| 沒排序，找配對 | Hash map |
| 已排序，找配對 | Two pointers（空間更省） |
| 要出現次數 | Hash map |
| 要原地修改、O(1) 空間 | Two pointers |
| 排序成本可接受，且排序後有結構可利用 | 先 sort 再 two pointers |
