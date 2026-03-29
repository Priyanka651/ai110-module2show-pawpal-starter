from pawpal_system import Task, Pet


def test_mark_complete_changes_status():
    task = Task("Feed Mochi", 10, 3, "Food")
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet("Mochi", "cat", 2, "No health issues")
    assert len(pet.tasks) == 0

    task = Task("Morning walk", 20, 3, "Exercise")
    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].task_name == "Morning walk"