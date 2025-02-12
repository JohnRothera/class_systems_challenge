class Todo:
    def __init__(self, task):
        self.task = task
        self.is_complete = False

    def __repr__(self):
        return f"Task: {self.task} Completed: {self.is_complete}"

    def mark_complete(self):
        self.is_complete = True
