from PIL import Image
import random
import os
from collections import deque
from ToyClasses import Search, Node, Thing, SaveAdapter, Place


def test():
    arr = []

    for x in range(0, 128):
        for y in range(0, 128):
            arr.append(y + 1)

    imge = Image.open("/Users/lennont/Downloads/test.jpeg")

    for i in range(0, imge.size[0]):
        for j in range(0, imge.size[1]):
            index = (i, j)

            rnd = random.randint(0, (len(arr) - 1))
            v = arr[rnd]

            value = (v, v, v)  ## color value
            del arr[rnd]

            imge.putpixel(index, value)

    imge.save('/Users/lennont/Downloads/test2.jpeg')


def checkDup():
    group1 = os.listdir('/Users/lennont/Movies/jx-backup/11')
    group2 = os.listdir('/Users/lennont/Movies/jx-backup/print')

    others = []
    for i in group2:
        if i not in group1:
            others.append(i)

    if len(others) > 0:
        for j in others:
            print(j)


list = [1, 3, 5, 8, 9, 13, 19, 50]


# 二分法查找
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return mid

    return None


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for item in range(1, len(arr)):
        if arr[item] < smallest:
            smallest = arr[item]
            smallest_index = item

    return smallest_index


#  选择排序
def selectionSort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        small = findSmallest(arr)
        sorted_arr.append(arr.pop(small))
    return sorted_arr


# 递归方式求阶乘
def factorial(num):
    if num == 1:
        # 基线条件
        return num
    else:
        # 递归条件
        return num * factorial(num - 1)


# 使用分而治之的策略 运用递归方式实现的： 求最大公约数算法
def getCommonDivisor(width, height):
    small = width
    big = height
    if small > big:
        small = height
        big = width
    if big % small == 0:
        return small
    else:
        return getCommonDivisor(big % small, small)


# 使用分而治之的策略 运用递归方式实现的：数组求和
def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


# 递归方式实现的二分法查找
def binary_serach_recursive(arr, low, high, item):
    if low > high:
        return None
    mid = (low + high) // 2  # python3中的地板除
    print(mid)
    if arr[mid] == item:
        return mid
    elif arr[mid] < item:
        return binary_serach_recursive(arr, mid + 1, high, item)
    else:
        return binary_serach_recursive(arr, low, mid - 1, item)


def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph["you"] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search_queue = deque()
search_queue += graph["you"]


def BFS(s_queue):
    searched = []

    while s_queue:
        person = s_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is found!")
                return True
            else:
                searched.append(person)
                s_queue += graph[person]
    return False


# gra = {}
# # gra['start'] = {}
# # gra['start']['a'] = 6
# # gra['start']['b'] = 2
# # gra['a'] = {}
# # gra['a']['final'] = 1
# # gra['b'] = {}
# # gra['b']['a'] = 3
# # gra['b']['final'] = 5
# # gra['final'] = {}

gra = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'final': 1
    },
    'b': {
        'a': 3,
        'final': 5
    },
    'final': {}
}

# 到起点到开销
costs = {
    'a': 6,
    'b': 2,
    'final': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'final': None
}


def find_lowest_cost_node(lst, processed):
    lowest_node = None
    lowest_cost = float('inf')
    for node in lst:
        cost = lst[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_node = node
    return lowest_node


# 狄克斯特拉算法
def djistra():
    processed = []  # 已经处理节点
    node = find_lowest_cost_node(costs, processed)  # 开销最小节点
    while node is not None:
        cost = costs[node]
        neighbor = gra[node]
        for n in neighbor.keys():
            new_cost = cost + neighbor[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    print(costs['final'])

    path = ['final']
    while path[0] in parents:
        path.insert(0, parents[path[0]])

    for i in range(0, len(path)):
        print(path[i])


# 贪心算法 每次获取的结果不一样 是因为set集合没有顺序，每次遍历时可能都不一样
def tanxin():
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"}
    }

    best_station = None
    final_stations = set()

    while states_needed:
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states  # 尚未覆盖的州
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        print("states_covered", states_covered)
        print("best", best_station)

        states_needed -= states_covered
        final_stations.add(best_station)
        stations.pop(best_station)
        print("needed", states_needed)

    return final_stations


# 动态规划处理背包问题
def dynamic_plan(all_items, max_capacity, granularity=1):
    max_steps = int(max_capacity / granularity)  # 获取步数

    plan_table = [[0 for i in range(max_steps)] for j in range(len(all_items))]

    for i in range(len(all_items)):  # i表示哪个物品
        for j in range(max_steps):
            cur_bag_capacity = (j + 1) * granularity  # 表示背包容量
            if i == 0:  # 第一行 直接放进去
                if all_items[0].get_weight() <= cur_bag_capacity:  # 只放当前物品 可以放入背包
                    plan_table[0][j] = SaveAdapter(all_items[0].get_value(), [all_items[0]])
                else:
                    plan_table[0][j] = SaveAdapter(0, [])  # 第一个就放不进去 直接赋空
            else:  # 其他行 用当前物品做叠加
                last_max_value = plan_table[i - 1][j].value

                new_max_value = 0
                last_lst = []
                if all_items[i].get_weight() <= cur_bag_capacity:  # 只放当前物品
                    new_max_value = all_items[i].get_value()

                if cur_bag_capacity - all_items[i].get_weight() > 0:  # 放完当前行的物品后还有空间
                    last_table = plan_table[i - 1][
                        int((cur_bag_capacity - all_items[i].get_weight()) / granularity) - 1]  # 直接查阅已算完部分，获取其最大价值
                    new_max_value += last_table.value
                    last_lst = last_table.lst

                # 判断是不是更有价值
                if new_max_value > last_max_value:  # 可以放入更多
                    last_lst.append(all_items[i])  # append方法返回None 不能直接用
                    plan_table[i][j] = SaveAdapter(new_max_value, last_lst)
                else:
                    # plan_table[i][j] = plan_table[i - 1][j]  # 这种写法有问题 相当于浅拷贝了一个SaveAdapter 导致意外的交叉访问其lst
                    plan_table[i][j] = plan_table[i - 1][j].copy()

    return plan_table


if __name__ == '__main__':
    # test()
    # checkDup()
    # print(selectionSort([9, 10 ,1, 5, 3]))
    # print(factorial(5))
    # print(getCommonDivisor(512, 180))
    # print(recursive_sum([1, 3, 5, 9, 50]))
    # print(quick_sort([12, 9, 3, 16, 50, 28]))
    # print(binary_serach_recursive([2, 4, 8, 9, 15, 20], 0, 5, 20))
    # BFS(search_queue)

    # djistra()
    # print(tanxin())

    all_things = [
        Thing("A", 2, 1500),
        Thing("B", 3, 2000),
        Thing("C", 4, 3000),
        Thing("D", 2, 2500),
        Thing("E", 2, 1000),
        # Thing("Diamond", 5, 100000000)
    ]
    bag_capacity = 6  # 背包最多装多少

    all_places = [
        Place("west", 0.5, 7),
        Place("global", 0.5, 6),
        Place("draw", 1, 9),
        Place("britain", 2, 9),
        Place("church", 0.5, 8)
    ]

    max_days = 2
    step = 0.5

    dynamic_plan(all_things, bag_capacity)[len(all_things) - 1][bag_capacity - 1].print()
    # dynamic_plan(all_places, max_days, step)[len(all_places) - 1][int(max_days / step) - 1].print()
