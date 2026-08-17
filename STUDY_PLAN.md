# DSA & SQL Study Plan -- Complete 280-Day Breakdown

## Overview

**Target**: Data Engineering (primary) and Software Development roles at top product companies (Netflix, Amazon, Anthropic, OpenAI)

**Timeline**: 280 days (40 weeks / ~10 months)

**Daily Commitment**: 1.5-2 hours per day (mornings)

**Start Date**: August 10, 2026

### Resources

- **Book**: Grokking Algorithms, 2nd Edition (Chapters 1-13)
- **LeetCode**: Problems organized by topic and difficulty
- **NeetCode 150**: Curated problem set covering all major patterns
- **SQL Practice Problems** (book): Progressive SQL chapters
- **StrataScratch**: SQL practice platform (Easy, Medium, Hard tiers)

### Grokking Algorithms 2nd Edition -- Chapter Map

1. Introduction to Algorithms (Binary Search, Big O)
2. Selection Sort (Arrays vs Linked Lists)
3. Recursion
4. Quicksort (Divide & Conquer)
5. Hash Tables
6. Breadth-First Search (Graphs intro)
7. Trees
8. Binary Search Trees (BST) *(new in 2nd edition)*
9. Dijkstra's Algorithm
10. Greedy Algorithms
11. Dynamic Programming
12. K-Nearest Neighbors
13. Where to Go Next

### Phase Overview

| Phase | Weeks | Days | Focus |
|-------|-------|------|-------|
| Phase 0 | W1-W3 | D1-D21 | Python fundamentals (no DSA yet) |
| Phase 1 | W4-W12 | D22-D84 | Grokking Ch 1-5 + LeetCode + SQL foundations |
| Phase 2 | W13-W21 | D85-D147 | Grokking Ch 6-8 + LeetCode + SQL intermediate |
| Phase 3 | W22-W30 | D148-D210 | Grokking Ch 9-11 + LeetCode + SQL advanced |
| Phase 4 | W31-W36 | D211-D252 | NeetCode 150 patterns (not in book) |
| Phase 5 | W37-W40 | D253-D280 | Mock interviews + revision + weak spots |

---

## PHASE 0: PYTHON FOUNDATIONS (Weeks 1-3, Days 1-21)

**Goal**: Write functions, loops, lists, dicts, sets, recursion WITHOUT looking them up.

### Week 1: Core Python Mechanics (Days 1-7)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D1 (Mon) | 2h | Variables, data types, if/else, operators | Write 10 small programs from scratch (no lookups) |
| D2 (Tue) | 2h | `for` loops, `while` loops, `range()`, `enumerate()` | LC #1480 Running Sum, LC #1672 Richest Customer |
| D3 (Wed) | 2h | Lists: indexing, slicing, append, pop, insert, list comprehensions | LC #1929 Concatenation of Array, LC #1470 Shuffle the Array |
| D4 (Thu) | 2h | Strings: methods, slicing, f-strings, iteration | LC #344 Reverse String, LC #242 Valid Anagram |
| D5 (Fri) | 2h | Dictionaries: CRUD, iteration, `.get()`, `.items()`, defaultdict | LC #1 Two Sum (brute force), LC #383 Ransom Note |
| D6 (Sat) | 2h | Sets: operations, membership, dedup | LC #217 Contains Duplicate, LC #349 Intersection of Two Arrays |
| D7 (Sun) | 1.5h | **REVIEW**: Redo any problem you struggled with. Write a cheat sheet from memory | - |

### Week 2: Functions & Recursion (Days 8-14)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D8 (Mon) | 2h | Functions: def, return, parameters, default args, *args, **kwargs | Write 5 utility functions from scratch |
| D9 (Tue) | 2h | Nested loops, 2D lists, matrix traversal | LC #1672 Richest Customer (matrix), LC #867 Transpose Matrix |
| D10 (Wed) | 2h | Sorting: `sorted()`, `.sort()`, key functions, lambda | LC #2418 Sort the People, LC #1636 Sort Array by Increasing Frequency |
| D11 (Thu) | 2h | Recursion basics: base case, recursive case, call stack | Write: factorial, sum of list, countdown -- all recursive |
| D12 (Fri) | 2h | More recursion: string reversal, palindrome check, power function | LC #509 Fibonacci Number, LC #231 Power of Two |
| D13 (Sat) | 2h | Stacks (using list), Queues (using deque) | LC #20 Valid Parentheses, LC #225 Implement Stack using Queues |
| D14 (Sun) | 1.5h | **REVIEW**: Timed redo of W1-W2 hard problems. Update cheat sheet | - |

### Week 3: Python Patterns & Problem Solving (Days 15-21)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D15 (Mon) | 2h | Collections module: Counter, defaultdict, deque | LC #387 First Unique Character, LC #169 Majority Element |
| D16 (Tue) | 2h | Tuple, heapq basics, itertools basics | LC #703 Kth Largest Element in a Stream |
| D17 (Wed) | 2h | File I/O, error handling (try/except) | Write: read CSV, parse data, output summary |
| D18 (Thu) | 2h | Practice: solve 3 easy LeetCode without ANY reference | LC #26 Remove Duplicates, LC #88 Merge Sorted Array, LC #136 Single Number |
| D19 (Fri) | 2h | Practice: solve 3 more, focus on writing clean functions | LC #121 Best Time to Buy/Sell Stock, LC #125 Valid Palindrome, LC #283 Move Zeroes |
| D20 (Sat) | 2h | **SQL START**: SQL Practice Problems Ch 1-3 (SELECT, WHERE, ORDER BY) | StrataScratch: Easy #1-5 |
| D21 (Sun) | 1.5h | **REVIEW**: Phase 0 self-assessment. Can you write all basics from memory? | - |

### Phase 0 Checkpoint

You should be able to write functions, loops, list/dict/set operations, and basic recursion WITHOUT looking anything up. If not, extend Phase 0 by 1 week.

---

## PHASE 1: GROKKING CH 1-5 + LEETCODE (Weeks 4-12, Days 22-84)

**Goal**: Master binary search, arrays/linked lists, recursion, divide & conquer, hash tables.

### Week 4: Ch 1 -- Introduction to Algorithms / Binary Search (Days 22-28)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D22 (Mon) | 2h | Read Grokking Ch 1. Understand binary search, Big O notation | Implement binary search from scratch |
| D23 (Tue) | 2h | Big O: O(1), O(log n), O(n), O(n log n), O(n^2). Practice identifying | LC #704 Binary Search |
| D24 (Wed) | 2h | Binary search variations: first/last occurrence | LC #35 Search Insert Position, LC #278 First Bad Version |
| D25 (Thu) | 2h | More binary search practice | LC #374 Guess Number Higher or Lower, LC #69 Sqrt(x) |
| D26 (Fri) | 2h | SQL: SQL Practice Problems Ch 4-6 (JOINs basics) | StrataScratch: Easy #6-10 |
| D27 (Sat) | 2h | Binary search review + edge cases | LC #367 Valid Perfect Square, LC #441 Arranging Coins |
| D28 (Sun) | 1.5h | **REVIEW**: Redo Ch 1 exercises. Timed binary search problems | - |

### Week 5: Ch 2 -- Selection Sort / Arrays vs Linked Lists (Days 29-35)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D29 (Mon) | 2h | Read Grokking Ch 2. Arrays vs Linked Lists, memory, access patterns | Implement selection sort from scratch |
| D30 (Tue) | 2h | Array problems: traversal, in-place modification | LC #27 Remove Element, LC #26 Remove Duplicates from Sorted Array |
| D31 (Wed) | 2h | Linked List basics: Node class, traversal, insert, delete | LC #206 Reverse Linked List, LC #21 Merge Two Sorted Lists |
| D32 (Thu) | 2h | More linked list practice | LC #141 Linked List Cycle, LC #83 Remove Duplicates from Sorted List |
| D33 (Fri) | 2h | SQL: SQL Practice Problems Ch 7-9 (GROUP BY, HAVING, aggregations) | StrataScratch: Easy #11-15 |
| D34 (Sat) | 2h | Selection sort analysis + comparison with other sorts | LC #912 Sort an Array (implement selection sort) |
| D35 (Sun) | 1.5h | **REVIEW**: Array vs LL tradeoffs quiz. Redo hard problems | - |

### Week 6: Ch 3 -- Recursion (Days 36-42)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D36 (Mon) | 2h | Read Grokking Ch 3. Call stack, base case, recursive case | Trace call stack on paper for factorial(5) |
| D37 (Tue) | 2h | Recursive problems: sum array, count items, find max | LC #509 Fibonacci, LC #70 Climbing Stairs |
| D38 (Wed) | 2h | Recursion with strings and lists | LC #344 Reverse String (recursive), LC #21 Merge Two Sorted Lists (recursive) |
| D39 (Thu) | 2h | Recursion to iteration conversion practice | LC #206 Reverse Linked List (both ways) |
| D40 (Fri) | 2h | SQL: SQL Practice Problems Ch 10-12 (subqueries) | StrataScratch: Medium #1-3 |
| D41 (Sat) | 2h | Recursion deep practice | LC #234 Palindrome Linked List, LC #104 Maximum Depth of Binary Tree |
| D42 (Sun) | 1.5h | **REVIEW**: Draw call stacks from memory. Redo struggles | - |

### Week 7: Ch 4 -- Quicksort / Divide & Conquer (Days 43-49)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D43 (Mon) | 2h | Read Grokking Ch 4. D&C strategy, quicksort walkthrough | Implement quicksort from scratch |
| D44 (Tue) | 2h | D&C: sum array, count elements using D&C | LC #169 Majority Element (D&C approach) |
| D45 (Wed) | 2h | Merge sort implementation + comparison with quicksort | LC #912 Sort an Array (merge sort), LC #148 Sort List |
| D46 (Thu) | 2h | Partition logic, pivot selection, average vs worst case | LC #215 Kth Largest Element (quickselect) |
| D47 (Fri) | 2h | SQL: SQL Practice Problems Ch 13-15 (CASE, window functions intro) | StrataScratch: Medium #4-6 |
| D48 (Sat) | 2h | D&C review + mixed problems | LC #53 Maximum Subarray, LC #108 Convert Sorted Array to BST |
| D49 (Sun) | 1.5h | **REVIEW**: Implement quicksort + mergesort from memory. Time yourself | - |

### Week 8: Ch 5 -- Hash Tables (Days 50-56)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D50 (Mon) | 2h | Read Grokking Ch 5. Hash functions, collisions, load factor | Implement simple hash table from scratch |
| D51 (Tue) | 2h | Hash map patterns: frequency count, lookup | LC #1 Two Sum, LC #242 Valid Anagram, LC #49 Group Anagrams |
| D52 (Wed) | 2h | Hash set patterns: dedup, membership | LC #217 Contains Duplicate, LC #128 Longest Consecutive Sequence |
| D53 (Thu) | 2h | Advanced hash patterns | LC #560 Subarray Sum Equals K, LC #347 Top K Frequent Elements |
| D54 (Fri) | 2h | SQL: Window functions (ROW_NUMBER, RANK, DENSE_RANK) | StrataScratch: Medium #7-9 |
| D55 (Sat) | 2h | Hash table review + contest-style practice | LC #438 Find All Anagrams, LC #350 Intersection of Two Arrays II |
| D56 (Sun) | 1.5h | **REVIEW**: Phase 1 comprehensive review. List weak areas | - |

### Weeks 9-10: Phase 1 Consolidation (Days 57-70)

| Day | Focus | Practice |
|-----|-------|----------|
| D57 | Redo ALL Phase 1 problems you couldn't solve in <15 min | Timed practice |
| D58 | Redo ALL Phase 1 problems you couldn't solve in <15 min | Timed practice |
| D59 | Binary search mastery | LC #33 Search in Rotated Sorted Array |
| D60 | Binary search mastery | LC #153 Find Minimum in Rotated Sorted Array |
| D61 | Array + Hash mastery | LC #238 Product of Array Except Self |
| D62 | Array + Hash mastery | LC #271 Encode and Decode Strings (NeetCode) |
| D63 | Linked List mastery | LC #19 Remove Nth Node |
| D64 | Linked List mastery | LC #143 Reorder List |
| D65 | SQL consolidation: redo hard queries | StrataScratch: Medium #10-12 |
| D66 | SQL consolidation: redo hard queries | StrataScratch: Medium #13-15 |
| D67 | Recursion + D&C mastery | LC #50 Pow(x,n) |
| D68 | Recursion + D&C mastery | LC #912 Sort an Array |
| D69 | Mixed timed practice: 3 problems in 90 min | Random easy/medium from covered topics |
| D70 | **REVIEW**: Phase 1 self-assessment | - |

### Weeks 11-12: Phase 1 Buffer + NeetCode Arrays & Hashing (Days 71-84)

| Day | Focus | Practice |
|-----|-------|----------|
| D71 | NeetCode 150: Arrays & Hashing | NC: Contains Duplicate, Valid Anagram |
| D72 | NeetCode 150: Arrays & Hashing | NC: Two Sum, Group Anagrams |
| D73 | NeetCode 150: Arrays & Hashing | NC: Top K Frequent, Encode/Decode Strings |
| D74 | NeetCode 150: Arrays & Hashing | NC: Product of Array Except Self |
| D75 | NeetCode 150: Arrays & Hashing | NC: Valid Sudoku |
| D76 | NeetCode 150: Arrays & Hashing | NC: Longest Consecutive Sequence |
| D77 | NeetCode 150: Arrays & Hashing review | Redo any missed from D71-D76 |
| D78 | Catch-up + SQL | StrataScratch: Medium #16-17, SQL Practice Problems remaining easy chapters |
| D79 | Catch-up + SQL | StrataScratch: Medium #18 |
| D80 | Catch-up + SQL | StrataScratch: Medium #19 |
| D81 | Catch-up + SQL | StrataScratch: Medium #20 |
| D82 | Catch-up: redo any weak problems from Phase 1 | Timed practice |
| D83 | Catch-up: redo any weak problems from Phase 1 | Timed practice |
| D84 | **REVIEW**: Phase 1 final assessment | - |

---

## PHASE 2: GROKKING CH 6-8 + LEETCODE (Weeks 13-21, Days 85-147)

**Goal**: Master graphs (BFS), trees, BSTs.

### Week 13: Ch 6 -- Breadth-First Search / Graphs (Days 85-91)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D85 (Mon) | 2h | Read Grokking Ch 6. Graph concepts, adjacency list, BFS | Implement BFS from scratch |
| D86 (Tue) | 2h | BFS: shortest path in unweighted graph | LC #994 Rotting Oranges, LC #733 Flood Fill |
| D87 (Wed) | 2h | BFS: level-order traversal | LC #102 Binary Tree Level Order Traversal |
| D88 (Thu) | 2h | DFS introduction (not in Grokking yet, but essential) | LC #200 Number of Islands |
| D89 (Fri) | 2h | SQL: Complex JOINs, self-joins | StrataScratch: Medium #21-23 |
| D90 (Sat) | 2h | Graph representation + traversal practice | LC #695 Max Area of Island, LC #547 Number of Provinces |
| D91 (Sun) | 1.5h | **REVIEW**: Implement BFS + DFS from memory | - |

### Week 14: Ch 7 -- Trees (Days 92-98)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D92 (Mon) | 2h | Read Grokking Ch 7. Tree concepts, binary trees, traversals | Implement inorder, preorder, postorder |
| D93 (Tue) | 2h | Tree DFS: recursive traversals | LC #94 Inorder Traversal, LC #144 Preorder, LC #145 Postorder |
| D94 (Wed) | 2h | Tree problems: depth, height, diameter | LC #104 Max Depth, LC #543 Diameter of Binary Tree |
| D95 (Thu) | 2h | Tree problems: symmetry, paths | LC #226 Invert Binary Tree, LC #100 Same Tree, LC #572 Subtree |
| D96 (Fri) | 2h | SQL: CTEs and recursive queries | StrataScratch: Medium #24-26 |
| D97 (Sat) | 2h | Tree BFS (level order) + mixed | LC #102 Level Order, LC #199 Right Side View |
| D98 (Sun) | 1.5h | **REVIEW**: Draw tree traversals on paper from memory | - |

### Week 15: Ch 8 -- Binary Search Trees (Days 99-105)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D99 (Mon) | 2h | Read Grokking Ch 8. BST properties, search, insert, delete | Implement BST from scratch |
| D100 (Tue) | 2h | BST search and validation | LC #700 Search in BST, LC #98 Validate BST |
| D101 (Wed) | 2h | BST operations | LC #701 Insert into BST, LC #450 Delete Node in BST |
| D102 (Thu) | 2h | BST properties exploitation | LC #230 Kth Smallest in BST, LC #235 LCA of BST |
| D103 (Fri) | 2h | SQL: Advanced window functions (LAG, LEAD, running totals) | StrataScratch: Hard #1-3 |
| D104 (Sat) | 2h | BST construction + balanced trees | LC #108 Convert Sorted Array to BST, LC #110 Balanced Binary Tree |
| D105 (Sun) | 1.5h | **REVIEW**: BST operations from memory | - |

### Weeks 16-17: NeetCode 150 -- Trees Section (Days 106-119)

| Day | Focus | Practice |
|-----|-------|----------|
| D106 | NeetCode Trees (1st half) | NC: Invert Tree, Max Depth |
| D107 | NeetCode Trees (1st half) | NC: Diameter, Balanced Tree |
| D108 | NeetCode Trees (1st half) | NC: Same Tree, Subtree |
| D109 | NeetCode Trees (1st half) | NC: LCA |
| D110 | NeetCode Trees (1st half) | NC: Level Order |
| D111 | NeetCode Trees (1st half) review | Redo any missed from D106-D110 |
| D112 | NeetCode Trees (1st half) review | Timed practice on all 1st half problems |
| D113 | NeetCode Trees (2nd half) | NC: Right Side View, Count Good Nodes |
| D114 | NeetCode Trees (2nd half) | NC: Validate BST, Kth Smallest |
| D115 | NeetCode Trees (2nd half) | NC: Build Tree from Preorder/Inorder |
| D116 | NeetCode Trees (2nd half) | NC: Max Path Sum |
| D117 | NeetCode Trees (2nd half) | NC: Serialize/Deserialize |
| D118 | NeetCode Trees (2nd half) + SQL | SQL: StrataScratch Hard #1-3 review |
| D119 | **REVIEW**: All tree problems | Timed redo of hardest tree problems |

### Weeks 18-19: NeetCode 150 -- Linked List + Stack (Days 120-133)

| Day | Focus | Practice |
|-----|-------|----------|
| D120 | NeetCode Linked List | NC: Reverse LL, Merge Two |
| D121 | NeetCode Linked List | NC: Reorder List, Remove Nth |
| D122 | NeetCode Linked List | NC: Copy Random Pointer, Add Two Numbers |
| D123 | NeetCode Linked List | NC: Has Cycle, Find Duplicate |
| D124 | NeetCode Linked List | NC: LRU Cache |
| D125 | NeetCode Linked List | NC: Merge K Lists |
| D126 | NeetCode Linked List | NC: Reverse K Group |
| D127 | NeetCode Stack | NC: Valid Parentheses, Min Stack |
| D128 | NeetCode Stack | NC: Evaluate RPN, Generate Parentheses |
| D129 | NeetCode Stack | NC: Daily Temperatures, Car Fleet |
| D130 | NeetCode Stack | NC: Largest Rectangle |
| D131 | SQL day | StrataScratch: Hard #4-6 |
| D132 | Stack + Linked List review | Redo any problems that took >25 min |
| D133 | **REVIEW**: Linked List + Stack comprehensive | Timed practice |

### Weeks 20-21: Phase 2 Consolidation (Days 134-147)

| Day | Focus | Practice |
|-----|-------|----------|
| D134 | Redo Phase 2 struggles | Timed: 25 min per medium |
| D135 | Redo Phase 2 struggles | Timed: 25 min per medium |
| D136 | Redo Phase 2 struggles | Timed: 25 min per medium |
| D137 | Redo Phase 2 struggles | Timed: 25 min per medium |
| D138 | Redo Phase 2 struggles | Timed: 25 min per medium |
| D139 | Graph + Tree mixed problems | LC #236 LCA of Binary Tree |
| D140 | Graph + Tree mixed problems | LC #297 Serialize/Deserialize |
| D141 | Graph + Tree mixed problems | LC #207 Course Schedule |
| D142 | Graph + Tree mixed problems | Mixed graph/tree mediums |
| D143 | SQL consolidation | StrataScratch: Hard #7-8, SQL Practice Problems advanced chapters |
| D144 | SQL consolidation | StrataScratch: Hard #9-10 |
| D145 | SQL consolidation | SQL Practice Problems advanced chapters |
| D146 | **Phase 2 Assessment**: Solve 4 random mediums in 2 hours | Timed |
| D147 | **Phase 2 Assessment**: Review and identify gaps | - |

---

## PHASE 3: GROKKING CH 9-11 + LEETCODE (Weeks 22-30, Days 148-210)

**Goal**: Master Dijkstra's, Greedy, Dynamic Programming.

### Week 22: Ch 9 -- Dijkstra's Algorithm (Days 148-154)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D148 (Mon) | 2h | Read Grokking Ch 9. Weighted graphs, Dijkstra's, negative edges | Implement Dijkstra from scratch (min-heap) |
| D149 (Tue) | 2h | Dijkstra practice | LC #743 Network Delay Time |
| D150 (Wed) | 2h | Shortest path variations | LC #787 Cheapest Flights Within K Stops |
| D151 (Thu) | 2h | Graph algorithms review: BFS vs DFS vs Dijkstra | LC #1091 Shortest Path in Binary Matrix |
| D152 (Fri) | 2h | SQL: Complex aggregations, pivoting | StrataScratch: Hard #11-13 |
| D153 (Sat) | 2h | Weighted graph practice | LC #778 Swim in Rising Water |
| D154 (Sun) | 1.5h | **REVIEW**: Implement Dijkstra from memory | - |

### Week 23: Ch 10 -- Greedy Algorithms (Days 155-161)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D155 (Mon) | 2h | Read Grokking Ch 10. Greedy strategy, set cover problem | Identify greedy vs non-greedy problems |
| D156 (Tue) | 2h | Classic greedy: interval scheduling | LC #435 Non-Overlapping Intervals, LC #56 Merge Intervals |
| D157 (Wed) | 2h | Greedy patterns | LC #55 Jump Game, LC #45 Jump Game II |
| D158 (Thu) | 2h | More greedy | LC #134 Gas Station, LC #846 Hand of Straights |
| D159 (Fri) | 2h | SQL: String functions, date functions, complex CASE | StrataScratch: Hard #14-16 |
| D160 (Sat) | 2h | Greedy review | LC #763 Partition Labels, LC #678 Valid Parenthesis String |
| D161 (Sun) | 1.5h | **REVIEW**: When greedy works vs when it doesn't | - |

### Weeks 24-26: Ch 11 -- Dynamic Programming (Days 162-182)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D162 (Mon) | 2h | Read Grokking Ch 11. Knapsack problem, DP grid | Trace DP table on paper |
| D163 (Tue) | 2h | 1D DP: Fibonacci, climbing stairs | LC #70 Climbing Stairs, LC #746 Min Cost Climbing Stairs |
| D164 (Wed) | 2h | 1D DP: house robber pattern | LC #198 House Robber, LC #213 House Robber II |
| D165 (Thu) | 2h | 1D DP: coin change, word break | LC #322 Coin Change, LC #139 Word Break |
| D166 (Fri) | 2h | SQL: DP-style SQL problems (running totals, cumulative) | StrataScratch: Hard #17-19 |
| D167 (Sat) | 2h | 1D DP review | LC #300 Longest Increasing Subsequence |
| D168 (Sun) | 1.5h | **REVIEW** | - |
| D169 (Mon) | 2h | 2D DP: grid problems | LC #62 Unique Paths, LC #64 Minimum Path Sum |
| D170 (Tue) | 2h | 2D DP: longest common subsequence | LC #1143 LCS, LC #72 Edit Distance |
| D171 (Wed) | 2h | 2D DP: knapsack variations | LC #416 Partition Equal Subset Sum, LC #494 Target Sum |
| D172 (Thu) | 2h | String DP | LC #5 Longest Palindromic Substring, LC #647 Palindromic Substrings |
| D173 (Fri) | 2h | SQL: Advanced analytics queries | StrataScratch: Hard #20-22 |
| D174 (Sat) | 2h | DP review: top-down vs bottom-up | LC #152 Maximum Product Subarray |
| D175 (Sun) | 1.5h | **REVIEW** | - |
| D176 (Mon) | 2h | NeetCode 150 DP section | NC: Climbing Stairs, Min Cost Climbing |
| D177 (Tue) | 2h | NeetCode 150 DP section | NC: House Robber I, House Robber II |
| D178 (Wed) | 2h | NeetCode 150 DP section | NC: Palindromic Substrings, Decode Ways |
| D179 (Thu) | 2h | NeetCode 150 DP section | NC: Coin Change, Max Product Subarray |
| D180 (Fri) | 2h | NeetCode 150 DP section | NC: Word Break, LIS |
| D181 (Sat) | 2h | NeetCode 150 DP section | NC: Can Partition, LCS |
| D182 (Sun) | 1.5h | **REVIEW**: DP section 1st half | - |

### Weeks 27-28: NeetCode DP Continued + Graphs (Days 183-196)

| Day | Focus | Practice |
|-----|-------|----------|
| D183 | NeetCode DP (remaining) | NC: Target Sum, Interleaving String |
| D184 | NeetCode DP (remaining) | NC: Edit Distance, Unique Paths |
| D185 | NeetCode DP (remaining) | NC: Longest Common Subseq, Buy/Sell Stock Cooldown |
| D186 | NeetCode DP (remaining) | NC: Coin Change 2, Burst Balloons |
| D187 | NeetCode DP (remaining) | NC: Regular Expression Matching |
| D188 | NeetCode DP (remaining) | NC: Distinct Subsequences |
| D189 | NeetCode DP (remaining) | NC: Best Time Buy/Sell Stock |
| D190 | NeetCode Graphs (1st half) | NC: Number of Islands, Max Area |
| D191 | NeetCode Graphs (1st half) | NC: Clone Graph, Pacific Atlantic |
| D192 | NeetCode Graphs (1st half) | NC: Course Schedule I, Course Schedule II |
| D193 | NeetCode Graphs (1st half) | NC: Rotting Oranges, Walls & Gates |
| D194 | NeetCode Graphs (1st half) | NC: Surrounded Regions |
| D195 | SQL day | StrataScratch: Hard #23-25 |
| D196 | **REVIEW**: DP + Graphs 1st half | Timed redo |

### Weeks 29-30: Phase 3 Consolidation (Days 197-210)

| Day | Focus | Practice |
|-----|-------|----------|
| D197 | NeetCode Graphs (remaining) | NC: Graph Valid Tree, Number Connected Components |
| D198 | NeetCode Graphs (remaining) | NC: Redundant Connection, Word Ladder |
| D199 | NeetCode Graphs (remaining) | NC: Alien Dictionary, Min Cost to Connect |
| D200 | NeetCode Graphs (remaining) | NC: Network Delay, Swim in Rising Water, Foreign Dictionary |
| D201 | DP weak spots: redo every DP problem that took >30 min | Timed practice |
| D202 | DP weak spots continued | Timed practice |
| D203 | DP weak spots continued | Timed practice |
| D204 | DP weak spots continued | Timed practice |
| D205 | Greedy + Dijkstra review | Mixed problems |
| D206 | Greedy + Dijkstra review | Mixed problems |
| D207 | Greedy + Dijkstra review | Mixed problems |
| D208 | Greedy + Dijkstra review | Mixed problems |
| D209 | **Phase 3 Assessment**: 4 mediums + 1 hard in 2.5 hours | Timed |
| D210 | **Phase 3 Assessment**: Review results and identify gaps | - |

---

## PHASE 4: NEETCODE PATTERNS NOT IN BOOK (Weeks 31-36, Days 211-252)

**Goal**: Master sliding window, two pointers, backtracking, binary search on answers, heap, union-find, tries, intervals, bit manipulation.

### Week 31: Two Pointers (Days 211-217)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D211 (Mon) | 2h | Two pointer pattern: opposite ends, same direction | LC #125 Valid Palindrome, LC #167 Two Sum II |
| D212 (Tue) | 2h | Two pointers: 3Sum pattern | LC #15 3Sum, LC #11 Container With Most Water |
| D213 (Wed) | 2h | Two pointers: fast/slow | LC #283 Move Zeroes, LC #42 Trapping Rain Water |
| D214 (Thu) | 2h | NeetCode Two Pointers complete (5 problems) | NC: Valid Palindrome, Two Sum II, 3Sum, Container With Most Water, Trapping Rain Water |
| D215 (Fri) | 2h | SQL review + new patterns | StrataScratch: Hard #26-28 |
| D216 (Sat) | 2h | Two pointer review | Extra practice from NeetCode |
| D217 (Sun) | 1.5h | **REVIEW** | - |

### Week 32: Sliding Window (Days 218-224)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D218 (Mon) | 2h | Fixed-size sliding window | LC #643 Max Average Subarray, LC #1456 Max Vowels in Substring |
| D219 (Tue) | 2h | Variable-size sliding window | LC #3 Longest Substring Without Repeating, LC #424 Longest Repeating Character Replacement |
| D220 (Wed) | 2h | Sliding window with hash map | LC #567 Permutation in String, LC #438 Find All Anagrams |
| D221 (Thu) | 2h | Hard sliding window | LC #76 Minimum Window Substring |
| D222 (Fri) | 2h | SQL: LeetCode SQL Medium problems | LC SQL: #175, #176, #177, #178 |
| D223 (Sat) | 2h | NeetCode Sliding Window (6 problems) | NC: Best Time Buy/Sell, Longest Substring, Longest Repeating Replacement, Permutation in String, Min Window Substring, Sliding Window Maximum |
| D224 (Sun) | 1.5h | **REVIEW** | - |

### Week 33: Binary Search Advanced + Heap (Days 225-231)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D225 (Mon) | 2h | Binary search on answers pattern | LC #875 Koko Eating Bananas, LC #1011 Capacity to Ship Packages |
| D226 (Tue) | 2h | Binary search: matrix, rotated array | LC #74 Search a 2D Matrix, LC #33 Search in Rotated Sorted Array |
| D227 (Wed) | 2h | NeetCode Binary Search (7 problems) | NC: Search in Rotated, Find Min in Rotated, Time Based KV Store, Median of Two Sorted Arrays, Koko Bananas, Search 2D Matrix |
| D228 (Thu) | 2h | Heap: top-K pattern, stream | LC #215 Kth Largest, LC #347 Top K Frequent, LC #295 Find Median from Data Stream |
| D229 (Fri) | 2h | SQL: LeetCode SQL Hard problems | LC SQL: #185, #262, #601 |
| D230 (Sat) | 2h | NeetCode Heap (7 problems) | NC: Kth Largest Stream, Last Stone Weight, K Closest Points, Kth Largest Element, Task Scheduler, Design Twitter, Find Median |
| D231 (Sun) | 1.5h | **REVIEW** | - |

### Week 34: Backtracking (Days 232-238)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D232 (Mon) | 2h | Backtracking template: choices, constraints, goal | LC #78 Subsets, LC #77 Combinations |
| D233 (Tue) | 2h | Backtracking: permutations | LC #46 Permutations, LC #47 Permutations II |
| D234 (Wed) | 2h | Backtracking: combination sum | LC #39 Combination Sum, LC #40 Combination Sum II |
| D235 (Thu) | 2h | Backtracking: grid/word | LC #79 Word Search, LC #51 N-Queens |
| D236 (Fri) | 2h | SQL: Data Engineering specific queries (ETL patterns, data quality) | StrataScratch: Hard #29-31 |
| D237 (Sat) | 2h | NeetCode Backtracking (9 problems) | NC: Subsets, Combination Sum, Permutations, Subsets II, Combination Sum II, Word Search, Palindrome Partitioning, Letter Combinations Phone, N-Queens |
| D238 (Sun) | 1.5h | **REVIEW** | - |

### Week 35: Tries + Intervals + Bit Manipulation (Days 239-245)

| Day | Time | Content | Practice |
|-----|------|---------|----------|
| D239 (Mon) | 2h | Trie: implement, insert, search, startsWith | LC #208 Implement Trie, LC #211 Design Add Search Words |
| D240 (Tue) | 2h | Intervals: merge, insert, meeting rooms | LC #56 Merge Intervals, LC #57 Insert Interval, LC #252 Meeting Rooms (NeetCode) |
| D241 (Wed) | 2h | NeetCode Intervals (6 problems) | NC: Insert Interval, Merge Intervals, Non-Overlapping Intervals, Meeting Rooms, Meeting Rooms II, Min Interval to Include Query |
| D242 (Thu) | 2h | Bit manipulation basics | LC #191 Number of 1 Bits, LC #338 Counting Bits, LC #190 Reverse Bits |
| D243 (Fri) | 2h | SQL: Mock interview -- 4 SQL problems in 1 hour | StrataScratch timed practice |
| D244 (Sat) | 2h | Union-Find: implement, connected components | LC #323 Number of Connected Components (NeetCode), LC #684 Redundant Connection |
| D245 (Sun) | 1.5h | **REVIEW** | - |

### Week 36: Phase 4 Consolidation (Days 246-252)

| Day | Focus | Practice |
|-----|-------|----------|
| D246 | Redo every problem from Phase 4 that took >25 min | Timed |
| D247 | Redo every problem from Phase 4 that took >25 min | Timed |
| D248 | Redo every problem from Phase 4 that took >25 min | Timed |
| D249 | Mixed NeetCode problems across all patterns | Random 3 mediums |
| D250 | Mixed NeetCode problems across all patterns | Random 3 mediums |
| D251 | SQL final consolidation | StrataScratch: 5 hard problems timed |
| D252 | **Phase 4 Assessment**: 5 mediums + 1 hard in 3 hours | Timed |

---

## PHASE 5: MOCK INTERVIEWS + REVISION (Weeks 37-40, Days 253-280)

**Goal**: Interview-ready. Consistent medium solves in 20-25 min.

### Weeks 37-38: Pattern Recognition Drilling (Days 253-266)

| Day | Focus | Practice |
|-----|-------|----------|
| D253 | Random LeetCode mediums (no topic filter): 2-3 problems | Identify pattern BEFORE coding |
| D254 | Random LeetCode mediums (no topic filter): 2-3 problems | Identify pattern BEFORE coding |
| D255 | Random LeetCode mediums (no topic filter): 2-3 problems | Identify pattern BEFORE coding |
| D256 | Random LeetCode mediums (no topic filter): 2-3 problems | Identify pattern BEFORE coding |
| D257 | Weak topic deep dive (your worst 3 topics) | 3 problems from weak area #1 |
| D258 | Weak topic deep dive (your worst 3 topics) | 3 problems from weak area #1 |
| D259 | Weak topic deep dive (your worst 3 topics) | 3 problems from weak area #2 |
| D260 | Weak topic deep dive (your worst 3 topics) | 3 problems from weak area #3 |
| D261 | Data Engineering specific: system design basics, SQL optimization | StrataScratch remaining hards |
| D262 | Data Engineering specific: system design basics, SQL optimization | LC SQL hards |
| D263 | Data Engineering specific: system design basics, SQL optimization | StrataScratch remaining hards |
| D264 | Data Engineering specific: system design basics, SQL optimization | LC SQL hards |
| D265 | **Mock Interview 1**: 2 DSA + 1 SQL in 1.5 hours | Simulate real interview |
| D266 | **Mock Interview 1**: Review and analyze mistakes | - |

### Weeks 39-40: Final Preparation (Days 267-280)

| Day | Focus | Practice |
|-----|-------|----------|
| D267 | Company-tagged problems (Amazon, Netflix on LC) | 2 problems from company tags |
| D268 | Company-tagged problems (Amazon, Netflix on LC) | 2 problems from company tags |
| D269 | Company-tagged problems (Amazon, Netflix on LC) | 2 problems from company tags |
| D270 | Company-tagged problems (Amazon, Netflix on LC) | 2 problems from company tags |
| D271 | Mock interview (self-timed or with peer) | 1 full mock |
| D272 | Mock interview (self-timed or with peer) | 1 full mock |
| D273 | Mock interview (self-timed or with peer) | 1 full mock |
| D274 | Mock interview (self-timed or with peer) | 1 full mock |
| D275 | Final weak spot patching | Redo failed mocks |
| D276 | Final weak spot patching | Redo failed mocks |
| D277 | Final weak spot patching | Redo failed mocks |
| D278 | Final weak spot patching | Redo failed mocks |
| D279 | Complete NeetCode 150 checklist -- fill any gaps | - |
| D280 | **FINAL ASSESSMENT**: 3 mediums (25 min each) + 1 hard (45 min) + 2 SQL (15 min each) | Timed |

---

## Weekly Schedule Template

```
Mon:  2h   -- New concept (read book chapter / learn pattern)
Tue:  2h   -- Practice problems on concept (2-3 LeetCode)
Wed:  2h   -- Practice problems continued (2-3 LeetCode)
Thu:  2h   -- Practice problems + harder variations
Fri:  2h   -- SQL day (SQL Practice Problems book / StrataScratch / LC SQL)
Sat:  2h   -- Review + NeetCode pattern problems
Sun:  1.5h -- MANDATORY REVIEW: redo struggles, update tracker, plan next week
```

**Total weekly hours**: ~13.5 hours

---

## Accountability System

1. **Daily**: Log every problem in tracker (problem #, time taken, solved?, approach used)
2. **Sunday Review**: Redo any problem that took >25 min or wasn't solved
3. **Phase Checkpoint**: Timed assessment at end of each phase -- must pass before moving on
4. **Pass criteria**: Solve 70% of phase problems without hints in target time

---

## Phase Checkpoints Summary

| Phase | Day | Assessment |
|-------|-----|------------|
| Phase 0 | D21 | Can you write functions, loops, list/dict/set ops, recursion from memory? |
| Phase 1 | D70, D84 | Timed problems across binary search, arrays, linked lists, hash tables |
| Phase 2 | D146-147 | Solve 4 random mediums (graphs, trees, BSTs) in 2 hours |
| Phase 3 | D209-210 | 4 mediums + 1 hard (Dijkstra, greedy, DP) in 2.5 hours |
| Phase 4 | D252 | 5 mediums + 1 hard (all patterns) in 3 hours |
| Phase 5 | D280 | 3 mediums (25 min each) + 1 hard (45 min) + 2 SQL (15 min each) |

---

## Project Structure

```
D:/10_DSA/
  tracker/progress.csv    -- daily problem log
  dsa/<topic>/<problem>.py -- solutions organized by topic
  sql/<topic>/<problem>.sql -- SQL solutions
  notes/<topic>.md         -- personal notes per topic
```
