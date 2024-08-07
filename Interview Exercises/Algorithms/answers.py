# 1. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 2. Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 3. Quick Sort
def quick_sort(arr):
    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    _quick_sort(arr, 0, len(arr) - 1)

# 4. Find the Maximum Subarray Sum (Kadane's Algorithm)
def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# 5. Find the Kth Largest Element in an Array
def kth_largest_element(arr, k):
    from heapq import heapify, heappop
    heapify(arr)
    return heappop(arr)

# 6. Fibonacci Sequence (Iterative)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 7. Reverse a Linked List
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# 8. Detect a Cycle in a Linked List
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 9. Implement Depth-First Search (DFS) in a Graph
def dfs(graph, start):
    visited = set()
    def _dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                _dfs(neighbor)
    _dfs(start)
    return visited

# 10. Implement Breadth-First Search (BFS) in a Graph
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return visited

# 11. Dijkstra's Shortest Path Algorithm
def dijkstra(graph, start):
    import heapq
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# 12. Bellman-Ford Algorithm
def bellman_ford(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")
    return distances

# 13. Floyd-Warshall Algorithm
def floyd_warshall(graph):
    vertices = list(graph.keys())
    dist = {vertex: {v: float('infinity') for v in vertices} for vertex in vertices}
    for u in vertices:
        dist[u][u] = 0
    for u in graph:
        for v, weight in graph[u]:
            dist[u][v] = weight
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# 14. Check if a String is a Permutation of Another String
def is_permutation(str1, str2):
    from collections import Counter
    return Counter(str1) == Counter(str2)

# 15. Find the Longest Common Subsequence
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# 16. Longest Increasing Subsequence
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# 17. Knapsack Problem (0/1 Knapsack)
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

# 18. Coin Change Problem
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# 19. Find the Majority Element (Boyer-Moore Voting Algorithm)
def majority_element(arr):
    count, candidate = 0, None
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

# 20. Find the Missing Number in an Array
def find_missing_number(arr):
    n = len(arr) + 1
    return n * (n - 1) // 2 - sum(arr)

# 21. Rotate an Array
def rotate_array(arr, k):
    k %= len(arr)
    arr[:] = arr[-k:] + arr[:-k]

# 22. Find the Intersection of Two Arrays
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

# 23. Find the Union of Two Arrays
def union(arr1, arr2):
    return list(set(arr1) | set(arr2))

# 24. Validate a Binary Search Tree
def is_valid_bst(root):
    def _is_bst(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return _is_bst(node.left, low, node.val) and _is_bst(node.right, node.val, high)
    return _is_bst(root)

# 25. Find the Lowest Common Ancestor in a Binary Tree
def lowest_common_ancestor(root, p, q):
    if not root or root in (p, q):
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right

# 26. Serialize and Deserialize a Binary Tree
def serialize(root):
    def _serialize(node):
        if not node:
            return ['#']
        return [str(node.val)] + _serialize(node.left) + _serialize(node.right)
    return ' '.join(_serialize(root))

def deserialize(data):
    def _deserialize():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = _deserialize()
        node.right = _deserialize()
        return node
    vals = iter(data.split())
    return _deserialize()

# 27. Implement a Trie (Prefix Tree)
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '$' in node
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

# 28. Top K Frequent Elements
def top_k_frequent(nums, k):
    from collections import Counter
    return [item for item, count in Counter(nums).most_common(k)]

# 29. Merge Intervals
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# 30. Search in Rotated Sorted Array
def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# 31. Implement a Priority Queue
class PriorityQueue:
    def __init__(self):
        import heapq
        self.heap = []
    def push(self, item, priority):
        import heapq
        heapq.heappush(self.heap, (priority, item))
    def pop(self):
        import heapq
        return heapq.heappop(self.heap)[1]

# 32. Calculate the Power of a Number
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    return half * half * (x if n % 2 else 1)

# 33. Find the Longest Palindromic Substring
def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    return longest

# 34. Minimum Window Substring
def min_window_substring(s, t):
    from collections import Counter
    t_count = Counter(t)
    s_count = Counter()
    l, r = 0, 0
    min_len = float('inf')
    min_window = ""
    required = len(t_count)
    formed = 0
    while r < len(s):
        s_count[s[r]] += 1
        if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
            formed += 1
        while l <= r and formed == required:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_window = s[l:r + 1]
            s_count[s[l]] -= 1
            if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                formed -= 1
            l += 1
        r += 1
    return min_window

# 35. Decode a String
def decode_string(s):
    stack = []
    current_num = 0
    current_str = ""
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str, current_num = "", 0
        elif char == ']':
            last_str, num = stack.pop()
            current_str = last_str + num * current_str
        else:
            current_str += char
    return current_str

# 36. Find the Duplicate Number in an Array
def find_duplicate(arr):
    slow = fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

# 37. Find the Intersection of Multiple Arrays
def intersection_multiple(arrays):
    from collections import Counter
    counts = Counter(x for array in arrays for x in array)
    return [x for x, count in counts.items() if count == len(arrays)]

# 38. Check if a Number is a Happy Number
def is_happy(n):
    def get_next(n):
        return sum(int(i) ** 2 for i in str(n))
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

# 39. Find the First Missing Positive Integer
def first_missing_positive(nums):
    nums = set(nums)
    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i

# 40. Calculate the Median of a Stream of Numbers
class MedianFinder:
    def __init__(self):
        from heapq import heappush, heappop
        self.max_heap = []  # Lower half
        self.min_heap = []  # Upper half
    def add_num(self, num):
        import heapq
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# 41. Implement an LRU Cache
class LRUCache:
    def __init__(self, capacity):
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# 42. Count Inversions in an Array
def count_inversions(arr):
    def merge_count_split_inv(arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
        return inv_count
    def merge_sort_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge_count_split_inv(arr, temp_arr, left, mid, right)
        return inv_count
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

# 43. Implement a Set Using Linked List
class Set:
    def __init__(self):
        self.data = []
    def add(self, value):
        if value not in self.data:
            self.data.append(value)
    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
    def contains(self, value):
        return value in self.data

# 44. Implement an AVL Tree
class AVLTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        def _insert(node, key):
            if not node:
                return TreeNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            balance = self.get_balance(node)
            if balance > 1 and key < node.left.key:
                return self.right_rotate(node)
            if balance < -1 and key > node.right.key:
                return self.left_rotate(node)
            if balance > 1 and key > node.left.key:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
            if balance < -1 and key < node.right.key:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            return node
        self.root = _insert(self.root, key)
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

# 45. Convert a Binary Tree to a Doubly Linked List
def btree_to_dll(root):
    def inorder_traversal(node):
        if not node:
            return []
        return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
    nodes = inorder_traversal(root)
    for i in range(len(nodes)):
        if i > 0:
            nodes[i].left = nodes[i - 1]
            nodes[i - 1].right = nodes[i]
        else:
            head = nodes[i]
    head.left = None
    nodes[-1].right = None
    return head
