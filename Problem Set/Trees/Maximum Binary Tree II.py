class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node