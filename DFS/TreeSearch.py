'''
    5
   / \
  1   4
     / \
    3   6
'''
class Root:
    def __init__(self, x, left=None, right=None):
        self.left = left
        self.right = right
        self.val = x

def solution(root):
    if not root:
        return True
    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        root, lower, upper = stack.pop()
        print(root, lower, upper)
        if not root:
            continue
        if root.val <= lower or root.val >= upper:      # 当左子树 大于 父节点  or  右子树 小于 父节点
            return False

        stack.append((root.right, root.val, upper))
        stack.append((root.left, lower, root.val))

    return True

if __name__ == '__main__':
    root = Root(5, Root(1), Root(4, Root(3), Root(6)))
    print(solution(root))