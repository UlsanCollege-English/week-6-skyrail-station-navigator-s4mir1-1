"""Weekly Coding #5 starter code: Trees, traversals, and BST basics."""

from __future__ import annotations
from typing import Any


class TreeNode:
    """A simple binary tree node."""

    def __init__(
        self,
        value: Any,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def preorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in preorder: node, left, right."""
    if root is None:
        return []
    return (
        [root.value]
        + preorder_values(root.left)
        + preorder_values(root.right)
    )


def inorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in inorder: left, node, right."""
    if root is None:
        return []
    return (
        inorder_values(root.left)
        + [root.value]
        + inorder_values(root.right)
    )


def postorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in postorder: left, right, node."""
    if root is None:
        return []
    return (
        postorder_values(root.left)
        + postorder_values(root.right)
        + [root.value]
    )


def bst_contains(root: TreeNode | None, target: int) -> bool:
    """Return True if target exists in the BST. Otherwise return False."""
    current = root
    while current:
        if target == current.value:
            return True
        elif target < current.value:
            current = current.left
        else:
            current = current.right
    return False


def bst_insert(root: TreeNode | None, value: int) -> TreeNode:
    """Insert value into the BST and return the root node.

    Duplicate values should be ignored.
    """
    if root is None:
        return TreeNode(value)

    current = root
    while True:
        if value == current.value:
            # Ignore duplicates
            return root
        elif value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = TreeNode(value)
                return root
            current = current.right