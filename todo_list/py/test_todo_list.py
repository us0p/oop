import unittest
from todo_list import PRIORITIES, Task, TodoList
from datetime import datetime


class TestPriorityContants(unittest.TestCase):
    def test_important(self):
        self.assertEqual(PRIORITIES["IMPORTANT"], 1)

    def test_daily(self):
        self.assertEqual(PRIORITIES["DAILY"], 2)

    def test_maybe(self):
        self.assertEqual(PRIORITIES["MAYBE"], 3)


class TestTask(unittest.TestCase):
    def test_create_task_with_missing_data(self):
        try:
            Task("clean house", None, None)
            raise Exception("should have failed with missing obrigatory data")
        except Exception as e:
            self.assertEqual(e.__str__(), "missing obrigatory data")

    def test_create_task_with_out_range_priority(self):
        try:
            Task("clean house", "2024/4/19", 0)
            raise Exception("should have failed with invalid priority range")
        except Exception as e:
            self.assertEqual(e.__str__(), "invalid priority range")

    def test_create_task_with_priority_up(self):
        try:
            Task("clean house", "2024/4/19", 4)
            raise Exception("should have failed with invalid priority range")
        except Exception as e:
            self.assertEqual(e.__str__(), "invalid priority range")

    def test_create_task_invalid_due_date(self):
        try:
            Task("clean house", "2024-4-19", PRIORITIES["MAYBE"])
            raise Exception("should have failed with invalid due date")
        except Exception as e:
            self.assertEqual(e.__str__(), "invalid due date")

    def test_create_task(self):
        task = Task("clean house", "2024/04/19", PRIORITIES["MAYBE"])

        self.assertEqual(task.task_name, "clean house")
        self.assertEqual(task.due_date, datetime(2024, 4, 19))
        self.assertEqual(task.priority, PRIORITIES["MAYBE"])

    def test_update_task_due_date_throws_not_instance_datetime(self):
        try:
            task = Task(
                "clean house",
                "2024/04/19",
                PRIORITIES["MAYBE"]
            )
            task.update_task_due_date_with_date_obj({})
            raise Exception("should have failed with invalid object")
        except Exception as e:
            self.assertEqual(e.__str__(), "invalid object")

    def test_update_task_due_date_with_date_obj(self):
        task = Task(
            "clean house",
            "2024/04/19",
            PRIORITIES["MAYBE"]
        )
        new_date = datetime(2024, 4, 19)
        task.update_task_due_date_with_date_obj(new_date)
        self.assertEqual(task.due_date, new_date)


class TestTodoList(unittest.TestCase):
    def test_todo_list_creation(self):
        todo_list = TodoList()

        self.assertEqual(todo_list.list, [])

    def test_exception_not_task_object(self):
        try:
            todo_list = TodoList()
            todo_list.add_task({})
            raise Exception("should have failed with invalid object")
        except Exception as e:
            self.assertEqual(e.__str__(), "invalid object")

    def test_add_task_to_list(self):
        todo_list = TodoList()
        task = Task(
            "clean house",
            "2024/4/19",
            PRIORITIES["MAYBE"]
        )
        todo_list.add_task(task)
        self.assertEqual(todo_list.list, [task])

    def test_remove_task_from_list_and_return_tasks_removed_list(self):
        todo_list = TodoList()
        task = Task(
            "clean house",
            "2024/4/19",
            PRIORITIES["MAYBE"]
        )
        todo_list.add_task(task)
        removed_tasks = todo_list.remove_task("clean house")
        self.assertEqual(todo_list.list, [])
        self.assertEqual(removed_tasks, [task])

    def test_return_empty_list_if_task_doesnt_exist(self):
        todo_list = TodoList()
        removed_tasks = todo_list.remove_task("clean house")
        self.assertEqual(removed_tasks, [])

    def test_raise_exception_provided_object_not_task_update_task(self):
        try:
            todo_list = TodoList()
            todo_list.update_task("clean house", {})
            raise Exception("should have failed with invalid object")
        except Exception as e:
            self.assertEqual(e.__str__(), "invalid object")

    def test_update_task_raise_exception_not_found_task(self):
        try:
            todo_list = TodoList()
            task = Task(
                "wash dishes",
                "2024/04/19",
                PRIORITIES["IMPORTANT"],
            )
            todo_list.add_task(task)
            todo_list.update_task("clean house", task)
            raise Exception("should have failed with not found task")
        except Exception as e:
            self.assertEqual(e.__str__(), "task not found")

    def test_update_task_updates_provided_task_returns_updated_count(self):
        todo_list = TodoList()
        task = Task(
            "wash dishes",
            "2024/04/19",
            PRIORITIES["IMPORTANT"],
        )
        new_task = Task(
            "wash dishes",
            "2024/04/20",
            PRIORITIES["IMPORTANT"],
        )
        todo_list.add_task(task)
        update_count = todo_list.update_task(task.task_name, new_task)
        self.assertEqual(todo_list.list[0].due_date, new_task.due_date)
        self.assertEqual(update_count, 1)


if __name__ == "__main__":
    unittest.main()
