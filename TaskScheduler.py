class Solution:
    def task_cooldown_order(self, tasks, cooldown):
        """
        Task Scheduler 1: give an array of tasks in uppercase characters, and a cooldown n
        find out minimum time required to execute all tasks in order
        Time complexity: O(result time), space: O(types of tasks)
        :param tasks: str
        :param cooldown: int
        :return:
        """
        time = 0
        last_run_time = {}
        for task in tasks:
            if task not in last_run_time or last_run_time[task] + cooldown < time:
                last_run_time[task] = time
                time += 1
            else:
                idle_time = last_run_time[task] + cooldown + 1 - time
                time += idle_time
                last_run_time[task] = time
                time += 1
        return time

    def task_cooldown_order_limit_space(self, tasks, cooldown):
        """
        Followup of previous question, if number of types of tasks is huge, how to reduce space complexity
        :param tasks:
        :param cooldown:
        :return:
        """


    def task_cooldown_unorder(self, tasks, cooldonw):
        """
        LC 621. Task Scheduler: same as first question but no need of keeping the task order
        transform to a earliest deadline task scheduler problem. the deadline for each of the task is its position
        of the schedule in the optimal order
        :param tasks:
        :param cooldonw:
        :return:
        """
