from unittest.mock import Mock
from lib.todo_task_formatter import TodoFormatter
from lib.todo import Todo


def test_mock_task_can_be_formatted():
    mock_todo = Mock()
    mock_todo.task = "I've got to get my head around this flipping mocking shite!"
    mock_todo.mark_complete = True
    task_formatter = TodoFormatter(mock_todo)
    formatted_task = task_formatter.format()
    assert (
        formatted_task
        == "- [x] I've got to get my head around this flipping mocking shite!"
    )


def test_mock_incomplete_task_can_be_formatted():
    mock_todo = Mock()
    mock_todo.task = "I've got to get my head around this flipping mocking shite!"
    mock_todo.is_complete = False
    task_formatter = TodoFormatter(mock_todo)
    formatted_task = task_formatter.format()
    assert (
        formatted_task
        == "- [ ] I've got to get my head around this flipping mocking shite!"
    )
