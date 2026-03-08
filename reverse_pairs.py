class TreeNode:
    def __init__(self, start, end, val = 0, left= None, right = None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, l, r):
        if l == r: return TreeNode(l, r, 0)
        left_tree = self.build(l, (l+r)//2)
        right_tree = self.build((l+r)//2 + 1, r)
        return TreeNode(l, r, 0, left_tree, right_tree)

    def update(self, root, index, value):
        if root.start == root.end == index:
            root.val += value
            return root.val
        if root.start > index or root.end < index:
            return root.val
        root.val = self.update(root.left, index, value) + self.update(root.right, index, value)
        return root.val

    def query(self, root, l, r) -> int:
        if root.start > r or root.end < l:
            return 0
        if l <= root.start and root.end <= r:
            return root.val
        return self.query(root.left, l, r) + self.query(root.right, l, r)
        
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # Coordinate compression
        sorted_nums = sorted(set(nums + [2 * x for x in nums]))
        rank_map = {val: idx for idx, val in enumerate(sorted_nums)}

        self.tree = SegmentTree(len(sorted_nums))
        res = 0
        for n in reversed(nums):
            res += self.tree.query(self.tree.root, 0, rank_map[n]-1)
            self.tree.update(self.tree.root, rank_map[2*n], 1)
        return res