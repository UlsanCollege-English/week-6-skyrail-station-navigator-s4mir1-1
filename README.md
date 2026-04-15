[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mHMwxQwH)

# Weekly Coding #5: Skyrail Station Navigator

## Summary
This program implements binary tree traversals and binary search tree (BST) operations.  
It includes preorder, inorder, and postorder traversals to explore tree structures.  
It also supports BST search to check for a value and BST insertion to add values while maintaining proper order.  
Additional tests were added to verify correctness for more edge cases like skewed trees and deeper insertions.

---

## Approach
- **Preorder traversal:** Visit the current node first, then recursively traverse the left subtree followed by the right subtree.
- **Inorder traversal:** Recursively traverse the left subtree, visit the node, then traverse the right subtree.
- **Postorder traversal:** Recursively traverse the left and right subtrees first, then visit the node.
- **BST search:** Iteratively compare the target value with the current node and move left or right depending on the comparison.
- **BST insert:** Traverse the tree iteratively to find the correct position and insert the value, ignoring duplicates.

---

## Complexity

### `preorder_values`
- **Time:** O(n)  
- **Space:** O(n)  
- **Why:** Each node is visited once, and recursion uses stack space proportional to tree height.

### `inorder_values`
- **Time:** O(n)  
- **Space:** O(n)  
- **Why:** Every node is processed once using recursion.

### `postorder_values`
- **Time:** O(n)  
- **Space:** O(n)  
- **Why:** Traverses all nodes once with recursive calls.

### `bst_contains`
- **Time:** O(h)  
- **Space:** O(1)  
- **Why:** Only one path from root to leaf is explored (h = height of the tree).

### `bst_insert`
- **Time:** O(h)  
- **Space:** O(1)  
- **Why:** Traverses down one path without recursion to insert the node.

---

## Edge-Case Checklist
- [x] Empty tree traversal returns `[]`  
  → Functions return an empty list when the root is `None`.

- [x] Single-node traversal works correctly  
  → Traversals return a list containing only the root value.

- [x] `bst_contains` returns `False` for an empty tree  
  → The loop does not execute and returns `False`.

- [x] `bst_contains` returns `False` when the target is missing  
  → The search reaches a `None` node without finding the value.

- [x] `bst_insert` creates a root when the tree is empty  
  → A new `TreeNode` is created and returned.

- [x] `bst_insert` ignores duplicate values  
  → The function returns the original tree without inserting.

- [x] I tested at least one deeper insert case  
  → Example: inserting 55 into a deeper level.

- [x] Right-heavy (skewed) trees are handled correctly  
  → Verified with traversal tests on right-only trees.

- [x] Left-heavy (skewed) trees are handled correctly  
  → Verified with traversal tests on left-only trees.

- [x] BST works when built from scratch  
  → Inserted multiple values starting from an empty tree.

---

## Assistance & Sources
- **AI used? (Y/N):** Y  
- **What AI helped with:** Verifying traversal logic, generating additional test cases, and structuring explanations.  
- **Other sources used:** Class notes and lecture materials  

---

## Test Results
All tests (including additional ones) passed successfully:
