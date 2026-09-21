# Day 01 — Time & Space Complexity + Arrays

## 📅 Day 1 of 30

**Language:** Python  
**DSA Challenge:** 30 Days  
**Practice Platform:** LeetCode

---

## 📚 Topics Learned

### 1. Time Complexity

Time complexity describes how the running time of an algorithm grows with the input size.

Common complexities:

- O(1) — Constant
- O(log n) — Logarithmic
- O(n) — Linear
- O(n log n) — Linearithmic
- O(n²) — Quadratic

---

### 2. Space Complexity

Space complexity describes the extra memory used by an algorithm.

---

### 3. Python Lists / Arrays

Learned basic operations:

```python
arr = [10, 20, 30, 40, 50]

print(arr[0])

arr.append(60)

arr.pop()


💻 Practice Problem 1 — Find Largest Element
Problem

Find the largest element in an array.

Code
arr = [4, 2, 9, 1, 7]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print(largest)
Output
9
Complexity
Time: O(n)
Space: O(1)
🟢 LeetCode #1 — Two Sum
Problem

Given an array of integers and a target value, return the indices of two numbers whose sum equals the target.

Example
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Because:

2 + 7 = 9
💡 Approach I Used
Brute Force Approach

I used two nested loops.

The first loop selects one element and the second loop checks the remaining elements.

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
Why I Used This Approach

This was the approach based on the concepts I learned today.

I compared every possible pair until I found the required sum.

Complexity
Time: O(n²)
Space: O(1)
LeetCode Result

✅ Accepted

🚀 Optimized Approach — To Learn Later

There is an optimized approach using Hashing / Dictionary.

Expected complexity:

Time: O(n)
Space: O(n)
Important

I have not learned Hashing yet, so I am intentionally not implementing the optimized solution today.

Hashing will be studied later in this 30-day DSA roadmap.

After learning Hashing, I will revisit Two Sum and understand how the optimized approach works.

🧠 Day 1 Learning

Today I learned:

Time Complexity
Space Complexity
Big-O notation
Python Lists / Arrays
Array traversal
Finding the largest element
Brute Force approach
Nested loops

LeetCode #1 — Two Sum
📊 Day 1 Progress
 Time Complexity
 Space Complexity
 Arrays / Lists
 Find Largest Element
 LeetCode #1 — Two Sum
 Accepted Submission
 Hashing — Learn later
 Optimized Two Sum — Revisit later