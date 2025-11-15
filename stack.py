class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self, item):
        self.__stack_list.append(item)
    def pop(self):
        item = self.__stack_list[-1]
        del self.__stack_list [-1]
        return item

class smartStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0
        self.__max = []
        self.__min = []

    def push(self, item):
        self.__sum += item
        if not self.__max or item >= self.__max[-1]:
            self.__max.append(item)
        if not self.__min or item <= self.__min[-1]:
            self.__min.append(item)
        super().push(item)

    def pop(self):
        item = super().pop()
        self.__sum-= item
        if self.__max and item == self.__max[-1]:
            del self.__max[-1]
        if self.__min and item == self.__min[-1]:
            del self.__min[-1]
        return item

    def get_sum(self):
        return self.__sum

    def get_max(self):
        return self.__max[-1] if self.__max else None

    def get_min(self):
        return self.__min[-1] if self.__min else None

s = smartStack()
s.push(5); s.push(10); s.push(3)
print(s.get_sum(), s.get_max(), s.get_min())
print(s.pop())
print(s.get_min())

print(s.__dict__)



