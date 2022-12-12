class Stack:
    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(", ".join(self.__list))

    def push(self, elem):
        self.__list.append(elem)

    def pop(self):
        if len(self.__list) == 0:
            return None
        else:
            return self.__list.pop()

class TaskManager:
    def __init__(self):
        self.task = {}

    def __str__(self):
        string = ""
        for i in sorted(self.task.keys()):
            string += str(i) + " " + str(self.task[i]) + ";\n"
        return string

    def new_task(self, task, priority):
        if not priority in self.task.keys():
            self.task[priority] = Stack()
            self.task[priority].push(task)
        else:
            new_stack = Stack()
            while len(str(self.task[priority])) != 0:
                value = self.task[priority].pop()
                if value != task:
                    new_stack.push(value)
            new_stack.push(task)
            self.task[priority] = new_stack


    def delete_task(self, priority):
        if not priority in self.task.keys():
            print("Задач с таким приоритетом нет!")
        else:
            print("Удалили задачу:", self.task[priority].pop())
            if len(str(self.task[priority])) == 0:
                self.task.pop(priority)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)