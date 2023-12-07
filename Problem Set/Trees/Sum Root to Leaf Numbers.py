# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Create list of Paths
        final = []
        def trav(root,path):
            if not root:
                return None

            if not root.left and not root.right:
                final.append(path)
            
            if root.left:
                trav(root.left, path + [root.left.val])
            
            if root.right:
                trav(root.right, path +  [root.right.val])

        # You get the Path as list in final
        trav(root,[root.val])
        #print(final)

        # to get the total path sum Simple math 
        total = 0
        for path in final:
            s = 0
            # take 1 Path and make it the number like 1->2->3 into 123
            for i in path:
                s = (s*10) + i
            # Add the path number to total
            total += s
        
        return total
    


