# dijkstra算法：
# 计算最短路径,带权的问题
# @time: 2019年12月17日 author:noc

# mapping = {
#     'A':['B', 'C'],
#     'B':['A', 'D', 'E'],
#     'C':['A'],
#     'D':['B', 'F'],
#     'E':['B', 'F'],
#     'F':['C', 'D', 'E'],
# }
# 带权值

import heapq
mapping = {
    'A':{'B':5, 'C':1},
    'B':{'A':5, 'D':1, 'C':2},
    'C':{'A':1, 'B':2, 'D':4, 'E':8},
    'D':{'B':1, 'C':4, 'E':3, 'F':6},
    'E':{'C':8, 'D':3},
    'F':{'D':6}
}

import math
def init_distance(start):
    '''初始化'''
    distance = {start:0}
    for v in mapping:
        if v != start:
            distance[v] = math.inf      # 真无穷大
    return distance

def bfs(start):
    pqueue = []      # 优先队列
    heapq.heappush(pqueue, (0, start))
    looked = set()  # 遍历过的节点
    # looked.add(start)   # 将开始的节点加入到遍历元组中
    parent = {start:None}
    distance = init_distance(start)    # 存放节点到start的路径权值
    # print(distance)
    while pqueue:    # 队列不为空
        pair = heapq.heappop(pqueue)      # 值最小的先出队
        d = pair[0]     # 节点权值
        v = pair[1]     # 节点
        looked.add(v)
        # print(looked)
        for i in mapping[v].keys():
            # print(i)
            if i not in looked:
                if d + mapping[v][i] < distance[i]:
                    heapq.heappush(pqueue, (d + mapping[v][i], i))      #
                    parent[i] = v   # 保存节点的父节点
                    distance[i] = d + mapping[v][i]
    return parent, distance

def path(start, end, parent, distance):
    '''输出路径长度和路径'''
    PathLength = distance[end]
    locate = [end]
    while end != start:
        end = parent[end]
        locate.insert(0, end)
    locate = '->'.join(locate)
    return PathLength, locate

if __name__ == '__main__':
    parent, distance = bfs('A')
    print(parent)
    print(distance)
    PathLength, locate = path('A', 'F', parent, distance)
    print(PathLength)
    print(locate)