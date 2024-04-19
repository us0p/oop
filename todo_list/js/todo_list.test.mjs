import { describe, it } from "node:test"
import assert from "node:assert"

import { TodoList, Task, PRIORITIES } from "./todo_list.mjs"

describe("Testing priorities constant", () => {
    it("Should match IMPORTANT to 1", () => {
        assert.strictEqual(PRIORITIES.IMPORTANT, 1)
    })
    it("Should match DAILY to 2", () => {
        assert.strictEqual(PRIORITIES.DAILY, 2)
    })
    it("Should match MAYBR to 3", () => {
        assert.strictEqual(PRIORITIES.MAYBE, 3)
    })
})

describe("Task class tests", () => {
    describe("Testing task creation", () => {
        it("Shouldn't be possible to create a task with missing data.", () => {
            try {
                new Task(
                    "clean house",
                )
                throw new Error("Should have failed with missing obrigatory data error")
            } catch (error) {
                assert.strictEqual(error.message, "missing obrigatory data")
            }
        })
        it("Should throw an date format error if provided dueDate is not as expected", () => {
            try {
                new Task(
                    "clean house",
                    "2024-4-19",
                    PRIORITIES.IMPORTANT
                )
                throw new Error("Should have failed with invalid due date")
            } catch (error) {
                assert.strictEqual(error.message, "invalid due date")
            }
        })
        it("Should create a task if all necessary data is provided.", () => {
            const todo = new Task(
                "clean house",
                "2024/4/19",
                PRIORITIES.IMPORTANT
            )

            assert.strictEqual(todo.taskName, "clean house")
            assert.deepStrictEqual(todo.dueDate, new Date(2024, 3, 19))
            assert.strictEqual(todo.priority, PRIORITIES.IMPORTANT)
        })
        it("Should throw an error if priority is > 3", () => {
            try {
                new Task(
                    "clean house",
                    "2024/4/19",
                    4,
                )
                throw new Error("should have failed with invalid priority range")
            } catch (error) {
                assert.strictEqual(error.message, "invalid priority range")
            }
        })
        it("Should throw an error if priority is < 1", () => {
            try {
                new Task(
                    "clean house",
                    "2024/4/19",
                    0,
                )
                throw new Error("should have failed with invalid priority range")
            } catch (error) {
                assert.strictEqual(error.message, "invalid priority range")
            }
        })
    })

    describe("Testing updateDueDateWithDateObj", () => {
        it("Should throw an error if the provided object if not an instance of Date", () => {
            try {
                const task = new Task(
                    "clean house",
                    "2024/4/19",
                    PRIORITIES.MAYBE
                )
                task.updateDueDateWithDateObj({})
                throw new Error("should have failed with invalid object")
            } catch (error) {
                assert.strictEqual(error.message, "invalid object")
            }
        })
        it("Should replace task current dueDate with the provided date", () => {
            const task = new Task(
                "clean house",
                "2024/4/19",
                PRIORITIES.MAYBE
            )
            const newDate = new Date(2024, 3, 20)
            task.updateDueDateWithDateObj(newDate)
            assert.deepStrictEqual(task.dueDate, newDate)
        })
    })
})

describe("TodoList class tests", () => {
    describe("Testing todo list creation", () => {
        it("Should return a new object with a empty todoList property", () => {
            const todoList = new TodoList()

            assert.deepStrictEqual(todoList.list, [])
        })
    })
    describe("Testing task addition", () => {
        it("Should throw an error if the provided object is not a Task", () => {
            try {
                const todoList = new TodoList()
                todoList.addTask({})
                throw new Error("should have thrown an error of invalid object")
            } catch (error) {
                assert.strictEqual(error.message, "invalid object")
            }
        })
        it("Should add provided task to todo list", () => {
            const todoList = new TodoList()
            const task = new Task(
                "clean house",
                "2024/4/19",
                PRIORITIES.IMPORTANT
            )
            todoList.addTask(task)
            assert.deepStrictEqual(todoList.list, [task])
        })
    })
    describe("Testing task deletion", () => {
        it("Should remove the task from the list and return a list of the removed tasks", () => {
            const task = new Task(
                "clean house",
                "2024/4/19",
                PRIORITIES.MAYBE
            )
            const todoList = new TodoList()
            todoList.addTask(task)

            const removedTask = todoList.removeTask(task.taskName)

            assert.deepStrictEqual(removedTask, [task])
            assert.deepStrictEqual(todoList.list, [])
        })
        it("Should return an empty list if the task is not present in the list", () => {
            const todoList = new TodoList()
            const removedTask = todoList.removeTask("clean house")
            assert.deepStrictEqual(removedTask, [])
        })
    })

    describe("Testing update task", () => {
        it("Should return an error if the provided object is not an instance of a Task", () => {
            try {
                const todoList = new TodoList()
                todoList.updateTask("clean house", {})
                throw new Error("should have failed with invalid object")
            } catch (error) {
                assert.strictEqual(error.message, "invalid object")
            }
        })
        it("Should return an error if there's no task with the provided name in the list", () => {
            try {
                const todoList = new TodoList()
                const taskUpdated = new Task(
                    "clean house",
                    "2024/4/19",
                    PRIORITIES.MAYBE
                )
                todoList.updateTask("clean house", taskUpdated)
                throw new Error("should have failed with task not found")
            } catch (error) {
                assert.strictEqual(error.message, "task not found")
            }
        })
        it("Should update matched task items with the provided new task object and return the number of updated items", () => {
            const todoList = new TodoList()
            const task = new Task(
                "clean house",
                "2024/4/19",
                PRIORITIES.MAYBE
            )
            const taskUpdated = new Task(
                "clean house",
                "2024/4/20",
                PRIORITIES.MAYBE
            )
            todoList.addTask(task)
            const updatedTasks = todoList.updateTask(task.taskName, taskUpdated)
            assert.deepStrictEqual(todoList.list[0].dueDate, new Date(2024, 3, 20))
            assert.strictEqual(updatedTasks, 1)
        })
    })
})
