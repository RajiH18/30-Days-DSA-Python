# Day 03 — Prefix Sum

## 📅 Day 3 of 30

**Language:** Python  
**Topic:** Prefix Sum  
**Practice Platform:** LeetCode

---

## 📚 What I Learned

- Prefix Sum
- Running total
- Creating a prefix sum array
- Using prefix sums to calculate range information
- Left sum and right sum
- Handling cases where an answer does not exist

---

## 💻 Practice 1 — Prefix Sum

```python
arr = [3, 5, 2, 8, 4]

prefix = []
total = 0

for i in arr:
    total = total + i
    prefix.append(total)

print(prefix)

Output:
[3, 8, 10, 18, 22]

Complexity
- Time: O(n)
- Space: O(n)
🟢 LeetCode #724 — Find Pivot Index
Approach Used
I calculated the total sum of the array and maintained a running left sum.
For every index:
Right = Total - Left - Current Element

Then I checked whether:
Left == Right

If they are equal, that index is the pivot index.
class Solution:    def pivotIndex(self, nums):        total = sum(nums)        left = 0        for i in range(len(nums)):            right = total - left - nums[i]            if left == right:                return i            left = left + nums[i]        return -1


Example
Input:
[1, 7, 3, 6, 5, 6]

Output:
3

At index 3:
Left = 1 + 7 + 3 = 11
Right = 5 + 6 = 11

Therefore, index 3 is the pivot index.
If No Pivot Exists
For:
[1, 2, 3]

there is no pivot index, so the function returns:
-1

Complexity
- Time: O(n)
- Space: O(1)
🧠 Day 3 Learning Summary
- [x] Prefix Sum
- [x] Running total
- [x] Prefix sum array
- [x] Left and right sums
- [x] LeetCode #724 — Find Pivot Index
- [x] Handled no-answer case with -1