classDiagram
    class Owner {
        +name
        +available_time
        +preferences
        +add_pet()
        +set_available_time()
        +update_preferences()
    }
    class Pet {
        +name
        +pet_type
        +age
        +health_notes
        +add_task()
        +view_tasks()
    }
    class Task {
        +task_name
        +duration
        +priority
        +category
        +completed
        +mark_complete()
        +update_priority()
    }
    class Scheduler {
        +tasks
        +available_time
        +sort_tasks_by_priority()
        +generate_daily_plan()
        +explain_plan()
    }
    Owner --> Pet : has
    Pet --> Task : has
    Scheduler --> Task : manages    