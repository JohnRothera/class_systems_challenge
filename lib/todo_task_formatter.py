class TodoFormatter:
    def __init__(self, task):  # task is an instance of Task
        self.task = task

    def format(self):
        if self.task.is_complete:
            return f"- [x] {self.task.task}"
        else:
            return f"- [ ] {self.task.task}"
