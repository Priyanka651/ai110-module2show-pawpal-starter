from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Priyanka", 40, "High priority tasks first")

pet = Pet("Buddy", "Dog", 3, "Healthy")

task1 = Task("Feeding", 10, 5, "Food")
task2 = Task("Walk", 20, 4, "Exercise")
task3 = Task("Medicine", 5, 5, "Health")
task4 = Task("Grooming", 15, 2, "Care")

pet.add_task(task1)
pet.add_task(task2)
pet.add_task(task3)
pet.add_task(task4)

owner.add_pet(pet)

scheduler = Scheduler(pet.view_tasks(), owner.available_time)
daily_plan = scheduler.generate_daily_plan()

print("Selected tasks for today:")
for task in daily_plan:
    print(f"- {task.task_name} ({task.duration} min, priority {task.priority})")

print()
print("Explanation:")
print(scheduler.explain_plan())