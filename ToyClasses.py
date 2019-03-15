class Search:
    def __init__(self):
        pass


class Node:
    def __init__(self, parents, children, weight):
        self.parents = parents
        self.children = children
        self.weight = weight


class IDynamicable:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def print(self):
        pass

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value


class Thing(IDynamicable):
    def __init__(self, name, weight, value):
        # IDynamicable.__init__(self, weight, value)  # 老写法
        super(Thing, self).__init__(weight, value)
        self.weight = weight
        self.name = name
        self.value = value

    def print(self):
        print("{ name: " + str(self.name) + ", weight: " + str(self.weight) + ", value: " + str(self.value) + " }", end='')


class Place(IDynamicable):
    def __init__(self, name, cost, rate):
        super(Place, self).__init__(cost, rate)
        self.name = name
        self.cost = cost
        self.rate = rate

    def print(self):
        print("{ name: " + str(self.name) + ", cost: " + str(self.cost) + ", rate: " + str(self.rate) + " }", end='')


class SaveAdapter:
    def __init__(self, value, lst):
        self.value = value
        self.lst = lst

    def print(self, pre='', end=''):
        print(pre, end='')

        print("value: " + str(self.value) + " ", end='')
        print("list: { ", end='')
        try:
            for i, item in enumerate(self.lst):
                item.print()
                if i < len(self.lst) - 1:
                    print(", ", end='')
            print(" }")
        except TypeError:
            pass

        print(end, end='')

    def append(self, value, sublist):
        self.value += value
        self.lst += sublist

    def copy(self):
        new_instance = SaveAdapter(self.value, self.lst.copy())
        return new_instance
