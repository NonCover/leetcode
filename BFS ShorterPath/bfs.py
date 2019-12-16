mapping = {
    'A':['B', 'C'],
    'B':['A', 'D', 'E'],
    'C':['A'],
    'D':['B', 'F'],
    'E':['B', 'F'],
    'F':['C', 'D', 'E'],
}
locate = {}
def bfs(start):
    queue = [start]      # 队列
    looked = set()  # 遍历过的节点
    looked.add(start)   # 将开始的节点加入到遍历元组中
    while queue:    # 队列不为空
        v = queue.pop(0)      # 出队
        # print(v)
        for i in mapping[v]:
            if i not in looked:
                if i not in locate:
                    locate[i] = v
                looked.add(i)
                queue.append(i)
def shortpath(start, end):
    path = []
    topNode = locate[end]
    while topNode != start:
        path.append(topNode)
        topNode = locate[topNode]
    return list(start) + path[::-1] + list(end)

def dfs(start):
    '''将入队换成入栈就是bfs 到 dfs 的改变'''
    pass

if __name__ == '__main__':
    bfs('C')
    print(locate)
    print(shortpath('C', 'D'))