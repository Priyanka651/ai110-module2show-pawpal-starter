from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner("Jordan", 60, "High priority tasks first")

# Create at least two pets
pet1 = Pet("Mochi", "cat", 2, "No health issues")
pet2 = Pet("Buddy", "dog", 4, "Needs daily exercise")

# Create tasks
task1 = Task("Feed Mochi", 10, 3, "Food")
task2 = Task("Walk Buddy", 20, 3, "Exercise")
task3 = Task("Give Buddy medicine", 5, 2, "Health")

# Add tasks to pets
pet1.add_task(task1)
pet2.add_task(task2)
pet2.add_task(task3)

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Collect all tasks from all pets
all_tasks = []
for pet in owner.pets:
    all_tasks.extend(pet.view_tasks())

# Run scheduler
scheduler = Scheduler(all_tasks, owner.available_time)
daily_plan = scheduler.generate_daily_plan()

# Print schedule nicely
print("\nToday's Schedule:")
for task in daily_plan:
    print(f"- {task.task_name} ({task.duration} min, priority {task.priority})")

print("\nExplanation:")
print(scheduler.explain_plan())