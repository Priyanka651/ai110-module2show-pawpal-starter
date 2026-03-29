from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    task_name: str
    duration: int
    priority: int
    category: str
    completed: bool = False

    def mark_complete(self) -> None:
        self.completed = True

    def update_priority(self, new_priority: int) -> None:
        self.priority = new_priority


@dataclass
class Pet:
    name: str
    pet_type: str
    age: int
    health_notes: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def view_tasks(self) -> List[Task]:
        return self.tasks


@dataclass
class Owner:
    name: str
    available_time: int
    preferences: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)


    def set_available_time(self, time: int) -> None:
        self.available_time = time

    def update_preferences(self, preferences: str) -> None:
        self.preferences = preferences


class Scheduler:
    def __init__(self, tasks, available_time):
        self.tasks = tasks
        self.available_time = available_time

    def sort_tasks_by_priority(self):
        return sorted(self.tasks, key=lambda task: task.priority, reverse=True)

    def generate_daily_plan(self):
        sorted_tasks = self.sort_tasks_by_priority()
        selected_tasks = []
        total_time = 0

        for task in sorted_tasks:
            if not task.completed and total_time + task.duration <= self.available_time:
                selected_tasks.append(task)
                total_time += task.duration

        return selected_tasks

    def explain_plan(self):
        daily_plan = self.generate_daily_plan()

        if not daily_plan:
            return "No tasks were selected because none could fit within the available time."

        task_names = [task.task_name for task in daily_plan]
        task_list = ", ".join(task_names)

        return f"The daily plan includes {task_list}. These tasks were selected because they are incomplete, have higher priority, and fit within the available time."

