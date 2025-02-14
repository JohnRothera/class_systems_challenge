from unittest.mock import Mock
from lib.todo_task_formatter import TodoFormatter
from lib.todo import Todo


def test_task_can_be_formatted():
    todo_task = Todo("I've got to get my head around this flipping mocking shite!")
    task_formatter = TodoFormatter(todo_task)
    formatted_task = task_formatter.format()
    assert (
        formatted_task
        == "- [ ] I've got to get my head around this flipping mocking shite!"
    )


def test_task_can_be_marked_complete_and_returned_formatted():
    todo_task = Todo("I've got to get my head around this flipping mocking shite!")
    todo_task.mark_complete()
    task_formatter = TodoFormatter(todo_task)
    formatted_task = task_formatter.format()
    assert (
        formatted_task
        == "- [x] I've got to get my head around this flipping mocking shite!"
    )
