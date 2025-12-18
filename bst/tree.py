from typing import Optional, Tuple


class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self):
        return f"TreeNode({self.key!r}, {self.value!r})"


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, key, value=None) -> None:
        if self.root is None:
            self.root = TreeNode(key, value)
            return

        node = self.root
        while True:
            if key == node.key:
                node.value = value
                return
            elif key < node.key:
                if node.left is None:
                    node.left = TreeNode(key, value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(key, value)
                    return
                node = node.right

    def search(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete(self, key) -> bool:
        self.root, deleted = self._delete_rec(self.root, key)
        return deleted

    def _delete_rec(self, node: Optional[TreeNode], key) -> Tuple[Optional[TreeNode], bool]:
        if node is None:
            return None, False

        if key < node.key:
            node.left, deleted = self._delete_rec(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete_rec(node.right, key)
            return node, deleted
        else:
            
            if node.left is None and node.right is None:
                return None, True
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True

            successor = self._min_node(node.right)
            node.key, node.value = successor.key, successor.value
            node.right, _ = self._delete_rec(node.right, successor.key)
            return node, True

    def _min_node(self, node: TreeNode) -> TreeNode:
        while node.left is not None:
            node = node.left
        return node

    def height(self) -> int:
        return self._height_rec(self.root)

    def _height_rec(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height_rec(node.left), self._height_rec(node.right))

    def is_balanced(self) -> bool:
        _, balanced = self._check_balanced(self.root)
        return balanced

    def _check_balanced(self, node: Optional[TreeNode]) -> Tuple[int, bool]:
        if node is None:
            return 0, True
        lh, lb = self._check_balanced(node.left)
        rh, rb = self._check_balanced(node.right)
        return 1 + max(lh, rh), lb and rb and abs(lh - rh) <= 1

    
    def inorder_items(self):
        yield from self._inorder(self.root)

    def _inorder(self, node: Optional[TreeNode]):
        if node is None:
            return
        yield from self._inorder(node.left)
        yield (node.key, node.value)
        yield from self._inorder(node.right)
