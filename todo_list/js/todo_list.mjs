export const PRIORITIES = {
    IMPORTANT: 1,
    DAILY: 2,
    MAYBE: 3
}

export class Task {
    /** @type {string} */
    #taskName
    /** @type {Date} */
    #dueDate
    /** @type {number} */
    #priority

    /**
     * @param {string} taskName
     * @param {string} dueDate
     * @param {number} priority
     */
    constructor(taskName, dueDate, priority) {
        if (priority < 1 || priority > 3) {
            throw new Error("invalid priority range")
        }

        if (!taskName || !dueDate || !priority) {
            throw new Error("missing obrigatory data")
        }

        this.#taskName = taskName;
        this.#dueDate = this.#parseDueDate(dueDate);
        this.#priority = priority;
    }

    get taskName() {
        return this.#taskName
    }

    set taskName(taskName) {
        this.#taskName = String(taskName)
    }

    get dueDate() {
        return this.#dueDate
    }

    set dueDate(dueDate) {
        this.#dueDate = this.#parseDueDate(dueDate);
    }

    get priority() {
        return this.#priority
    }

    set priority(priority) {
        if (priority < 1 || priority > 3) {
            throw new Error("invalid priority range")
        }

        this.#priority = priority
    }

    /**
     * @param {string} dueDate - expects string in the format: yyyy/mm/dd
     * @returns {Date}
     */
    #parseDueDate(dueDate) {
        const [year, month, dd] = dueDate.split("/")

        if (!year || !month || !dd) {
            throw new Error("invalid due date")
        }

        return new Date(year, Number(month) - 1, dd)
    }

    /**
     * @param {Date} newDate
     */
     updateDueDateWithDateObj(newDate) {
         if (!(newDate instanceof Date)) {
             throw new Error("invalid object")
         }

         this.#dueDate = newDate
     }
}

export class TodoList {
    /** @type {Array<Task>} */
    #list = [];

    get list() {
        return [...this.#list]
    }

    /**
     * @param {Task} task
     */
    addTask(task) {
        if (!(task instanceof Task)) {
            throw new Error("invalid object")
        }

        this.#list.push(task)
    }

    /**
     * @param {string} taskName
     * @returns {Array<Task>}
     */
    removeTask(taskName) {
        const removedTasks = []
        const newList = []
        for (const task of this.#list) {
            if (task.taskName === taskName) {
                removedTasks.push(task)
                continue
            }
            newList.push(task)
        }
        this.#list = newList

        return removedTasks
    }

    /**
     * @param {string} taskName
     * @param {Task} updatedTask
     * @returns {number}
     */
    updateTask(taskName, updatedTask) {
        if (!(updatedTask instanceof Task)) {
            throw new Error("invalid object")
        }

        let updatedTasks = 0;

        for (const task of this.#list) {
            if (task.taskName === taskName) {
                updatedTasks++
                task.taskName = updatedTask.taskName
                task.priority = updatedTask.priority
                task.updateDueDateWithDateObj(updatedTask.dueDate)
            }
        }

        if (updatedTasks == 0) {
            throw new Error("task not found")
        }

        return updatedTasks
    }
}
