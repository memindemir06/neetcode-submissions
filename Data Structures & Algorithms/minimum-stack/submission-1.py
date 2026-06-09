class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        i = len(self.minList) - 1
        while i > -1 and self.minList[i] < val:
            i -= 1
        self.minList.insert(i + 1, val)
        # print("push", self.minList)

    def pop(self) -> None:
        val = self.stack.pop()
        self.minList.remove(val)
        # print("pop", self.minList)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print("getMin", self.minList)
        return self.minList[-1]