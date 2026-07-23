# Hash Map 系列筆記

> LeetCode 刷題筆記 · Python
> 題目：1, 217, 242, 121, 383, 387, 205, 349

---

## 一、什麼時候該想到 Hash Map

**核心直覺：便利商店的條碼機。**

掃一下就知道價格，不用把整間店的商品從頭翻到尾。這就是 hash map 買到的超能力——**O(1) 查詢**。

但這台機器有代價：

| 買到什麼 | 付出什麼 |
| --- | --- |
| O(1) 查「在不在」「有幾個」 | 額外 O(n) 空間 |
| 不用巢狀迴圈掃描 | **順序資訊消失**（條碼機不知道商品排在架上第幾格） |

### 判斷訊號

看到這些字眼，先想 hash map：

- 重複 / duplicate
- 出現次數 / 頻率 / count
- 「有沒有出現過」
- 配對 / 對應關係 / mapping
- anagram、交集、統計

### 反向判斷（什麼時候**不要**用）

- 陣列已排序，而且要找「一組和/差」→ 用 two pointers，空間可以降到 O(1)
- 需要「最近放進去的先處理」→ 用 stack
- 只需要維護一個滾動的最小值/最大值 → 單次掃描就好（見下面的 121）

---

## 二、`dict` 還是 `set`？

這是這個系列最常犯的選擇題。判準只有一句話：

> **只在乎「在不在」用 `set`，需要「幾次」或「對應到什麼」用 `dict`。**

生活比喻：

- `set` ＝ 入場名單，門口的人只看你名字在不在上面
- `dict` ＝ 點名簿，除了名字還要記你缺席幾次

```python
# 只問存不存在
seen = set()
seen.add(5)
if 5 in seen: ...

# 要記數量
count = {}
count[ch] = count.get(ch, 0) + 1
```

`.get(key, 0)` 是這個系列最常用的 Python 慣用法：key 不存在時回傳預設值 0，不用先寫 `if key not in dict`。

---

## 三、常見陷阱（自己踩過的）

1. **搞混「元素值」和「索引位置」**
   `for i in nums` 拿到的是**值**不是**索引**。要同時要兩個請用 `enumerate()`。

   ```python
   for i, num in enumerate(nums):   # i = 索引, num = 值
   ```

2. **邊迭代邊修改 list**
   刪掉一個元素會讓後面全部往前位移，指標就對不上了 → 產生跳過元素的 bug。要改就另開一個 list，或改用雙指標原地覆寫。

3. **單向 map 抓不到「多對一」違規**（見 205）
   只記 `s → t` 的話，`s="ab"`、`t="aa"` 會被誤判成合法。必須雙向都記。

4. **Big O 化簡搞錯：連續要「相加」，巢狀才「相乘」**
   - 兩個各跑一次的 for 迴圈 → O(n) + O(n) = O(2n) = **O(n)**
   - for 裡面包 for → O(n) × O(n) = **O(n²)**
   係數常數要丟掉，`O(2n)` 就是 `O(n)`。

---

## 四、題目

### 1. Two Sum

找出兩個數字加起來等於 target，回傳它們的索引。

**思路**：暴力法是雙迴圈 O(n²)。優化的關鍵是換個問法——與其問「有沒有另一個數配得上我」，不如問「**我需要的那個數，之前出現過嗎？**」。邊走邊把看過的數字丟進 hash map，順便記下它的索引。

```python
def twoSum(nums, target):
    seen = {}                      # 值 -> 索引
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i              # 查完才放，避免自己配自己
    return []
```

**注意順序**：先查再放。反過來的話 `target = 6, nums = [3, ...]` 會讓 3 配到自己。

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(n) |

---

### 217. Contains Duplicate

判斷陣列有沒有重複元素。

**思路**：只在乎「看過沒」，不在乎次數 → `set`。

```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

一行寫法（但提早結束的優勢會消失）：

```python
return len(set(nums)) != len(nums)
```

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(n) |

---

### 242. Valid Anagram

判斷 t 是不是 s 的字母重排。

**思路**：兩個字串如果是 anagram，**每個字元的出現次數必須完全一樣**。先數 s，再拿 t 去扣；扣到負數就代表 t 多了某個字元。

```python
def isAnagram(s, t):
    if len(s) != len(t):           # 長度不同直接淘汰，省一趟掃描
        return False

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if count.get(ch, 0) == 0:  # t 有 s 沒有的字元，或已經扣完了
            return False
        count[ch] -= 1

    return True
```

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(k)，k = 不同字元數（小寫英文則為 26，可視為 O(1)） |

---

### 121. Best Time to Buy and Sell Stock

只能買一次賣一次，求最大獲利。

> ⚠️ **這題其實不是 hash map**。放在這個系列是因為它同樣示範了「用一次掃描取代雙層迴圈」的思維，但它不需要任何額外的表。

**思路**：暴力法是對每個賣出點回頭找最低買入點 → O(n²)。關鍵洞見是：**走到今天為止的歷史最低價，我一路上就記得住**，不用回頭找。

生活比喻：你邊走邊記「目前為止看過最便宜的價格」，每到一個新價格就算一次「如果今天賣掉能賺多少」。

```python
def maxProfit(prices):
    min_price = float('inf')
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > best:
            best = price - min_price
    return best
```

**用 `elif` 不用 `if`**：今天如果刷新了最低價，那今天賣出獲利必定是 0，不可能同時是最佳解，直接跳過。

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(1) |

---

### 383. Ransom Note

判斷 magazine 的字元能不能拼出 ransomNote。

**思路**：跟 242 幾乎一樣，差別是這裡**不要求數量完全相等**，只要求 magazine 的庫存夠用。

生活比喻：magazine 是倉庫存貨，ransomNote 是訂單。逐項出貨，缺貨就失敗。

```python
def canConstruct(ransomNote, magazine):
    stock = {}
    for ch in magazine:
        stock[ch] = stock.get(ch, 0) + 1

    for ch in ransomNote:
        if stock.get(ch, 0) == 0:
            return False
        stock[ch] -= 1

    return True
```

**方向不能反**：一定是「數 magazine，扣 ransomNote」。反過來就變成要求數量相等了。

| | 複雜度 |
| --- | --- |
| 時間 | O(m + n)（兩段是**連續**不是巢狀，所以相加） |
| 空間 | O(k) |

---

### 387. First Unique Character in a String

找出第一個只出現一次的字元的索引。

**思路**：這題最重要的體會是——**「只出現一次」必須看完整個字串才能確定，但「第一個」必須照原順序找**。這兩件事無法在同一趟迴圈完成，所以要掃兩趟。

- 第一趟：統計每個字元出現幾次
- 第二趟：**照原字串順序**走，第一個次數為 1 的就是答案

```python
def firstUniqChar(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i

    return -1
```

**為什麼第二趟要走 `s` 而不是走 `count`？**
因為 hash map 不保證你要的順序，而題目問的是「第一個」——順序資訊只存在於原字串裡。這正是前面說的「hash map 會弄丟順序」的實例。

| | 複雜度 |
| --- | --- |
| 時間 | O(n) + O(n) = O(n) |
| 空間 | O(k) |

---

### 205. Isomorphic Strings

判斷兩字串是否同構（字元可以一對一互相替換）。

**思路**：直覺上記一個 `s → t` 的對應表就好，但那會漏掉「多對一」的情況。

反例：`s = "ab"`, `t = "aa"`
- 單向表：`a→a`, `b→a`，完全沒衝突，回傳 True ❌
- 但 t 的 `a` 同時被 s 的 `a` 和 `b` 佔用了，這不是一對一

**所以必須雙向都檢查**。

生活比喻：座位表。不只要確保「每個人只坐一個位子」，也要確保「每個位子只有一個人坐」。

```python
def isIsomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for a, b in zip(s, t):
        if a in s_to_t and s_to_t[a] != b:
            return False
        if b in t_to_s and t_to_s[b] != a:
            return False
        s_to_t[a] = b
        t_to_s[b] = a

    return True
```

> **`zip()` 的隱形陷阱**：長度不同時它會**安靜地**截斷到較短的那個，不報錯。這題保證等長所以安全，但別的題目要先自己檢查長度。

| | 複雜度 |
| --- | --- |
| 時間 | O(n) |
| 空間 | O(k) |

---

### 349. Intersection of Two Arrays

回傳兩陣列的交集（結果不含重複）。

**思路**：兩層迴圈比對是 O(m×n)。把其中一個轉成 `set`，查詢就降到 O(1)。輸出也用 `set` 來自動去重。

```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()
    for num in nums2:
        if num in set1:
            result.add(num)
    return list(result)
```

Python 內建寫法：

```python
return list(set(nums1) & set(nums2))
```

**這題全程用 `set` 不用 `dict`**，因為完全不在乎出現幾次——這就是前面 `set` vs `dict` 判準的直接應用。

| | 複雜度 |
| --- | --- |
| 時間 | O(m + n) |
| 空間 | O(m + n) |

---

## 五、系列總結

| 題號 | 用的結構 | 為什麼 |
| --- | --- | --- |
| 1 | `dict` | 要記索引 |
| 217 | `set` | 只問在不在 |
| 242 | `dict` | 要比次數 |
| 121 | 無 | 只需一個滾動最小值 |
| 383 | `dict` | 要扣庫存數量 |
| 387 | `dict` | 要次數，且第二趟靠原順序 |
| 205 | 雙向 `dict` | 要抓多對一違規 |
| 349 | `set` | 只問在不在 |

**一句話帶走**：hash map 是用**空間**換**查詢速度**，代價是丟掉順序。當題目同時需要順序時，記得原始資料結構還在，回頭去走它。
