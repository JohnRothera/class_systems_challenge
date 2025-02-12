class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        self.todo_list.append(todo)

    def incomplete(self):
        # incomplete_tasks = []
        # for task in self.todo_list:
        #     if task.is_complete == False:
        #         incomplete_tasks.append(task)
        # return incomplete_tasks
        return [task for task in self.todo_list if task.is_complete == False]

    def complete(self):
        # complete_tasks = []
        # for task in self.todo_list:
        #     if task.is_complete == True:
        #         complete_tasks.append(task)
        # return complete_tasks
        return [task for task in self.todo_list if task.is_complete == True]

    def give_up(self):
        for task in self.todo_list:
            task.is_complete = True
