import unittest
from pawpal_system import Task, Scheduler


class TestPawPalSystem(unittest.TestCase):

    def test_sort_tasks_by_priority(self):
        task1 = Task("Feeding", 10, 3, "Food")
        task2 = Task("Walk", 20, 5, "Exercise")
        task3 = Task("Grooming", 15, 1, "Care")

        scheduler = Scheduler([task1, task2, task3], 60)
        sorted_tasks = scheduler.sort_tasks_by_priority()

        self.assertEqual(sorted_tasks[0].task_name, "Walk")
        self.assertEqual(sorted_tasks[1].task_name, "Feeding")
        self.assertEqual(sorted_tasks[2].task_name, "Grooming")

    def test_generate_daily_plan_with_time_limit(self):
        task1 = Task("Feeding", 10, 5, "Food")
        task2 = Task("Walk", 20, 4, "Exercise")
        task3 = Task("Grooming", 30, 2, "Care")

        scheduler = Scheduler([task1, task2, task3], 25)
        daily_plan = scheduler.generate_daily_plan()

        self.assertEqual(len(daily_plan), 1)
        self.assertEqual(daily_plan[0].task_name, "Feeding")

    def test_completed_tasks_are_skipped(self):
        task1 = Task("Medicine", 5, 5, "Health", completed=True)
        task2 = Task("Walk", 20, 4, "Exercise")

        scheduler = Scheduler([task1, task2], 30)
        daily_plan = scheduler.generate_daily_plan()

        self.assertEqual(len(daily_plan), 1)
        self.assertEqual(daily_plan[0].task_name, "Walk")


if __name__ == "__main__":
    unittest.main()