from typing import List, Any, Dict, Set, Generator, Optional

class StaticArray:
    def __init__(self, capacity: int):
        self.data = [0] * capacity
        self.capacity = capacity

    def set(self, index: int, value: int) -> None:
        self.data[index] = value

    def get(self, index: int) -> int:
        return self.data[index]

class DynamicArray:
    def __init__(self):
        self.data = []

    def append(self, value: int) -> None:
        self.data.append(value)

    def insert(self, index: int, value: int) -> None:
        self.data.insert(index, value)

    def delete(self, index: int) -> None:
        del self.data[index]

    def get(self, index: int) -> int:
        return self.data[index]

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    def insert(self, position: int, value: int) -> None:
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        prev = self.head
        for _ in range(position - 1):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node

    def delete(self, value: int) -> None:
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        prev = self.head
        while prev.next and prev.next.value != value:
            prev = prev.next
        if prev.next:
            prev.next = prev.next.next

    def find(self, value: int) -> Optional[Node]:
        curr = self.head
        while curr and curr.value != value:
            curr = curr.next
        return curr

    def size(self) -> int:
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def is_empty(self) -> bool:
        return self.head is None

    def reverse(self) -> None:
        prev, curr = None, self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr

class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)
        if not self.head:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        new_node.prev = tail

    def insert(self, position: int, value: int) -> None:
        new_node = DoubleNode(value)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        prev = self.head
        for _ in range(position - 1):
            prev = prev.next
        new_node.next = prev.next
        new_node.prev = prev
        if prev.next:
            prev.next.prev = new_node
        prev.next = new_node

    def delete(self, value: int) -> None:
        curr = self.head
        while curr and curr.value != value:
            curr = curr.next
        if curr:
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            if curr == self.head:
                self.head = curr.next

    def find(self, value: int) -> Optional[DoubleNode]:
        curr = self.head
        while curr and curr.value != value:
            curr = curr.next
        return curr

    def size(self) -> int:
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def is_empty(self) -> bool:
        return self.head is None

    def reverse(self) -> None:
        curr = self.head
        prev = None
        while curr:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev
        if prev:
            self.head = prev.prev

    def get_head(self) -> DoubleNode:
        return self.head

    def get_tail(self) -> DoubleNode:
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value: int) -> None:
        self.data.append(value)

    def dequeue(self) -> int:
        return self.data.pop(0)

    def peek(self) -> int:
        return self.data[0]

    def is_empty(self) -> bool:
        return len(self.data) == 0

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def delete(self, value: int) -> None:
        def _delete(node, value):
            if not node:
                return node
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp_val = self._min_value(node.right)
                node.value = temp_val
                node.right = _delete(node.right, temp_val)
            return node

        self.root = _delete(self.root, value)

    def search(self, value: int) -> Optional[TreeNode]:
        def _search(node, value):
            if not node or node.value == value:
                return node
            if value < node.value:
                return _search(node.left, value)
            return _search(node.right, value)
        return _search(self.root, value)

    def inorder_traversal(self) -> List[int]:
        result = []
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            result.append(node.value)
            _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder_traversal(self) -> List[int]:
        result = []
        def _preorder(node):
            if not node:
                return
            result.append(node.value)
            _preorder(node.left)
            _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder_traversal(self) -> List[int]:
        result = []
        def _postorder(node):
            if not node:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.value)
        _postorder(self.root)
        return result

    def level_order_traversal(self) -> List[int]:
        result = []
        if not self.root:
            return result
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def minimum(self) -> Optional[TreeNode]:
        node = self.root
        while node and node.left:
            node = node.left
        return node

    def maximum(self) -> Optional[TreeNode]:
        node = self.root
        while node and node.right:
            node = node.right
        return node

    def size(self) -> int:
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)

    def is_empty(self) -> bool:
        return self.root is None

    def height(self) -> int:
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def is_valid_bst(self) -> bool:
        def _is_valid(node, low, high):
            if not node:
                return True
            if not (low < node.value < high):
                return False
            return _is_valid(node.left, low, node.value) and _is_valid(node.right, node.value, high)
        return _is_valid(self.root, float('-inf'), float('inf'))

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def shell_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return _merge(left, right)

def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def linear_search(lst: List[int], target: int) -> int:
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1

def binary_search(lst: List[int], target: int) -> int:
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)