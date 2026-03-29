classDiagram
    class Owner {
        +name
        +available_time
        +preferences
        +pets: List[Pet]
        +add_pet(pet)
        +set_available_time(time)
        +update_preferences(preferences)
    }
    class Pet {
        +name
        +pet_type
        +age
        +health_notes
        +tasks: List[Task]
        +add_task(task)
        +view_tasks()
    }
    class Task {
        +task_name
        +duration
        +priority
        +category
        +completed
        +mark_complete()
        +update_priority(new_priority)
    }
    class Scheduler {
        +tasks
        +available_time
        +sort_tasks_by_priority()
        +generate_daily_plan()
        +explain_plan()
    }
    Owner --> Pet : owns
    Pet --> Task : contains
    Scheduler --> Task : schedules