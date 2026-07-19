# Day 01: Big-O and Array Fundamentals

## 🎯 Learning Objectives

- Understand Big-O notation (O(1), O(log n), O(n), O(n log n), O(n²))
- Learn array indexing and traversal
- Distinguish between time and space complexity
- Analyze time/space complexity of array operations

---

## 📚 Concept: Big-O Complexity Analysis

### Big-O Notation Breakdown

| Notation | Name | Example | Growth |
|----------|------|---------|--------|
| **O(1)** | Constant | Dictionary lookup, array index access | Flat |
| **O(log n)** | Logarithmic | Binary search | Very slow growth |
| **O(n)** | Linear | Simple loop through array | Linear growth |
| **O(n log n)** | Linearithmic | Merge sort, Quick sort | Moderate growth |
| **O(n²)** | Quadratic | Nested loops | Rapid growth |
| **O(2ⁿ)** | Exponential | Recursive backtracking | Extremely fast growth |
| **O(n!)** | Factorial | Permutations | Fastest growth |

### Complexity Comparison
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

### Array Operations Complexity

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access by index | O(1) | - | Direct memory access |
| Insert/Delete at start | O(n) | O(1) | Shifts all elements |
| Insert/Delete at end | O(1) amortized | O(1) | No shift needed |
| Insert/Delete at middle | O(n) | O(1) | Shifts remaining elements |
| Search (unsorted) | O(n) | - | Linear scan |
| Search (sorted) | O(log n) | - | Binary search possible |

---

## 💡 Core Pattern: Linear Traversal

### Basic Template

```python
def process_array(nums):
    """
    Process each element in an array
    Time: O(n)
    Space: O(1)
    """
    for value in nums:
        # Process each element
        print(value)
    
    return result
```

### Pattern Recognition Clue
You need to inspect **every element once** → Think **O(n) linear scan**

---

## 🧠 Key Insights

1. **Time vs Space Trade-off:** Sometimes you can reduce time complexity by using extra space
2. **Array Indexing is Fast:** O(1) access makes arrays great for random access
3. **Modifications are Expensive:** Inserting/deleting in the middle requires shifting elements
4. **Different patterns, different complexities:** Two solutions can have vastly different complexities

---

## 📋 Practice Problems

### Problem 1: Running Sum of 1D Array
**Difficulty:** Easy

**Problem Statement:**
Given an array `nums`, return an array `runningSum` where `runningSum[i]` is the sum of all elements `nums[0]... nums[i]`.

**Example:**
```
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: 
  runningSum[0] = 1
  runningSum[1] = 1 + 2 = 3
  runningSum[2] = 1 + 2 + 3 = 6
  runningSum[3] = 1 + 2 + 3 + 4 = 10
```

**Constraints:**
- 1 ≤ nums.length ≤ 1000
- -10⁶ ≤ nums[i] ≤ 10⁶

**Solution Location:** [solutions/1_running_sum.py](solutions/1_running_sum.py)

---

### Problem 2: Best Time to Buy and Sell Stock
**Difficulty:** Easy

**Problem Statement:**
You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day. You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

**Example:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
```

**Constraints:**
- 1 ≤ prices.length ≤ 10⁵
- 0 ≤ prices[i] ≤ 10⁴

**Solution Location:** [solutions/2_best_time_to_buy_sell.py](solutions/2_best_time_to_buy_sell.py)

---

## ✅ Daily Checklist

- [ ] Understand Big-O basics and all 7 complexity classes
- [ ] Know array operation complexities by heart
- [ ] Solve Problem 1 (Running Sum)
- [ ] Solve Problem 2 (Best Time to Buy and Sell Stock)
- [ ] Explain the time/space complexity of each solution
- [ ] Write the pattern template from memory

---

## 🔍 Review Questions

1. What is the time complexity of accessing an element at index 5 in an array of size 1000? Why?
2. Why is inserting an element at the beginning of an array O(n)?
3. What is the trade-off between time and space in sorting algorithms?
4. Which is faster: O(n²) algorithm on 1000 elements or O(n log n) on 10,000 elements?

---

## 📝 Key Takeaways

- **Big-O describes worst-case growth:** How the algorithm scales as input grows
- **Array operations vary:** O(1) access but O(n) insertion in the middle
- **Space matters:** Sometimes O(n) space is worth O(log n) or O(1) time improvement
- **Linear scan:** When you need to look at every element, you're at least O(n)

---

## 🎬 Next Steps

Once you complete this day:
1. Run both solutions locally
2. Test edge cases (empty arrays, single element, etc.)
3. Verify your complexity analysis matches actual performance
4. Move to [Day 02: Hash Sets](../Day-02/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Write pattern: 10 min
- Solve problems: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*
