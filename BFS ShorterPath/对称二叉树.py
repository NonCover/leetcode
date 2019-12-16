class Root:
    def __init__(self, x, left=None, right=None):
        self.left = left
        self.right = right
        self.data = x
res = []
def middle(root):
    if root is None:
        return
    middle(root.left)
    res.append(root.data)
    middle(root.right)

def solution(tree):
    print(tree)
    if len(tree) == 1:
        return True
    r = tree.pop()
    l = tree.pop(0)
    if r == l:
        return solution(tree)
    else:
        return False

if __name__ == '__main__':
    tree = Root(1, Root(2, Root(3), Root(4)), Root(2, Root(4), Root(3)))
    m = middle(tree)
    print(res)
    print(solution(res))
