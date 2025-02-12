from lib.todo import *
from lib.todo_list import *

"""
Test that we can set a new task and mark its complete status to False.
"""


def test_new_task_and_complete_status_is_false():
    new_todo = Todo("Clean teeth")
    assert new_todo.is_complete == False


"""
Test that we can mark the task as complete using a function.
"""


def test_mark_complete_function_changes_todo_object():
    new_todo = Todo("Clean teeth")
    new_todo.mark_complete()
    assert new_todo.is_complete == True


"""
Running coverage shows me that we should have a test 
to see the __repr__ magic function is functioning how 
we expect
"""


def test_repr_functionality_and_output():
    new_todo = Todo("Clean teeth")
    assert repr(new_todo) == "Task: Clean teeth Completed: False"


"""
Move into integration testing so we can add multiple tasks.
"""


def test_add_tasks_to_list():
    new_todo_list = TodoList()
    new_task1 = Todo("Walk dog")
    new_task2 = Todo("Brush hair")
    new_task3 = Todo("Wash clothes")
    new_todo_list.add(new_task1)
    new_todo_list.add(new_task2)
    new_todo_list.add(new_task3)
    assert new_todo_list.todo_list == [new_task1, new_task2, new_task3]


"""
Test incomplete function returns list of any instances
where todo.iscomplete is marked as False.
"""


def test_incomplete_function_where_all_tasks_are_incomplete():
    new_todo_list = TodoList()
    new_task1 = Todo("Walk dog")
    new_task2 = Todo("Brush hair")
    new_task3 = Todo("Wash clothes")
    new_todo_list.add(new_task1)
    new_todo_list.add(new_task2)
    new_todo_list.add(new_task3)
    assert new_todo_list.incomplete() == [new_task1, new_task2, new_task3]


"""
Test for an example where a task has been marked as complete.
"""


def test_mark_complete_and_incomplete_function_are_compatible():
    new_todo_list = TodoList()
    new_task1 = Todo("Walk dog")
    new_task2 = Todo("Brush hair")
    new_task3 = Todo("Wash clothes")
    new_todo_list.add(new_task1)
    new_todo_list.add(new_task2)
    new_todo_list.add(new_task3)
    new_task1.mark_complete()
    assert new_task1.is_complete == True
    assert new_task2.is_complete == False
    assert new_todo_list.incomplete() == [new_task2, new_task3]


"""
Test the complete function. This should be very 
similar to the incomplete function.
"""


def test_complete_function_returns_expected_list():
    new_todo_list = TodoList()
    new_task1 = Todo("Walk dog")
    new_task2 = Todo("Brush hair")
    new_task3 = Todo("Wash clothes")
    new_todo_list.add(new_task1)
    new_todo_list.add(new_task2)
    new_todo_list.add(new_task3)
    new_task1.mark_complete()
    assert new_task1.is_complete == True
    assert new_task2.is_complete == False
    assert new_todo_list.complete() == [new_task1]


"""
Finally test that give up function marks all tasks complete
regardless of whether they were marked complete already.
"""


def test_give_up_function_behaves_as_expected():
    new_todo_list = TodoList()
    new_task1 = Todo("Walk dog")
    new_task2 = Todo("Brush hair")
    new_task3 = Todo("Wash clothes")
    new_todo_list.add(new_task1)
    new_todo_list.add(new_task2)
    new_todo_list.add(new_task3)
    new_task1.mark_complete()
    assert new_task1.is_complete == True
    assert new_task2.is_complete == False

    new_todo_list.give_up()
    assert new_task1.is_complete == True
    assert new_task2.is_complete == True
    assert new_todo_list.incomplete() == []
