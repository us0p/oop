from datetime import datetime

PRIORITIES = {
    "IMPORTANT": 1,
    "DAILY": 2,
    "MAYBE": 3
}


class Task:
    _task_name = ""
    _due_date = None
    _priority = None

    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        self._task_name = task_name

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = self._parse_due_date(due_date)

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        if (priority < 1 or priority > 3):
            raise Exception("invalid priority range")

        self._priority = priority

    def __init__(self, task_name, due_date, priority):
        if (not task_name or not due_date or priority != 0 and not priority):
            raise Exception("missing obrigatory data")

        if (priority < 1 or priority > 3):
            raise Exception("invalid priority range")

        self._task_name = task_name
        self._priority = priority
        self._due_date = self._parse_due_date(due_date)

    def _parse_due_date(self, due_date):
        dateValues = due_date.split("/")

        if (len(dateValues) != 3):
            raise Exception("invalid due date")

        return datetime(
            int(dateValues[0]),
            int(dateValues[1]),
            int(dateValues[2])
        )

    def update_task_due_date_with_date_obj(self, newDue):
        if (not isinstance(newDue, datetime)):
            raise Exception("invalid object")

        self._due_date = newDue


class TodoList:
    _list = []

    @property
    def list(self):
        return [i for i in self._list]

    def __init__(self):
        self._list = []

    def add_task(self, task):
        if (not isinstance(task, Task)):
            raise Exception("invalid object")

        self._list.append(task)

    def remove_task(self, task_name):
        removed_tasks = []
        updated_tasks = []
        for task in self._list:
            if (task.task_name == task_name):
                removed_tasks.append(task)
                continue
            updated_tasks.append(task)

        self._list = updated_tasks
        return removed_tasks

    def update_task(self, task_name, updatedTask):
        if (not isinstance(updatedTask, Task)):
            raise Exception("invalid object")

        updated_count = 0

        for task in self._list:
            if (task.task_name == task_name):
                updated_count += 1
                task.task_name = updatedTask.task_name
                task.priority = updatedTask.priority
                task.update_task_due_date_with_date_obj(updatedTask.due_date)

        if (not updated_count):
            raise Exception("task not found")

        return updated_count
